<?php

$input_file_name = 'politik_input.xml';

$output_file_name = 'my_output.xml';

// read xml to object
$xml = simplexml_load_file($input_file_name)
  or die('Error: cannot read file or create object');
$namespaces = $xml->getNamespaces(true);


// create output xml
$dom = new DOMDocument();
$dom->encoding = 'utf-8';
$dom->xmlVersion = '1.0';
$dom->formatOutput = true;

$root = $dom->createElement('n24news');

for ($i = 0; $i < 3; $i++) {
  $news_node = $dom->createElement('news');
  $child_node_subline = $dom->createElement('subline', $xml->channel->item[$i]->children($namespaces['welt'])->topic);
  $child_node_headline = $dom->createElement('headline', $xml->channel->item[$i]->title);
  $child_node_source = $dom->createElement('source', 'Quelle: ');
  $child_node_textmessage = $dom->createElement('textmessage', $xml->channel->item[$i]->description);
  $child_node_published = $dom->createElement('published', $xml->channel->item[$i]->pubDate);
  $attr_published = new DOMAttr('type', 'timestamp');
  $child_node_published->setAttributeNode($attr_published);
  $child_node_image = $dom->createElement('image', 'https://weltooh.de/main/img736x414/some_cropped_image_' . $i . '.jpg');
  $attr_image = new DOMAttr('type', 'remotefile');
  $child_node_image->setAttributeNode($attr_image);
  $child_node_thumb = $dom->createElement('thumb', '');
  $attr_thumb = new DOMAttr('type', 'remotefile');
  $child_node_thumb->setAttributeNode($attr_thumb);
  $child_node_video = $dom->createElement('video', '');
  $attr_video = new DOMAttr('type', 'remotefile');
  $child_node_video->setAttributeNode($attr_video);
  $child_node_webUrl = $dom->createElement('webUrl', $xml->channel->item[$i]->link);

  $news_node->appendChild($child_node_subline);
  $news_node->appendChild($child_node_headline);
  $news_node->appendChild($child_node_source);
  $news_node->appendChild($child_node_textmessage);
  $news_node->appendChild($child_node_published);
  $news_node->appendChild($child_node_image);
  $news_node->appendChild($child_node_thumb);
  $news_node->appendChild($child_node_video);
  $news_node->appendChild($child_node_webUrl);
  $root->appendChild($news_node);
}
$dom->appendChild($root);

$dom->save($output_file_name);
echo "$output_file_name has been successfully created";
