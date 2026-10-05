# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T16:37:29.811273+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8128`

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

- `market_context_high->crypto_major_24h` score `11.1186` n `78` status `ready` deltaP `30.5956` edge `0.7362` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.6516` n `65` status `ready` deltaP `33.6187` edge `0.6005` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.095` n `65` status `ready` deltaP `20.8537` edge `0.5033` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5178` n `78` status `ready` deltaP `26.2019` edge `0.3471` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.4331` n `65` status `ready` deltaP `24.4792` edge `0.1229` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2081` n `65` status `ready` deltaP `9.8184` edge `0.2119` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8613` n `65` status `ready` deltaP `31.7613` edge `0.0529` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6248` n `65` status `ready` deltaP `10.4652` edge `0.1845` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5422` n `117` status `ready` deltaP `13.1059` edge `0.2209` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.4254` n `65` status `ready` deltaP `20.1196` edge `0.129` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0015` n `65` status `ready` deltaP `24.8687` edge `0.016` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9105` n `65` status `ready` deltaP `18.1637` edge `0.0797` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6336` n `117` status `ready` deltaP `27.7348` edge `0.0269` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2764` n `65` status `ready` deltaP `4.1202` edge `0.1308` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0701` n `117` status `ready` deltaP `16.5848` edge `0.007` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9944` n `117` status `ready` deltaP `14.6199` edge `0.0554` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.8782` n `78` status `ready` deltaP `26.4423` edge `0.0738` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.6531` n `117` status `ready` deltaP `11.3069` edge `0.0187` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.6072` n `78` status `ready` deltaP `13.4081` edge `-0.0327` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3608` n `65` status `ready` deltaP `24.9119` edge `0.0833` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
