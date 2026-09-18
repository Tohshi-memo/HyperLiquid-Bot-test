# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T08:52:29.785260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8314`

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

- `market_context_high->unknown_4h` score `39.803` n `149` status `ready` deltaP `-0.1586` edge `3.3413` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.6817` n `52` status `ready` deltaP `-7.3992` edge `1.212` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.6817` n `52` status `ready` deltaP `-7.3992` edge `1.212` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8756` n `52` status `ready` deltaP `50.0` edge `0.4063` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8756` n `52` status `ready` deltaP `50.0` edge `0.4063` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5765` n `149` status `ready` deltaP `43.2886` edge `0.3953` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8559` n `52` status `ready` deltaP `32.8447` edge `0.054` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8559` n `52` status `ready` deltaP `32.8447` edge `0.054` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7556` n `149` status `ready` deltaP `29.347` edge `0.0758` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.7021` n `79` status `ready` deltaP `18.4335` edge `0.4386` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.1744` n `149` status `ready` deltaP `16.66` edge `0.0245` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `1.1729` n `79` status `ready` deltaP `14.5434` edge `0.1371` maxDD `-3.3619`
- `risk_on_high->fx_24h` score `1.0712` n `52` status `ready` deltaP `19.6047` edge `-0.0372` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.0712` n `52` status `ready` deltaP `19.6047` edge `-0.0372` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.9363` n `149` status `ready` deltaP `16.8298` edge `-0.0126` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5512` n `52` status `ready` deltaP `9.7421` edge `0.0162` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5512` n `52` status `ready` deltaP `9.7421` edge `0.0162` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.4384` n `91` status `ready` deltaP `12.0863` edge `0.0278` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2297` n `79` status `ready` deltaP `7.6972` edge `0.0228` maxDD `-0.2398`
- `news_risk_high->index_1h` score `0.0445` n `91` status `ready` deltaP `5.0948` edge `0.0013` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
