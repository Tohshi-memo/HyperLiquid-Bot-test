# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T23:22:34.507513+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7928`

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

- `market_context_high->crypto_major_24h` score `10.4658` n `78` status `ready` deltaP `27.161` edge `0.7047` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.1986` n `65` status `ready` deltaP `32.0959` edge `0.5729` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6784` n `65` status `ready` deltaP `19.6369` edge `0.4767` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5309` n `78` status `ready` deltaP `25.8261` edge `0.3507` maxDD `-2.9571`
- `news_risk_high->equity_24h` score `3.2765` n `65` status `ready` deltaP `9.6538` edge `0.2187` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2388` n `65` status `ready` deltaP `22.6804` edge `0.1187` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6168` n `65` status `ready` deltaP `29.1703` edge `0.0498` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3634` n `65` status `ready` deltaP `8.8185` edge `0.1737` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.0892` n `117` status `ready` deltaP `11.5831` edge `0.1933` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0474` n `65` status `ready` deltaP `17.4188` edge `0.1155` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9488` n `65` status `ready` deltaP `24.2699` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7445` n `65` status `ready` deltaP `16.5833` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5161` n `117` status `ready` deltaP `26.3716` edge `0.0262` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2626` n `117` status `ready` deltaP `16.8031` edge `0.0632` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.0594` n `65` status `ready` deltaP `3.0723` edge `0.1197` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0091` n `117` status `ready` deltaP `15.8363` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7837` n `117` status `ready` deltaP `12.6542` edge `0.0206` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7343` n `78` status `ready` deltaP `24.5308` edge `0.0681` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.6756` n `78` status `ready` deltaP `13.2435` edge `-0.0259` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3097` n `65` status `ready` deltaP `25.4005` edge `0.0735` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
