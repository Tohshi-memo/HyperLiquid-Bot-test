# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T15:22:24.135254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `market_context_high->unknown_1h` score `368.0445` n `50` status `ready` deltaP `11.4731` edge `30.5988` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `296.4648` n `50` status `ready` deltaP `12.1951` edge `24.6241` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.3043` n `50` status `ready` deltaP `29.9792` edge `1.1625` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8135` n `50` status `ready` deltaP `37.6326` edge `0.8752` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `11.0391` n `62` status `ready` deltaP `38.5573` edge `0.6832` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.6191` n `62` status `ready` deltaP `29.6109` edge `0.736` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.6779` n `62` status `ready` deltaP `27.0506` edge `0.5939` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3805` n `50` status `ready` deltaP `17.8476` edge `0.5664` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3457` n `50` status `ready` deltaP `18.0183` edge `0.5376` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6191` n `62` status `ready` deltaP `33.8095` edge `0.1754` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.052` n `62` status `ready` deltaP `27.3801` edge `0.2164` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3369` n `50` status `ready` deltaP `14.9521` edge `0.2447` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1617` n `62` status `ready` deltaP `34.1365` edge `0.0621` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0736` n `50` status `ready` deltaP `34.5183` edge `0.0395` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0326` n `68` status `ready` deltaP `13.9574` edge `0.1952` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9677` n `50` status `ready` deltaP `13.2515` edge `0.204` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3915` n `62` status `ready` deltaP `19.3302` edge `0.112` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0593` n `68` status `ready` deltaP `25.3963` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6816` n `68` status `ready` deltaP `6.305` edge `0.15` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5945` n `50` status `ready` deltaP `22.1377` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
