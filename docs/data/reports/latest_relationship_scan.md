# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T17:37:27.180163+00:00`
- Price records: `672`
- Market context records: `2163`
- Flow alert records: `8122`
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

- `market_context_high->crypto_alt_4h` score `13.2093` n `139` status `ready` deltaP `37.1117` edge `0.947` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7171` n `139` status `ready` deltaP `41.3427` edge `0.7538` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7168` n `139` status `ready` deltaP `23.5524` edge `0.3943` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.9904` n `43` status `ready` deltaP `32.4624` edge `0.3623` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.9561` n `139` status `ready` deltaP `24.6787` edge `0.2746` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2566` n `139` status `ready` deltaP `17.6841` edge `0.2012` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.1817` n `139` status `ready` deltaP `16.3368` edge `0.2426` maxDD `-4.9097`
- `market_context_high->index_24h` score `3.109` n `139` status `ready` deltaP `12.3938` edge `0.2993` maxDD `-4.1604`
- `market_context_high->index_4h` score `2.9798` n `139` status `ready` deltaP `23.3067` edge `0.1613` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.669` n `139` status `ready` deltaP `27.5492` edge `0.5708` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.2228` n `139` status `ready` deltaP `20.1277` edge `1.0085` maxDD `-62.2831`
- `market_context_high->equity_24h` score `2.1699` n `139` status `ready` deltaP `24.1007` edge `0.51` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.0369` n `43` status `ready` deltaP `26.0599` edge `0.0144` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.9641` n `139` status `ready` deltaP `19.0834` edge `0.1752` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.4913` n `43` status `ready` deltaP `15.8395` edge `0.091` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.4471` n `43` status `ready` deltaP `-2.0739` edge `0.3201` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3039` n `43` status `ready` deltaP `21.3445` edge `0.0133` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8344` n `43` status `ready` deltaP `10.9142` edge `0.1022` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5505` n `139` status `ready` deltaP `10.4112` edge `0.0553` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5395` n `139` status `ready` deltaP `9.2922` edge `0.05` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
