# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T09:37:30.822108+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3714`

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

- `news_risk_high->unknown_1h` score `3386.4372` n `31` status `ready` deltaP `2.0813` edge `282.2068` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3247.1926` n `31` status `ready` deltaP `3.7864` edge `270.5798` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.7024` n `31` status `ready` deltaP `33.2756` edge `1.5867` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5805` n `31` status `ready` deltaP `31.1958` edge `1.0904` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.1792` n `31` status `ready` deltaP `26.6898` edge `0.837` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.3442` n `31` status `ready` deltaP `21.8823` edge `0.6365` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.3535` n `31` status `ready` deltaP `29.9076` edge `0.2948` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1833` n `31` status `ready` deltaP `15.8635` edge `0.7005` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9557` n `31` status `ready` deltaP `40.7559` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.7273` n `31` status `ready` deltaP `15.1339` edge `0.2372` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3784` n `31` status `ready` deltaP `29.2978` edge `0.0289` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3323` n `31` status `ready` deltaP `25.8232` edge `0.0222` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3127` n `31` status `ready` deltaP `28.3997` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1388` n `31` status `ready` deltaP `14.2988` edge `0.1016` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8718` n `31` status `ready` deltaP `6.1184` edge `0.2453` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7015` n `31` status `ready` deltaP `8.813` edge `0.1951` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1309` n `31` status `ready` deltaP `24.6426` edge `0.0086` maxDD `-0.2315`
- `market_context_high->fx_4h` score `0.9067` n `31` status `ready` deltaP `14.2112` edge `0.019` maxDD `-0.0545`
- `market_context_high->fx_1h` score `0.399` n `43` status `ready` deltaP `10.4651` edge `0.0028` maxDD `-0.0466`
- `news_risk_high->commodity_4h` score `0.3682` n `31` status `ready` deltaP `9.1316` edge `0.0261` maxDD `-0.5151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
