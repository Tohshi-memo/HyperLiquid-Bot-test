# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T08:22:39.243707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8300`

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

- `market_context_high->unknown_1h` score `78.6596` n `120` status `ready` deltaP `0.2296` edge `6.5949` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `53.3157` n `108` status `ready` deltaP `1.0276` edge `4.4703` maxDD `-0.7342`
- `market_context_high->crypto_major_24h` score `10.795` n `77` status `ready` deltaP `29.6108` edge `0.7158` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3155` n `65` status `ready` deltaP `32.5516` edge `0.5796` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1859` n `77` status `ready` deltaP `24.8535` edge `0.4951` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7924` n `65` status `ready` deltaP `19.7866` edge `0.4852` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3421` n `65` status `ready` deltaP `23.6111` edge `0.1211` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2723` n `65` status `ready` deltaP `12.0754` edge `0.2022` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `3.1992` n `108` status `ready` deltaP `14.318` edge `0.2509` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.483` n `65` status `ready` deltaP `20.1196` edge `0.1338` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.3777` n `65` status `ready` deltaP `9.4173` edge `0.1709` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0207` n `65` status `ready` deltaP `25.0184` edge `0.0166` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9186` n `65` status `ready` deltaP `17.8588` edge `0.0824` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2836` n `108` status `ready` deltaP `23.645` edge `0.025` maxDD `-0.3868`
- `market_context_high->crypto_major_1h` score `1.0383` n `120` status `ready` deltaP `11.5968` edge `0.0981` maxDD `-3.7778`
- `news_risk_high->crypto_alt_1h` score `1.0294` n `65` status `ready` deltaP `2.9226` edge `0.1182` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.5765` n `65` status `ready` deltaP `25.0855` edge `0.1098` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.5013` n `120` status `ready` deltaP `13.2086` edge `0.0046` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.1992` n `77` status `ready` deltaP `5.2422` edge `0.0019` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
