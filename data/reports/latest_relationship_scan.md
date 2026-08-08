# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T03:37:30.248345+00:00`
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

- `market_context_high->equity_24h` score `6.7581` n `81` status `ready` deltaP `3.6844` edge `0.8446` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6385` n `81` status `ready` deltaP `11.4005` edge `0.2848` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.7681` n `103` status `ready` deltaP `17.0302` edge `0.1011` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.7209` n `81` status `ready` deltaP `33.6034` edge `0.0666` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.2756` n `81` status `ready` deltaP `8.2368` edge `0.2027` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1663` n `103` status `ready` deltaP `13.4832` edge `0.0416` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3154` n `103` status `ready` deltaP `5.0957` edge `0.0226` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4866` n `103` status `ready` deltaP `2.2048` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5061` n `103` status `ready` deltaP `-3.4838` edge `-0.0069` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6078` n `103` status `ready` deltaP `-3.4111` edge `-0.0056` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6342` n `103` status `ready` deltaP `-1.4238` edge `-0.0113` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.9309` n `103` status `ready` deltaP `0.4129` edge `-0.005` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0407` n `103` status `ready` deltaP `-2.9156` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.7852` n `103` status `ready` deltaP `-9.232` edge `-0.0243` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-1.8897` n `103` status `ready` deltaP `2.5885` edge `-0.041` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.1451` n `81` status `ready` deltaP `9.9923` edge `-0.0922` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.2528` n `103` status `ready` deltaP `-6.0883` edge `-0.0475` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5988` n `81` status `ready` deltaP `-21.4313` edge `-0.1742` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7057` n `103` status `ready` deltaP `-7.6827` edge `-0.0924` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.2129` n `103` status `ready` deltaP `-9.6806` edge `-0.1974` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
