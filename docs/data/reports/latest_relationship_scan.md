# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T02:52:29.467363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `52.6438` n `49` status `ready` deltaP `17.1875` edge `4.2724` maxDD `0.0`
- `news_risk_high->equity_24h` score `15.744` n `49` status `ready` deltaP `43.4383` edge `1.0826` maxDD `-2.8148`
- `news_risk_high->unknown_4h` score `13.0157` n `51` status `ready` deltaP `23.4965` edge `0.9326` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.2702` n `49` status `ready` deltaP `52.4695` edge `0.182` maxDD `-0.0755`
- `risk_on_high->unknown_1h` score `4.0742` n `34` status `ready` deltaP `-13.8253` edge `0.6594` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.0742` n `34` status `ready` deltaP `-13.8253` edge `0.6594` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.1567` n `51` status `ready` deltaP `37.1682` edge `0.0287` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.0191` n `51` status `ready` deltaP `24.3365` edge `0.1664` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `2.9119` n `51` status `ready` deltaP `15.5864` edge `0.1692` maxDD `-0.7693`
- `news_risk_high->crypto_alt_24h` score `2.5543` n `49` status `ready` deltaP `27.0833` edge `0.0323` maxDD `0.0`
- `risk_on_high->equity_4h` score `2.4058` n `34` status `ready` deltaP `0.8071` edge `0.2381` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.4058` n `34` status `ready` deltaP `0.8071` edge `0.2381` maxDD `-0.773`
- `risk_on_high->metal_4h` score `2.279` n `34` status `ready` deltaP `29.8512` edge `-0.0003` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.279` n `34` status `ready` deltaP `29.8512` edge `-0.0003` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.1047` n `49` status `ready` deltaP `37.3689` edge `-0.0695` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `1.984` n `145` status `ready` deltaP `21.3194` edge `0.0369` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.6883` n `157` status `ready` deltaP `10.3036` edge `0.1169` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2937` n `51` status `ready` deltaP `17.5942` edge `0.0075` maxDD `-0.0257`
- `risk_on_high->index_4h` score `0.837` n `34` status `ready` deltaP `11.7198` edge `0.0396` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.837` n `34` status `ready` deltaP `11.7198` edge `0.0396` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
