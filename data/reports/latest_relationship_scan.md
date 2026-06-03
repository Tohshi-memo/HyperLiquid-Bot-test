# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T04:07:22.502868+00:00`
- Price records: `672`
- Market context records: `2728`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.4115` n `111` status `ready` deltaP `16.3523` edge `1.1913` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6556` n `111` status `ready` deltaP `17.4784` edge `0.6376` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.2361` n `111` status `ready` deltaP `6.5175` edge `0.8713` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.1359` n `143` status `ready` deltaP `7.4685` edge `0.1502` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0625` n `143` status `ready` deltaP `9.7892` edge `0.0269` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1507` n `143` status `ready` deltaP `2.8988` edge `0.0412` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1674` n `143` status `ready` deltaP `3.0506` edge `0.0076` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.4269` n `143` status `ready` deltaP `16.5157` edge `0.2884` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5195` n `143` status `ready` deltaP `-0.3475` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5249` n `143` status `ready` deltaP `1.1003` edge `0.0007` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5393` n `143` status `ready` deltaP `6.1451` edge `0.0659` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7785` n `143` status `ready` deltaP `-1.6991` edge `-0.0039` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9089` n `143` status `ready` deltaP `3.6473` edge `0.0461` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0177` n `143` status `ready` deltaP `-2.421` edge `0.0092` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.0361` n `111` status `ready` deltaP `1.7924` edge `-0.0111` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.2447` n `143` status `ready` deltaP `-4.3852` edge `0.0088` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3409` n `143` status `ready` deltaP `1.6662` edge `0.009` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6144` n `111` status `ready` deltaP `2.5807` edge `0.0852` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0793` n `143` status `ready` deltaP `-1.0969` edge `-0.028` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.3228` n `143` status `ready` deltaP `6.4473` edge `0.1498` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
