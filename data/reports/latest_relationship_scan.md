# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T23:07:28.636000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `8.0785` n `81` status `ready` deltaP `6.8094` edge `0.9338` maxDD `-21.1456`
- `market_context_high->metal_24h` score `4.0105` n `81` status `ready` deltaP `13.831` edge `0.2996` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7248` n `81` status `ready` deltaP `33.6034` edge `0.0671` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.6348` n `81` status `ready` deltaP `11.3618` edge `0.2118` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.5001` n `103` status `ready` deltaP `15.8107` edge `0.0869` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.1099` n `103` status `ready` deltaP `13.3335` edge `0.0379` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.1285` n `103` status `ready` deltaP `6.443` edge `0.0292` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4687` n `103` status `ready` deltaP `-2.885` edge `-0.0061` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5201` n `103` status `ready` deltaP `1.7557` edge `-0.0055` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5663` n `103` status `ready` deltaP `-0.5091` edge `-0.0087` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5914` n `103` status `ready` deltaP `-3.1117` edge `-0.0055` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7606` n `103` status `ready` deltaP `2.2421` edge `-0.003` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9071` n `103` status `ready` deltaP `-0.7814` edge `-0.0102` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.4086` n `103` status `ready` deltaP `5.3324` edge `-0.0192` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.5803` n `103` status `ready` deltaP `-7.4356` edge `-0.0192` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.7432` n `81` status `ready` deltaP `11.5548` edge `-0.0511` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.0958` n `103` status `ready` deltaP `-4.8907` edge `-0.0424` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5294` n `81` status `ready` deltaP `-21.4313` edge `-0.1653` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.6901` n `103` status `ready` deltaP `-7.6827` edge `-0.0911` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.0763` n `103` status `ready` deltaP `-8.9184` edge `-0.1911` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
