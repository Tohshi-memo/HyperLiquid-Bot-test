# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T01:37:27.244394+00:00`
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

- `news_risk_high->unknown_24h` score `53.5282` n `44` status `ready` deltaP `17.1875` edge `4.3461` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.1283` n `44` status `ready` deltaP `52.3674` edge `1.1931` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0817` n `51` status `ready` deltaP `23.4965` edge `0.9381` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8787` n `44` status `ready` deltaP `58.3017` edge `0.193` maxDD `-0.0095`
- `risk_on_high->unknown_1h` score `3.8522` n `37` status `ready` deltaP `-10.0097` edge `0.6055` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8522` n `37` status `ready` deltaP `-10.0097` edge `0.6055` maxDD `-1.5916`
- `news_risk_high->crypto_alt_24h` score `3.8429` n `44` status `ready` deltaP `27.9514` edge `0.1339` maxDD `0.0`
- `news_risk_high->fx_4h` score `3.0873` n `51` status `ready` deltaP `36.406` edge `0.028` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `3.0593` n `37` status `ready` deltaP `3.8605` edge `0.2722` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `3.0593` n `37` status `ready` deltaP `3.8605` edge `0.2722` maxDD `-0.773`
- `news_risk_high->unknown_1h` score `2.9419` n `51` status `ready` deltaP `15.5864` edge `0.1717` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `2.7973` n `51` status `ready` deltaP `23.5743` edge `0.153` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.3527` n `37` status `ready` deltaP `30.6526` edge `0.0005` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3527` n `37` status `ready` deltaP `30.6526` edge `0.0005` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.1405` n `44` status `ready` deltaP `37.8315` edge `-0.0696` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `1.7476` n `145` status `ready` deltaP `21.3194` edge `0.0172` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.5863` n `157` status `ready` deltaP `10.3036` edge `0.1084` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.241` n `51` status `ready` deltaP `16.9954` edge `0.0071` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.1151` n `37` status `ready` deltaP `14.2963` edge `0.0456` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.1151` n `37` status `ready` deltaP `14.2963` edge `0.0456` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
