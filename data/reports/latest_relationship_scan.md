# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T11:07:27.573247+00:00`
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

- `news_risk_high->unknown_4h` score `14.6092` n `51` status `ready` deltaP `26.2404` edge `1.0471` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9634` n `33` status `ready` deltaP `-8.4785` edge `0.7377` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9634` n `33` status `ready` deltaP `-8.4785` edge `0.7377` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.6736` n `51` status `ready` deltaP `19.3289` edge `0.2077` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8366` n `51` status `ready` deltaP `33.6621` edge `0.0254` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7717` n `51` status `ready` deltaP `23.4218` edge `0.1521` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.3814` n `33` status `ready` deltaP `31.4764` edge `-0.0026` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3814` n `33` status `ready` deltaP `31.4764` edge `-0.0026` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6388` n `33` status `ready` deltaP `-1.5336` edge `0.2634` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6388` n `33` status `ready` deltaP `-1.5336` edge `0.2634` maxDD `-0.7794`
- `market_context_high->crypto_alt_4h` score `1.5785` n `127` status `ready` deltaP `9.2039` edge `0.217` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.4045` n `128` status `ready` deltaP `7.2885` edge `0.1133` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1871` n `51` status `ready` deltaP `16.3966` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.1465` n `127` status `ready` deltaP `21.902` edge `-0.0333` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `0.9145` n `108` status `ready` deltaP `1.4468` edge `0.1139` maxDD `-0.7869`
- `news_risk_high->equity_1h` score `0.7667` n `51` status `ready` deltaP `16.9954` edge `0.0215` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.6666` n `51` status `ready` deltaP `11.2625` edge `0.0202` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.6303` n `33` status `ready` deltaP `15.1238` edge `0.0032` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6303` n `33` status `ready` deltaP `15.1238` edge `0.0032` maxDD `-0.1905`
- `risk_on_high->index_4h` score `0.4842` n `33` status `ready` deltaP `10.0148` edge `0.0433` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
