# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T22:22:28.719156+00:00`
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

- `market_context_high->equity_24h` score `8.269` n `81` status `ready` deltaP `7.3302` edge `0.9462` maxDD `-21.1456`
- `market_context_high->metal_24h` score `4.0369` n `81` status `ready` deltaP `13.831` edge `0.3018` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.724` n `81` status `ready` deltaP `33.6034` edge `0.067` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.6861` n `81` status `ready` deltaP `11.8827` edge `0.2126` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.4347` n `103` status `ready` deltaP `15.3534` edge `0.0845` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0811` n `103` status `ready` deltaP `13.0341` edge `0.0375` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.168` n `103` status `ready` deltaP `6.2933` edge `0.0269` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4703` n `103` status `ready` deltaP `-2.885` edge `-0.0063` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.495` n `103` status `ready` deltaP `2.0551` edge `-0.0054` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5553` n `103` status `ready` deltaP `-0.3567` edge `-0.0083` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5938` n `103` status `ready` deltaP `-3.1117` edge `-0.0058` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7192` n `103` status `ready` deltaP `2.6995` edge `-0.0026` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9079` n `103` status `ready` deltaP `-0.7814` edge `-0.0103` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.3348` n `103` status `ready` deltaP `5.7897` edge `-0.0161` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.6342` n `103` status `ready` deltaP `-7.735` edge `-0.0217` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.737` n `81` status `ready` deltaP `11.5548` edge `-0.0503` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1569` n `103` status `ready` deltaP `-5.3398` edge `-0.0445` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5869` n `81` status `ready` deltaP `-21.9521` edge `-0.1692` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7155` n `103` status `ready` deltaP `-7.8351` edge `-0.0922` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.0229` n `103` status `ready` deltaP `-8.4611` edge `-0.1897` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
