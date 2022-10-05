<?php

$article_count = 3;
$input_file_name = 'politik_input.xml';
$output_file_name = 'my_output.json';

// read xml to object
$xml = simplexml_load_file($input_file_name)
  or die('Error: cannot read file or create object');
$namespaces = $xml->getNamespaces(true);

// build json array
$array = array();
for ($i = 0; $i < $article_count; $i++) {
  array_push($array, array(
    "headline" => (string)$xml->channel->item[$i]->title,
    "subline" => (string)$xml->channel->item[$i]->children($namespaces['welt'])->topic,
    "text" => (string)$xml->channel->item[$i]->description,
    "img" => "https:\/\/weltooh.de\/main\/img736x414\/some_generated_img.jpg",
    "source" => "Quelle: " . $xml->channel->item[$i]->children($namespaces['dc'])->source,
    "video" => ""
  ));
}

// encode and write json file
$json = json_encode($array, JSON_PRETTY_PRINT);
$bytes = file_put_contents($output_file_name, $json);
echo "$output_file_name has been successfully created";
