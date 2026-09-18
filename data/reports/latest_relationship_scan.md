# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T06:08:08.625826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8410`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `40.0024` n `149` status `ready` deltaP `-0.0061` edge `3.3569` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8811` n `52` status `ready` deltaP `-7.2467` edge `1.2276` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8811` n `52` status `ready` deltaP `-7.2467` edge `1.2276` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9104` n `52` status `ready` deltaP `50.0` edge `0.4092` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9104` n `52` status `ready` deltaP `50.0` edge `0.4092` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6113` n `149` status `ready` deltaP `43.2886` edge `0.3982` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8931` n `52` status `ready` deltaP `32.8447` edge `0.0571` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8931` n `52` status `ready` deltaP `32.8447` edge `0.0571` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7928` n `149` status `ready` deltaP `29.347` edge `0.0789` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.6141` n `69` status `ready` deltaP `16.4413` edge `0.4406` maxDD `-12.8718`
- `risk_on_high->fx_24h` score `1.2899` n `52` status `ready` deltaP `21.5144` edge `-0.0317` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.2899` n `52` status `ready` deltaP `21.5144` edge `-0.0317` maxDD `-0.0054`
- `market_context_high->commodity_1h` score `1.2032` n `149` status `ready` deltaP `16.9594` edge `0.0249` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1551` n `149` status `ready` deltaP `18.7395` edge `-0.0071` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5799` n `52` status `ready` deltaP `10.0415` edge `0.0166` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5799` n `52` status `ready` deltaP `10.0415` edge `0.0166` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4183` n `69` status `ready` deltaP `10.262` edge `0.0689` maxDD `-3.3619`
- `news_risk_high->fx_4h` score `0.1948` n `69` status `ready` deltaP `6.831` edge `0.0241` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.1888` n `80` status `ready` deltaP `9.2964` edge `0.0144` maxDD `-1.8403`
- `market_context_high->fx_4h` score `0.02` n `149` status `ready` deltaP `7.5994` edge `-0.0005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
