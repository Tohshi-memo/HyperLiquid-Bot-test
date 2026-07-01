# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T11:37:29.103700+00:00`
- Price records: `672`
- Market context records: `5347`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->unknown_24h` score `16.4858` n `158` status `ready` deltaP `20.6707` edge `1.245` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.9054` n `158` status `ready` deltaP `22.431` edge `0.7875` maxDD `-28.9274`
- `market_context_high->equity_24h` score `4.667` n `158` status `ready` deltaP `18.0599` edge `0.8314` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9035` n `194` status `ready` deltaP `13.3361` edge `0.3823` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.6861` n `194` status `ready` deltaP `10.9693` edge `0.3148` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.8496` n `194` status `ready` deltaP `10.2448` edge `0.2497` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8277` n `158` status `ready` deltaP `25.0813` edge `0.1024` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.4835` n `194` status `ready` deltaP `7.8632` edge `0.0844` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1609` n `158` status `ready` deltaP `9.6365` edge `0.0387` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.115` n `194` status `ready` deltaP `4.7904` edge `0.1022` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0926` n `194` status `ready` deltaP `2.2455` edge `0.0889` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.067` n `194` status `ready` deltaP `6.5174` edge `0.0125` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3797` n `194` status `ready` deltaP `0.1158` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3857` n `194` status `ready` deltaP `6.0692` edge `0.026` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4542` n `194` status `ready` deltaP `0.8982` edge `0.0033` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6929` n `194` status `ready` deltaP `1.6784` edge `0.0029` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2821` n `194` status `ready` deltaP `7.7555` edge `-0.0403` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4682` n `194` status `ready` deltaP `-3.6252` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.5771` n `194` status `ready` deltaP `-7.0719` edge `-0.0308` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8286` n `194` status `ready` deltaP `-7.1662` edge `-0.0429` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
