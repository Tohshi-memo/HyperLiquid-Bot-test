# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T00:37:29.453760+00:00`
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

- `market_context_high->crypto_major_24h` score `10.5089` n `78` status `ready` deltaP `27.5046` edge `0.706` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.0779` n `65` status `ready` deltaP `31.5174` edge `0.5667` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `5.6437` n `78` status `ready` deltaP `25.8261` edge `0.3601` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.5037` n `65` status `ready` deltaP `19.0578` edge `0.466` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3401` n `65` status `ready` deltaP `9.6538` edge `0.224` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2376` n `65` status `ready` deltaP `22.6804` edge `0.1186` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5755` n `65` status `ready` deltaP `28.7445` edge `0.0492` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4462` n `65` status `ready` deltaP `9.2676` edge `0.1776` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.986` n `65` status `ready` deltaP `24.719` edge `0.0157` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9685` n `117` status `ready` deltaP `11.0046` edge `0.1871` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.9595` n `65` status `ready` deltaP `16.8155` edge `0.1122` maxDD `-2.881`
- `news_risk_high->metal_4h` score `1.7363` n `65` status `ready` deltaP `16.4952` edge `0.0763` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4744` n `117` status `ready` deltaP `25.8801` edge `0.026` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2858` n `117` status `ready` deltaP `17.0473` edge `0.0635` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1925` n `65` status `ready` deltaP `3.6711` edge `0.1268` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9959` n `117` status `ready` deltaP `15.6866` edge `0.0068` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7581` n `78` status `ready` deltaP `24.7026` edge `0.07` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.7573` n `117` status `ready` deltaP `12.3548` edge `0.0204` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.7392` n `78` status `ready` deltaP `13.2435` edge `-0.0206` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.2606` n `65` status `ready` deltaP `25.4005` edge `0.0672` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
