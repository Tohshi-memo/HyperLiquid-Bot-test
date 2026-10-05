# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T15:37:35.961367+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8072`

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

- `market_context_high->crypto_major_24h` score `10.9085` n `79` status `ready` deltaP `29.7094` edge `0.7246` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5902` n `65` status `ready` deltaP `33.4662` edge `0.5964` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.9806` n `65` status `ready` deltaP `20.5488` edge `0.4958` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4865` n `79` status `ready` deltaP `25.8109` edge `0.3471` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.4506` n `65` status `ready` deltaP `24.6528` edge `0.1232` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1553` n `65` status `ready` deltaP `9.8184` edge `0.2075` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8783` n `65` status `ready` deltaP `31.9137` edge `0.0533` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5253` n `65` status `ready` deltaP `9.8664` edge `0.1802` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4388` n `65` status `ready` deltaP `20.272` edge `0.1291` maxDD `-2.881`
- `market_context_high->crypto_major_4h` score `2.3889` n `118` status `ready` deltaP `12.3449` edge `0.2132` maxDD `-4.047`
- `news_risk_high->index_1h` score `1.9979` n `65` status `ready` deltaP `24.8687` edge `0.0157` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8754` n `65` status `ready` deltaP `17.8588` edge `0.0788` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5574` n `118` status `ready` deltaP `26.8577` edge `0.0264` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1841` n `65` status `ready` deltaP `3.6711` edge `0.1261` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0135` n `118` status `ready` deltaP `15.9063` edge `0.0068` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9081` n `118` status `ready` deltaP `13.9314` edge `0.0528` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.8588` n `79` status `ready` deltaP `26.1955` edge `0.0738` maxDD `-5.7335`
- `market_context_high->equity_24h` score `0.665` n `79` status `ready` deltaP `13.4406` edge `-0.0281` maxDD `-0.1536`
- `market_context_high->commodity_1h` score `0.5503` n `118` status `ready` deltaP `10.8216` edge `0.0158` maxDD `-0.7005`
- `news_risk_high->commodity_24h` score `0.3857` n `65` status `ready` deltaP `24.9119` edge `0.0865` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
