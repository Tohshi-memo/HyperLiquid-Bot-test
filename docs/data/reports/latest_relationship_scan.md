# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T08:52:27.402491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_24h` score `565.0566` n `103` status `ready` deltaP `9.0547` edge `47.0657` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `34.1484` n `103` status `ready` deltaP `-2.7616` edge `2.918` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.926` n `62` status `ready` deltaP `34.6184` edge `0.6167` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.6491` n `62` status `ready` deltaP `22.0201` edge `0.5417` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4748` n `62` status `ready` deltaP `25.0` edge `0.1229` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.1896` n `103` status `ready` deltaP `15.4984` edge `0.2589` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8578` n `62` status `ready` deltaP `32.0024` edge `0.051` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.4846` n `62` status `ready` deltaP `5.7012` edge `0.179` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0847` n `62` status `ready` deltaP `7.7796` edge `0.1574` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0067` n `62` status `ready` deltaP `25.3236` edge `0.0134` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9143` n `62` status `ready` deltaP `17.9288` edge `0.0998` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4138` n `62` status `ready` deltaP `20.1809` edge `0.0883` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.0417` n `103` status `ready` deltaP `15.7244` edge `0.0062` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.9572` n `62` status `ready` deltaP `2.4097` edge `0.1156` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.8639` n `103` status `ready` deltaP `-1.6724` edge `0.2555` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `0.8406` n `103` status `ready` deltaP `6.818` edge `0.3597` maxDD `-16.7906`
- `market_context_high->fx_4h` score `0.747` n `103` status `ready` deltaP `18.1373` edge `0.017` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.4909` n `62` status `ready` deltaP `26.1537` edge `0.0452` maxDD `-8.196`
- `market_context_high->commodity_1h` score `0.4405` n `103` status `ready` deltaP `8.7015` edge `0.0163` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `0.2447` n `103` status `ready` deltaP `10.2538` edge `0.0519` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
