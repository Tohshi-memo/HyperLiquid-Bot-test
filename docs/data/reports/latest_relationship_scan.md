# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T03:48:04.841095+00:00`
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

- `market_context_high->equity_24h` score `6.707` n `81` status `ready` deltaP `3.5108` edge `0.8415` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6313` n `81` status `ready` deltaP `11.4005` edge `0.2842` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.7523` n `103` status `ready` deltaP `16.8778` edge `0.1008` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.7217` n `81` status `ready` deltaP `33.6034` edge `0.0667` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.272` n `81` status `ready` deltaP `8.2368` edge `0.2024` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1627` n `103` status `ready` deltaP `13.4832` edge `0.0413` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3286` n `103` status `ready` deltaP `4.946` edge `0.0225` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4866` n `103` status `ready` deltaP `2.2048` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4976` n `103` status `ready` deltaP `-3.3341` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6078` n `103` status `ready` deltaP `-3.4111` edge `-0.0056` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6334` n `103` status `ready` deltaP `-1.4238` edge `-0.0112` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.9431` n `103` status `ready` deltaP `0.2604` edge `-0.005` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0494` n `103` status `ready` deltaP `-3.068` edge `-0.0132` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.802` n `103` status `ready` deltaP `-9.3817` edge `-0.0247` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-1.8897` n `103` status `ready` deltaP `2.5885` edge `-0.041` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.1728` n `81` status `ready` deltaP `9.8187` edge `-0.0946` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.2588` n `103` status `ready` deltaP `-6.0883` edge `-0.048` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.6125` n `81` status `ready` deltaP `-21.6049` edge `-0.1748` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7033` n `103` status `ready` deltaP `-7.6827` edge `-0.0922` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.2201` n `103` status `ready` deltaP `-9.6806` edge `-0.198` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
