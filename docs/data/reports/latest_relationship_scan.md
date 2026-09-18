# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T05:52:26.519847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8646`

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

- `market_context_high->unknown_4h` score `40.078` n `149` status `ready` deltaP `-0.0061` edge `3.3632` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9567` n `52` status `ready` deltaP `-7.2467` edge `1.2339` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9567` n `52` status `ready` deltaP `-7.2467` edge `1.2339` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9188` n `52` status `ready` deltaP `50.0` edge `0.4099` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9188` n `52` status `ready` deltaP `50.0` edge `0.4099` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6197` n `149` status `ready` deltaP `43.2886` edge `0.3989` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8991` n `52` status `ready` deltaP `32.8447` edge `0.0576` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8991` n `52` status `ready` deltaP `32.8447` edge `0.0576` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7988` n `149` status `ready` deltaP `29.347` edge `0.0794` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.3662` n `69` status `ready` deltaP `15.1445` edge `0.4228` maxDD `-12.9654`
- `risk_on_high->fx_24h` score `1.3086` n `52` status `ready` deltaP `21.688` edge `-0.0313` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.3086` n `52` status `ready` deltaP `21.688` edge `-0.0313` maxDD `-0.0054`
- `market_context_high->commodity_1h` score `1.2056` n `149` status `ready` deltaP `16.9594` edge `0.0251` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1738` n `149` status `ready` deltaP `18.9131` edge `-0.0067` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5823` n `52` status `ready` deltaP `10.0415` edge `0.0168` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5823` n `52` status `ready` deltaP `10.0415` edge `0.0168` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4167` n `69` status `ready` deltaP `10.262` edge `0.0687` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.2153` n `80` status `ready` deltaP `9.2964` edge `0.0178` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.114` n `69` status `ready` deltaP `5.5342` edge `0.0224` maxDD `-0.2415`
- `market_context_high->fx_4h` score `0.0287` n `149` status `ready` deltaP `7.7518` edge `-0.0004` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
