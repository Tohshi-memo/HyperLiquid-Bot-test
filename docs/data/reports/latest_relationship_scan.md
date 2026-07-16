# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T09:22:28.983571+00:00`
- Price records: `672`
- Market context records: `6904`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `0.2786` n `189` status `ready` deltaP `-4.5107` edge `0.4624` maxDD `-14.0627`
- `market_context_high->fx_1h` score `-0.1942` n `224` status `ready` deltaP `3.1357` edge `0.0027` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3587` n `224` status `ready` deltaP `3.2587` edge `0.0248` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4375` n `224` status `ready` deltaP `4.745` edge `0.0223` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.5972` n `224` status `ready` deltaP `-0.5988` edge `-0.0041` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7583` n `224` status `ready` deltaP `14.9173` edge `0.0097` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7752` n `224` status `ready` deltaP `-0.8795` edge `-0.0024` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8401` n `224` status `ready` deltaP `-3.8441` edge `-0.0053` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3262` n `224` status `ready` deltaP `-1.7313` edge `-0.0095` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5798` n `224` status `ready` deltaP `-3.1116` edge `-0.0208` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7536` n `224` status `ready` deltaP `2.0851` edge `-0.0207` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9132` n `224` status `ready` deltaP `5.0088` edge `-0.0207` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1749` n `224` status `ready` deltaP `2.6241` edge `0.002` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.2654` n `189` status `ready` deltaP `0.2155` edge `-0.0034` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.748` n `224` status `ready` deltaP `2.2104` edge `-0.0087` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8439` n `224` status `ready` deltaP `-0.0871` edge `-0.0313` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0193` n `224` status `ready` deltaP `-8.1228` edge `0.0391` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1743` n `189` status `ready` deltaP `-5.7339` edge `-0.006` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1537` n `224` status `ready` deltaP `2.4064` edge `-0.1387` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3653` n `189` status `ready` deltaP `-13.6613` edge `-0.1223` maxDD `-28.3945`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
