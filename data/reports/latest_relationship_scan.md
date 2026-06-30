# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T15:37:48.845405+00:00`
- Price records: `672`
- Market context records: `5261`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.8463` n `147` status `ready` deltaP `30.2367` edge `2.0446` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.4667` n `147` status `ready` deltaP `28.4297` edge `1.0431` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.0777` n `158` status `ready` deltaP `14.2193` edge `0.4091` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8493` n `158` status `ready` deltaP `14.418` edge `0.4539` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.4056` n `147` status `ready` deltaP `19.5118` edge `0.7166` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.9463` n `158` status `ready` deltaP `17.1311` edge `0.1502` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.6095` n `158` status `ready` deltaP `8.5887` edge `0.1574` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5245` n `147` status `ready` deltaP `12.6666` edge `0.0488` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4724` n `169` status `ready` deltaP `4.3236` edge `0.1067` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.24` n `147` status `ready` deltaP `21.0247` edge `0.0541` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2089` n `169` status `ready` deltaP `5.243` edge `0.107` maxDD `-6.9639`
- `market_context_high->crypto_alt_24h` score `0.0878` n `147` status `ready` deltaP `15.4018` edge `0.5381` maxDD `-38.6949`
- `market_context_high->equity_1h` score `-0.0407` n `169` status `ready` deltaP `5.7356` edge `0.0549` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0795` n `169` status `ready` deltaP `4.8515` edge `0.0114` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1598` n `169` status `ready` deltaP `4.6159` edge `0.0151` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2387` n `169` status `ready` deltaP `2.0356` edge `0.0006` maxDD `-0.5823`
- `market_context_high->unknown_1h` score `-0.6728` n `169` status `ready` deltaP `7.1972` edge `-0.0399` maxDD `-2.7986`
- `market_context_high->index_4h` score `-0.7182` n `158` status `ready` deltaP `4.8279` edge `0.0197` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7975` n `158` status `ready` deltaP `0.0425` edge `0.0004` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.2818` n `169` status `ready` deltaP `-2.3775` edge `-0.006` maxDD `-2.7973`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
