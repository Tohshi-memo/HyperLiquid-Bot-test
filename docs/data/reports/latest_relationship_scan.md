# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T00:22:29.477082+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7065`

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

- `market_context_high->unknown_24h` score `7620.5875` n `55` status `ready` deltaP `1.3889` edge `635.0397` maxDD `0.0`
- `market_context_high->unknown_4h` score `331.2014` n `55` status `ready` deltaP `7.1757` edge `27.5566` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `37.2925` n `55` status `ready` deltaP `4.5101` edge `3.0887` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.3208` n `55` status `ready` deltaP `42.7999` edge `1.515` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.3875` n `94` status `ready` deltaP `31.6563` edge `1.0402` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.171` n `55` status `ready` deltaP `49.1319` edge `0.1867` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0411` n `55` status `ready` deltaP `23.9024` edge `0.3735` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8698` n `55` status `ready` deltaP `40.5808` edge `0.2497` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.4695` n `55` status `ready` deltaP `30.5876` edge `0.2855` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.2048` n `55` status `ready` deltaP `5.5903` edge `0.3` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.0268` n `55` status `ready` deltaP `29.0854` edge `0.0834` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4173` n `55` status `ready` deltaP `10.5114` edge `0.3075` maxDD `-3.0799`
- `news_risk_high->crypto_alt_4h` score `2.3631` n `126` status `ready` deltaP `9.7754` edge `0.2704` maxDD `-7.4246`
- `market_context_high->crypto_alt_24h` score `2.0123` n `55` status `ready` deltaP `-3.6048` edge `0.4338` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7543` n `55` status `ready` deltaP `20.6374` edge `0.0511` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4961` n `55` status `ready` deltaP `3.0267` edge `0.157` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.392` n `55` status `ready` deltaP `3.6255` edge `0.1589` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.3856` n `55` status `ready` deltaP `8.0321` edge `0.1229` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9426` n `55` status `ready` deltaP `11.7746` edge `0.0249` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5568` n `55` status `ready` deltaP `13.4867` edge `-0.0001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
