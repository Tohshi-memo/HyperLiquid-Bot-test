# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T05:22:25.043690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11764`

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

- `market_context_high->equity_24h` score `6.4041` n `81` status `ready` deltaP `2.4691` edge `0.8232` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.5965` n `81` status `ready` deltaP `11.4005` edge `0.2813` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7232` n `81` status `ready` deltaP `33.6034` edge `0.0669` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.6879` n `103` status `ready` deltaP `16.268` edge `0.0995` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1786` n `81` status `ready` deltaP `7.3688` edge `0.2004` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1555` n `103` status `ready` deltaP `13.3335` edge `0.0417` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2963` n `103` status `ready` deltaP `5.2454` edge `0.0232` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.489` n `103` status `ready` deltaP `-3.1844` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.501` n `103` status `ready` deltaP `2.0551` edge `-0.0059` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5986` n `103` status `ready` deltaP `-0.814` edge `-0.0108` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6163` n `103` status `ready` deltaP `-3.5608` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9565` n `103` status `ready` deltaP `0.108` edge `-0.0051` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0486` n `103` status `ready` deltaP `-3.068` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.796` n `103` status `ready` deltaP `-9.3817` edge `-0.0242` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-1.7997` n `103` status `ready` deltaP `3.5031` edge `-0.0396` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.3043` n `103` status `ready` deltaP `-6.5374` edge `-0.0488` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.358` n `81` status `ready` deltaP `8.777` edge `-0.1114` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6829` n `103` status `ready` deltaP `-7.6827` edge `-0.0905` maxDD `-6.5487`
- `market_context_high->crypto_alt_24h` score `-3.7127` n `81` status `ready` deltaP `-22.6466` edge `-0.1807` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.2513` n `103` status `ready` deltaP `-9.6806` edge `-0.2006` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
