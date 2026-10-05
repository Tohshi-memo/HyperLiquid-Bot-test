# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T14:37:28.139710+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8272`

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

- `market_context_high->crypto_major_24h` score `10.9304` n `82` status `ready` deltaP `29.8484` edge `0.7255` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.413` n `65` status `ready` deltaP `32.8565` edge `0.5857` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.2581` n `82` status `ready` deltaP `25.6606` edge `0.4124` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7674` n `65` status `ready` deltaP `19.939` edge `0.4821` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4422` n `65` status `ready` deltaP `24.6528` edge `0.1225` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0425` n `65` status `ready` deltaP `9.8184` edge `0.1981` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8771` n `65` status `ready` deltaP `31.9137` edge `0.0532` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.8144` n `119` status `ready` deltaP `13.658` edge `0.2399` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.3957` n `65` status `ready` deltaP `9.4173` edge `0.1724` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3944` n `65` status `ready` deltaP `20.272` edge `0.1254` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9967` n `65` status `ready` deltaP `24.8687` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.811` n `65` status `ready` deltaP `17.2491` edge `0.0775` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4966` n `119` status `ready` deltaP `26.1427` edge `0.0261` maxDD `-0.3868`
- `market_context_high->equity_24h` score `1.0756` n `82` status `ready` deltaP `13.5332` edge `0.0055` maxDD `-0.1536`
- `news_risk_high->crypto_alt_1h` score `1.0653` n `65` status `ready` deltaP `3.3717` edge `0.1182` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9652` n `121` status `ready` deltaP `15.3486` edge `0.0065` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.8604` n `82` status `ready` deltaP `26.2957` edge `0.0741` maxDD `-5.7943`
- `market_context_high->commodity_4h` score `0.6648` n `119` status `ready` deltaP `12.181` edge `0.0442` maxDD `-1.6002`
- `news_risk_high->commodity_24h` score `0.4216` n `65` status `ready` deltaP `24.9119` edge `0.0911` maxDD `-10.9169`
- `market_context_high->crypto_alt_4h` score `0.3431` n `119` status `ready` deltaP `-0.3971` edge `0.2036` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
