# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T01:54:18.519107+00:00`
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

- `news_risk_high->unknown_24h` score `53.3566` n `45` status `ready` deltaP `17.1875` edge `4.3318` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.7742` n `45` status `ready` deltaP `50.5208` edge `1.1759` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0709` n `51` status `ready` deltaP `23.4965` edge `0.9372` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8676` n `45` status `ready` deltaP `58.4028` edge `0.1914` maxDD `-0.0095`
- `risk_on_high->unknown_1h` score `3.8335` n `37` status `ready` deltaP `-10.1594` edge `0.6041` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8335` n `37` status `ready` deltaP `-10.1594` edge `0.6041` maxDD `-1.5916`
- `news_risk_high->crypto_alt_24h` score `3.4594` n `45` status `ready` deltaP `27.7778` edge `0.1031` maxDD `0.0`
- `news_risk_high->fx_4h` score `3.1007` n `51` status `ready` deltaP `36.5585` edge `0.0281` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `3.0991` n `37` status `ready` deltaP `4.0129` edge `0.2745` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `3.0991` n `37` status `ready` deltaP `4.0129` edge `0.2745` maxDD `-0.773`
- `news_risk_high->unknown_1h` score `2.9131` n `51` status `ready` deltaP `15.4367` edge `0.1703` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `2.8371` n `51` status `ready` deltaP `23.7267` edge `0.1553` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.3661` n `37` status `ready` deltaP `30.8051` edge `0.0006` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3661` n `37` status `ready` deltaP `30.8051` edge `0.0006` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.1278` n `45` status `ready` deltaP `37.882` edge `-0.071` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `1.786` n `145` status `ready` deltaP `21.3194` edge `0.0204` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.6829` n `157` status `ready` deltaP `10.7908` edge `0.1132` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.241` n `51` status `ready` deltaP `16.9954` edge `0.0071` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.1309` n `37` status `ready` deltaP `14.4488` edge `0.0459` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.1309` n `37` status `ready` deltaP `14.4488` edge `0.0459` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
