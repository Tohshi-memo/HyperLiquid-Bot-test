# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T17:22:21.748403+00:00`
- Price records: `672`
- Market context records: `2162`
- Flow alert records: `8119`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `13.292` n `140` status `ready` deltaP `37.2299` edge `0.9531` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.728` n `140` status `ready` deltaP `41.4198` edge `0.7542` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7481` n `140` status `ready` deltaP `23.7631` edge `0.3955` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.0767` n `140` status `ready` deltaP `25.0915` edge `0.2819` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0052` n `43` status `ready` deltaP `32.4624` edge `0.3642` maxDD `-3.0367`
- `market_context_high->crypto_major_1h` score `3.2271` n `140` status `ready` deltaP `17.361` edge `0.2009` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.219` n `140` status `ready` deltaP `16.5783` edge `0.2441` maxDD `-4.9097`
- `market_context_high->index_24h` score `3.1755` n `140` status `ready` deltaP `12.5943` edge `0.3035` maxDD `-4.1604`
- `market_context_high->index_4h` score `3.0316` n `140` status `ready` deltaP `23.4146` edge `0.1649` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.6351` n `140` status `ready` deltaP `27.5297` edge `0.5681` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.3198` n `140` status `ready` deltaP `24.4593` edge `0.5201` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `2.1567` n `140` status `ready` deltaP `19.7371` edge `1.0035` maxDD `-62.3533`
- `market_context_high->metal_4h` score `2.089` n `140` status `ready` deltaP `19.3249` edge `0.184` maxDD `-4.7664`
- `news_risk_high->fx_4h` score `2.0223` n `43` status `ready` deltaP `25.9075` edge `0.0142` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.4997` n `43` status `ready` deltaP `15.8395` edge `0.0917` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.4926` n `43` status `ready` deltaP `-1.769` edge `0.3239` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.1179` n `43` status `ready` deltaP `19.1686` edge `0.0123` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8204` n `43` status `ready` deltaP `10.7645` edge `0.1014` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5925` n `140` status `ready` deltaP `10.9367` edge `0.0553` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5713` n `140` status `ready` deltaP `9.5851` edge `0.0507` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
