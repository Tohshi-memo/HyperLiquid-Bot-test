# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T03:52:23.672152+00:00`
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

- `news_risk_high->unknown_24h` score `51.9862` n `51` status `ready` deltaP `17.1875` edge `4.2176` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3983` n `51` status `ready` deltaP `40.237` edge `1.0247` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9653` n `51` status `ready` deltaP `23.4965` edge `0.9284` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8336` n `51` status `ready` deltaP `48.9481` edge `0.175` maxDD `-0.2147`
- `risk_on_high->unknown_1h` score `5.0041` n `30` status `ready` deltaP `-13.4332` edge `0.776` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `5.0041` n `30` status `ready` deltaP `-13.4332` edge `0.776` maxDD `-1.5916`
- `news_risk_high->equity_4h` score `3.2323` n `51` status `ready` deltaP `24.9462` edge `0.1801` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.1981` n `51` status `ready` deltaP `37.6255` edge `0.0291` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.9143` n `51` status `ready` deltaP `15.5864` edge `0.1694` maxDD `-0.7693`
- `market_context_high->unknown_4h` score `2.158` n `145` status `ready` deltaP `21.3194` edge `0.0514` maxDD `-0.0956`
- `risk_on_high->metal_4h` score `2.0911` n `30` status `ready` deltaP `28.2826` edge `-0.0055` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.0911` n `30` status `ready` deltaP `28.2826` edge `-0.0055` maxDD `-0.0367`
- `news_risk_high->crypto_alt_24h` score `2.0799` n `51` status `ready` deltaP `26.3889` edge `-0.0026` maxDD `0.0`
- `news_risk_high->metal_24h` score `2.034` n `51` status `ready` deltaP `36.7545` edge `-0.0713` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `1.6787` n `157` status `ready` deltaP `10.3036` edge `0.1161` maxDD `-1.5916`
- `risk_on_high->equity_4h` score `1.5182` n `30` status `ready` deltaP `-4.8577` edge `0.2019` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.5182` n `30` status `ready` deltaP `-4.8577` edge `0.2019` maxDD `-0.773`
- `news_risk_high->fx_1h` score `1.2685` n `51` status `ready` deltaP `17.2948` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8735` n `51` status `ready` deltaP `17.4445` edge `0.0321` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.7819` n `51` status `ready` deltaP `12.3296` edge `0.0227` maxDD `-0.1788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
