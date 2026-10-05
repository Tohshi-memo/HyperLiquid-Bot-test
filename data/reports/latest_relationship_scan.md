# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T11:52:32.804547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8318`

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

- `market_context_high->crypto_major_24h` score `10.9316` n `81` status `ready` deltaP `29.8032` edge `0.7259` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3441` n `65` status `ready` deltaP `32.3992` edge `0.583` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.3066` n `81` status `ready` deltaP `25.3666` edge `0.4184` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8042` n `65` status `ready` deltaP `19.6341` edge `0.4872` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5233` n `112` status `ready` deltaP `15.9844` edge `0.2668` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.4422` n `65` status `ready` deltaP `24.6528` edge `0.1225` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.083` n `65` status `ready` deltaP `10.3393` edge `0.198` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9474` n `65` status `ready` deltaP `32.5235` edge `0.055` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5061` n `65` status `ready` deltaP `9.8664` edge `0.1786` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4956` n `65` status `ready` deltaP `20.5769` edge `0.1318` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0866` n `65` status `ready` deltaP `25.7669` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.778` n `65` status `ready` deltaP `16.7918` edge `0.0778` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6329` n `112` status `ready` deltaP `27.5915` edge `0.0278` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1949` n `65` status `ready` deltaP `3.6711` edge `0.127` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9784` n `122` status `ready` deltaP `15.5885` edge `0.006` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9205` n `112` status `ready` deltaP `14.4817` edge `0.0542` maxDD `-1.9231`
- `market_context_high->equity_24h` score `0.8263` n `81` status `ready` deltaP `11.5548` edge `0.0041` maxDD `-0.3151`
- `market_context_high->crypto_alt_4h` score `0.8054` n `112` status `ready` deltaP `3.027` edge `0.2193` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.6243` n `81` status `ready` deltaP `24.1705` edge `0.062` maxDD `-6.1146`
- `news_risk_high->commodity_24h` score `0.4809` n `65` status `ready` deltaP `24.9119` edge `0.0987` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
