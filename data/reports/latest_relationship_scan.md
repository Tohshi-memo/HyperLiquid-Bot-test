# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T11:22:26.214393+00:00`
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

- `news_risk_high->unknown_4h` score `14.602` n `51` status `ready` deltaP `26.2404` edge `1.0465` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9618` n `33` status `ready` deltaP `-8.4785` edge `0.7375` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9618` n `33` status `ready` deltaP `-8.4785` edge `0.7375` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.6712` n `51` status `ready` deltaP `19.3289` edge `0.2075` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8402` n `51` status `ready` deltaP `33.6621` edge `0.0257` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7535` n `51` status `ready` deltaP `23.2694` edge `0.1516` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.3692` n `33` status `ready` deltaP `31.3239` edge `-0.0026` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3692` n `33` status `ready` deltaP `31.3239` edge `-0.0026` maxDD `-0.0367`
- `market_context_high->crypto_alt_4h` score `1.7369` n `128` status `ready` deltaP `9.4131` edge `0.2288` maxDD `-7.0785`
- `risk_on_high->equity_4h` score `1.627` n `33` status `ready` deltaP `-1.686` edge `0.2629` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.627` n `33` status `ready` deltaP `-1.686` edge `0.2629` maxDD `-0.7794`
- `market_context_high->unknown_1h` score `1.4021` n `128` status `ready` deltaP `7.2885` edge `0.1131` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1871` n `51` status `ready` deltaP `16.3966` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.1577` n `128` status `ready` deltaP `21.9512` edge `-0.0327` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `0.8982` n `108` status `ready` deltaP `1.2731` edge `0.1137` maxDD `-0.7869`
- `news_risk_high->equity_1h` score `0.7582` n `51` status `ready` deltaP `16.8457` edge `0.0214` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.6532` n `51` status `ready` deltaP `11.1101` edge `0.0201` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.6327` n `33` status `ready` deltaP `15.1238` edge `0.0035` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6327` n `33` status `ready` deltaP `15.1238` edge `0.0035` maxDD `-0.1905`
- `risk_on_high->index_4h` score `0.4755` n `33` status `ready` deltaP `9.8624` edge `0.0432` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
