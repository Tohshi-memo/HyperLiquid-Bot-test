# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T17:07:36.540262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1584.6358` n `117` status `ready` deltaP `11.0847` edge `132.0171` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.0875` n `117` status `ready` deltaP `-0.3583` edge `2.3969` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `8.9537` n `62` status `ready` deltaP `32.4843` edge `0.5499` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.1004` n `62` status `ready` deltaP `18.6664` edge `0.435` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0748` n `62` status `ready` deltaP `21.6495` edge `0.1119` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.8684` n `62` status `ready` deltaP `8.6687` edge `0.1912` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.4029` n `62` status `ready` deltaP `27.2768` edge `0.0446` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.2088` n `117` status `ready` deltaP `12.3437` edge `0.1982` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.9144` n `62` status `ready` deltaP `7.3305` edge `0.1462` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8163` n `62` status `ready` deltaP `23.2278` edge `0.0115` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.4149` n `62` status `ready` deltaP `14.8801` edge `0.0785` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1877` n `62` status `ready` deltaP `17.437` edge `0.0776` maxDD `-0.993`
- `market_context_high->commodity_4h` score `0.9414` n `117` status `ready` deltaP `14.4674` edge `0.052` maxDD `-1.6002`
- `news_risk_high->commodity_24h` score `0.9259` n `62` status `ready` deltaP `28.3838` edge `0.0861` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8946` n `117` status `ready` deltaP `19.5031` edge `0.0202` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7567` n `62` status `ready` deltaP `2.8588` edge `0.0959` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7276` n `117` status `ready` deltaP `12.5429` edge `0.0054` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.5896` n `117` status `ready` deltaP `10.7081` edge `0.0174` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `-0.0244` n `117` status `ready` deltaP `-2.2462` edge `0.1853` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0816` n `62` status `ready` deltaP `4.6552` edge `0.004` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
