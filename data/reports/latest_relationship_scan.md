# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T11:52:27.290192+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8366`

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

- `market_context_high->unknown_4h` score `39.912` n `149` status `ready` deltaP `-0.311` edge `3.3514` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7907` n `52` status `ready` deltaP `-7.5516` edge `1.2221` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7907` n `52` status `ready` deltaP `-7.5516` edge `1.2221` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9046` n `52` status `ready` deltaP `50.3472` edge `0.4064` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9046` n `52` status `ready` deltaP `50.3472` edge `0.4064` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6054` n `149` status `ready` deltaP `43.6358` edge `0.3954` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1297` n `91` status `ready` deltaP `20.5207` edge `0.4795` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8231` n `52` status `ready` deltaP `32.5399` edge `0.0533` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8231` n `52` status `ready` deltaP `32.5399` edge `0.0533` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7228` n `149` status `ready` deltaP `29.0422` edge `0.0751` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.1181` n `149` status `ready` deltaP `16.2109` edge `0.0228` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.9932` n `91` status `ready` deltaP `13.9842` edge `0.1178` maxDD `-3.3619`
- `risk_on_high->fx_24h` score `0.8361` n `52` status `ready` deltaP `17.5213` edge `-0.0429` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.8361` n `52` status `ready` deltaP `17.5213` edge `-0.0429` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.7012` n `149` status `ready` deltaP `14.7464` edge `-0.0183` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4948` n `52` status `ready` deltaP `9.293` edge `0.0145` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4948` n `52` status `ready` deltaP `9.293` edge `0.0145` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.4073` n `91` status `ready` deltaP `10.5418` edge `0.0266` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.278` n `95` status `ready` deltaP `9.8408` edge `0.0222` maxDD `-1.8403`
- `news_risk_high->crypto_major_4h` score `0.258` n `91` status `ready` deltaP `12.1231` edge `0.2769` maxDD `-19.972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
