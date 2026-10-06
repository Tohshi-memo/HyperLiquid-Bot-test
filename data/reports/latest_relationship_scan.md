# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T01:52:30.677976+00:00`
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

- `market_context_high->crypto_major_24h` score `9.5315` n `81` status `ready` deltaP `23.7241` edge `0.6572` maxDD `-0.6852`
- `news_risk_high->crypto_major_4h` score `9.0031` n `65` status `ready` deltaP `31.3321` edge `0.5617` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.3832` n `65` status `ready` deltaP `18.872` edge `0.4572` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `4.8581` n `81` status `ready` deltaP `22.8459` edge `0.3145` maxDD `-2.9571`
- `news_risk_high->equity_24h` score `3.4702` n `65` status `ready` deltaP `10.1692` edge `0.2314` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2424` n `65` status `ready` deltaP `22.6804` edge `0.119` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5548` n `65` status `ready` deltaP `28.5601` edge `0.0487` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4354` n `65` status `ready` deltaP `9.2676` edge `0.1767` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9848` n `65` status `ready` deltaP `24.719` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8989` n `65` status `ready` deltaP `16.6135` edge `0.1085` maxDD `-2.881`
- `market_context_high->crypto_major_4h` score `1.8937` n `117` status `ready` deltaP `10.8193` edge `0.1821` maxDD `-4.047`
- `news_risk_high->metal_4h` score `1.721` n `65` status `ready` deltaP `16.3345` edge `0.0761` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.424` n `117` status `ready` deltaP `25.2958` edge `0.0257` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3061` n `117` status `ready` deltaP `17.2113` edge `0.0641` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2476` n `65` status `ready` deltaP `3.9705` edge `0.1294` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9935` n `117` status `ready` deltaP `15.6866` edge `0.0066` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7309` n `117` status `ready` deltaP `12.0554` edge `0.0202` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.6284` n `81` status `ready` deltaP `22.464` edge `0.0683` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.213` n `65` status `ready` deltaP `25.4005` edge `0.0611` maxDD `-10.9169`
- `market_context_high->equity_24h` score `0.1609` n `81` status `ready` deltaP `10.1502` edge `-0.0344` maxDD `-0.5885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
