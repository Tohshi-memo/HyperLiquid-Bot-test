# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T17:37:27.156244+00:00`
- Price records: `672`
- Market context records: `5270`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `26.1869` n `150` status `ready` deltaP `29.5695` edge `1.9941` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `9.3283` n `150` status `ready` deltaP `27.0555` edge `0.9574` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.3822` n `165` status `ready` deltaP `16.0901` edge `0.422` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8579` n `165` status `ready` deltaP `14.8706` edge `0.4516` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.5753` n `150` status `ready` deltaP `19.7431` edge `0.7292` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.3162` n `165` status `ready` deltaP `16.0052` edge `0.1052` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.7964` n `165` status `ready` deltaP `8.8996` edge `0.1709` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.547` n `150` status `ready` deltaP `12.9931` edge `0.0485` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4784` n `177` status `ready` deltaP `4.7879` edge `0.1041` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2548` n `177` status `ready` deltaP `5.6379` edge `0.1082` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2429` n `150` status `ready` deltaP `21.0209` edge `0.0545` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0661` n `177` status `ready` deltaP `6.5598` edge `0.0583` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0057` n `177` status `ready` deltaP `5.7292` edge `0.0117` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.288` n `177` status `ready` deltaP `3.5082` edge `0.0118` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.327` n `177` status `ready` deltaP `0.4127` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.6109` n `165` status `ready` deltaP `5.4342` edge `0.0246` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.702` n `165` status `ready` deltaP `1.6084` edge `0.0022` maxDD `-1.567`
- `market_context_high->crypto_alt_24h` score `-1.3261` n `150` status `ready` deltaP `14.3541` edge `0.4647` maxDD `-45.7658`
- `market_context_high->commodity_1h` score `-1.4695` n `177` status `ready` deltaP `-3.5564` edge `-0.0078` maxDD `-3.2759`
- `market_context_high->metal_4h` score `-1.5788` n `165` status `ready` deltaP `-2.0953` edge `0.0119` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
