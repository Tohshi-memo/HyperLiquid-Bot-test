# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T22:52:28.027951+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12499`

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

- `market_context_high->unknown_24h` score `14387.503` n `64` status `ready` deltaP `12.3264` edge `1198.8816` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.3936` n `82` status `ready` deltaP `-5.4002` edge `31.9443` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.1148` n `81` status `ready` deltaP `32.8896` edge `1.3391` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0201` n `81` status `ready` deltaP `39.5447` edge `1.3851` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `11.7466` n `64` status `ready` deltaP `25.1736` edge `0.8938` maxDD `-3.9523`
- `market_context_high->equity_24h` score `10.0008` n `64` status `ready` deltaP `44.4444` edge `0.5371` maxDD `0.0`
- `news_risk_high->index_24h` score `6.1375` n `81` status `ready` deltaP `42.3033` edge `0.2471` maxDD `-0.0797`
- `news_risk_high->equity_24h` score `6.1357` n `81` status `ready` deltaP `14.8148` edge `0.5831` maxDD `-6.3112`
- `news_risk_high->metal_24h` score `5.2429` n `81` status `ready` deltaP `30.5556` edge `0.2786` maxDD `-0.6317`
- `market_context_high->commodity_24h` score `3.7613` n `64` status `ready` deltaP `39.0625` edge `0.0576` maxDD `-0.0328`
- `market_context_high->index_24h` score `3.312` n `64` status `ready` deltaP `35.2431` edge `0.0804` maxDD `-0.1483`
- `risk_on_high->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `risk_on_high->crypto_alt_4h` score `0.089` n `47` status `ready` deltaP `6.3862` edge `0.123` maxDD `-6.333`
- `risk_on_and_context->crypto_alt_4h` score `0.089` n `47` status `ready` deltaP `6.3862` edge `0.123` maxDD `-6.333`
- `news_risk_high->index_4h` score `0.0834` n `82` status `ready` deltaP `6.8597` edge `0.0278` maxDD `-0.6935`
- `risk_on_high->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `market_context_high->metal_24h` score `-0.0216` n `64` status `ready` deltaP `5.9028` edge `0.1038` maxDD `-3.3403`
- `risk_on_high->fx_1h` score `-0.0928` n `53` status `ready` deltaP `1.6015` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
