# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T03:22:20.473376+00:00`
- Price records: `672`
- Market context records: `2103`
- Flow alert records: `7948`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.6692` n `178` status `ready` deltaP `31.1952` edge `0.7956` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4803` n `178` status `ready` deltaP `37.6885` edge `0.6751` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7677` n `178` status `ready` deltaP `23.6041` edge `0.3982` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1331` n `178` status `ready` deltaP `22.6758` edge `0.3027` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5258` n `178` status `ready` deltaP `18.9521` edge `0.1525` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.4061` n `177` status `ready` deltaP `23.0622` edge `0.5788` maxDD `-35.8966`
- `market_context_high->index_24h` score `2.3123` n `177` status `ready` deltaP `11.7491` edge `0.2372` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.1581` n `178` status `ready` deltaP `15.5789` edge `0.1746` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.9695` n `178` status `ready` deltaP `12.5849` edge `0.1916` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.5746` n `177` status `ready` deltaP `22.9596` edge `0.468` maxDD `-33.1875`
- `market_context_high->metal_4h` score `0.9975` n `178` status `ready` deltaP `15.6567` edge `0.1792` maxDD `-9.7032`
- `market_context_high->equity_1h` score `0.8209` n `178` status `ready` deltaP `10.9416` edge `0.0743` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2005` n `178` status `ready` deltaP `5.3203` edge `0.0532` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1612` n `178` status `ready` deltaP `6.2959` edge `0.0305` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0862` n `177` status `ready` deltaP `20.9352` edge `0.7262` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0746` n `177` status `ready` deltaP `14.9014` edge `0.0304` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.2081` n `178` status `ready` deltaP `6.8156` edge `0.0393` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.867` n `178` status `ready` deltaP `-1.5727` edge `0.001` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-0.9694` n `177` status `ready` deltaP `10.1304` edge `0.2418` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.0491` n `178` status `ready` deltaP `-6.5634` edge `-0.0026` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
