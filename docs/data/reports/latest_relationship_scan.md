# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T12:52:31.279361+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.4254` n `51` status `ready` deltaP `26.088` edge `1.0328` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.8706` n `33` status `ready` deltaP `-8.7779` edge `0.7278` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.8706` n `33` status `ready` deltaP `-8.7779` edge `0.7278` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.5309` n `51` status `ready` deltaP `19.0295` edge `0.1978` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8926` n `51` status `ready` deltaP `34.2719` edge `0.026` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7283` n `51` status `ready` deltaP `23.2694` edge `0.1495` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.2924` n `33` status `ready` deltaP `30.4093` edge `-0.0029` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2924` n `33` status `ready` deltaP `30.4093` edge `-0.0029` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6106` n `33` status `ready` deltaP `-1.686` edge `0.2608` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6106` n `33` status `ready` deltaP `-1.686` edge `0.2608` maxDD `-0.7794`
- `market_context_high->crypto_alt_4h` score `1.5077` n `128` status `ready` deltaP `9.4131` edge `0.2097` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.2618` n `128` status `ready` deltaP `6.9891` edge `0.1034` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1631` n `51` status `ready` deltaP `16.0972` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `0.9811` n `128` status `ready` deltaP `21.7988` edge `-0.0464` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.7107` n `51` status `ready` deltaP `16.0972` edge `0.0203` maxDD `-0.9204`
- `risk_on_high->fx_4h` score `0.6667` n `33` status `ready` deltaP `15.7336` edge `0.0038` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6667` n `33` status `ready` deltaP `15.7336` edge `0.0038` maxDD `-0.1905`
- `market_context_high->commodity_24h` score `0.5924` n `111` status `ready` deltaP `-1.0276` edge `0.1037` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.5874` n `51` status `ready` deltaP `10.3479` edge `0.0197` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.4328` n `33` status `ready` deltaP `9.1002` edge `0.0428` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
