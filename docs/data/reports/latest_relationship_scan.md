# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T00:37:26.386427+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6231`

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

- `market_context_high->unknown_24h` score `4140.4856` n `80` status `ready` deltaP `-10.2083` edge `345.1515` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `153.8503` n `80` status `ready` deltaP `0.4268` edge `12.8313` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `76.504` n `108` status `ready` deltaP `-5.1951` edge `6.4386` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.8213` n `92` status `ready` deltaP `35.0921` edge `1.1185` maxDD `-6.3871`
- `market_context_high->equity_24h` score `10.8098` n `80` status `ready` deltaP `20.6597` edge `1.0388` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5706` n `108` status `ready` deltaP `21.189` edge `0.4616` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.0461` n `80` status `ready` deltaP `44.0278` edge `0.1453` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.3107` n `80` status `ready` deltaP `23.0488` edge `0.0723` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.2524` n `80` status `ready` deltaP `15.5183` edge `0.0434` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.9152` n `108` status `ready` deltaP `9.3258` edge `0.1095` maxDD `-3.9659`
- `market_context_high->fx_4h` score `0.7022` n `80` status `ready` deltaP `14.2988` edge `0.0023` maxDD `-0.1285`
- `market_context_high->metal_1h` score `0.6799` n `80` status `ready` deltaP `9.8952` edge `0.0197` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5343` n `80` status `ready` deltaP `13.0539` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.3003` n `80` status `ready` deltaP `0.7485` edge `0.1076` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.2444` n `80` status `ready` deltaP `-3.1402` edge `0.1916` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.1023` n `80` status `ready` deltaP `3.2485` edge `0.068` maxDD `-5.2213`
- `market_context_high->index_1h` score `-0.4803` n `80` status `ready` deltaP `-1.1003` edge `0.0016` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4892` n `80` status `ready` deltaP `-0.9057` edge `0.0167` maxDD `-0.4475`
- `market_context_high->commodity_24h` score `-0.619` n `80` status `ready` deltaP `21.7361` edge `0.0638` maxDD `-14.7123`
- `news_risk_high->index_1h` score `-0.691` n `108` status `ready` deltaP `3.8534` edge `-0.0033` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
