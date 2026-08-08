# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T15:07:31.457938+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.804` n `96` status `ready` deltaP `3.2986` edge `0.601` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.576` n `96` status `ready` deltaP `10.7639` edge `0.2005` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.452` n `103` status `ready` deltaP `13.829` edge `0.0961` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.2059` n `96` status `ready` deltaP `27.4305` edge `0.0584` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.995` n `103` status `ready` deltaP `11.5371` edge `0.0403` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4002` n `96` status `ready` deltaP `7.118` edge `0.157` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4508` n `103` status `ready` deltaP `3.5987` edge `0.0213` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4986` n `103` status `ready` deltaP `2.0551` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5123` n `103` status `ready` deltaP `-3.6335` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6208` n `103` status `ready` deltaP `-1.2713` edge `-0.0106` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6475` n `103` status `ready` deltaP `-4.1596` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8747` n `103` status `ready` deltaP `1.1751` edge `-0.0054` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.047` n `103` status `ready` deltaP `-3.068` edge `-0.0129` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.9257` n `103` status `ready` deltaP `2.5885` edge `-0.044` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.9829` n `103` status `ready` deltaP `-11.1781` edge `-0.0278` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.5212` n `103` status `ready` deltaP `-8.3338` edge `-0.0549` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.5679` n `96` status `ready` deltaP `4.8611` edge `-0.1122` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.0042` n `96` status `ready` deltaP `-15.2778` edge `-0.139` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2254` n `103` status `ready` deltaP `-11.4936` edge `-0.1103` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.9149` n `103` status `ready` deltaP `-14.4062` edge `-0.2244` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
