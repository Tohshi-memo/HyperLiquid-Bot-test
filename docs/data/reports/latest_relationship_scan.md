# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T02:37:33.832694+00:00`
- Price records: `672`
- Market context records: `5412`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11492`

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

- `market_context_high->crypto_major_24h` score `4.0742` n `194` status `ready` deltaP `19.7612` edge `0.6618` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.9523` n `205` status `ready` deltaP `16.9207` edge `0.4458` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.177` n `205` status `ready` deltaP `12.5305` edge `0.3453` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.4568` n `205` status `ready` deltaP `12.1952` edge `0.2873` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3649` n `205` status `ready` deltaP `7.3105` edge `0.0782` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.0969` n `205` status `ready` deltaP `4.7736` edge `0.1008` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0735` n `205` status `ready` deltaP `6.0253` edge `0.0153` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `0.0168` n `205` status `ready` deltaP `2.3784` edge `0.0817` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.0404` n `194` status `ready` deltaP `8.3799` edge `0.0303` maxDD `-0.8294`
- `market_context_high->equity_24h` score `-0.2672` n `194` status `ready` deltaP `8.0327` edge `0.5079` maxDD `-40.0306`
- `market_context_high->fx_1h` score `-0.4641` n `205` status `ready` deltaP `-1.4028` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5766` n `205` status `ready` deltaP `1.3305` edge `0.0106` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9337` n `205` status `ready` deltaP `6.7073` edge `0.0384` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2511` n `205` status `ready` deltaP `-0.3658` edge `0.0011` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4711` n `205` status `ready` deltaP `-3.1707` edge `-0.007` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6355` n `194` status `ready` deltaP `12.8275` edge `0.0768` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.5164` n `205` status `ready` deltaP `-6.2195` edge `-0.0287` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2523` n `205` status `ready` deltaP `-6.8292` edge `-0.045` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.1021` n `194` status `ready` deltaP `11.0252` edge `0.2877` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.052` n `194` status `ready` deltaP `-4.5962` edge `-0.1357` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
