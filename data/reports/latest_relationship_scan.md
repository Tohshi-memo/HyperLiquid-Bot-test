# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T17:22:38.266540+00:00`
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

- `market_context_high->unknown_24h` score `1577.1322` n `117` status `ready` deltaP `11.0847` edge `131.3918` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.2087` n `117` status `ready` deltaP `-0.3583` edge `2.407` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `8.9657` n `62` status `ready` deltaP `32.4843` edge `0.5509` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.1124` n `62` status `ready` deltaP `18.6664` edge `0.436` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0772` n `62` status `ready` deltaP `21.6495` edge `0.1121` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.8403` n `62` status `ready` deltaP `8.4969` edge `0.19` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.4175` n `62` status `ready` deltaP `27.4292` edge `0.0448` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.2208` n `117` status `ready` deltaP `12.3437` edge `0.1992` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.9336` n `62` status `ready` deltaP `7.4802` edge `0.1468` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8175` n `62` status `ready` deltaP `23.2278` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.4137` n `62` status `ready` deltaP `14.8801` edge `0.0784` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.19` n `62` status `ready` deltaP `17.437` edge `0.0779` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9364` n `62` status `ready` deltaP `28.5556` edge `0.0863` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.916` n `117` status `ready` deltaP `14.315` edge `0.0509` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.8812` n `117` status `ready` deltaP `19.3507` edge `0.0201` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7627` n `62` status `ready` deltaP `2.8588` edge `0.0964` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7144` n `117` status `ready` deltaP `12.3932` edge `0.0053` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.5728` n `117` status `ready` deltaP `10.5584` edge `0.017` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `-0.0124` n `117` status `ready` deltaP `-2.2462` edge `0.1863` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0684` n `62` status `ready` deltaP `4.8049` edge `0.0041` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
