# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T18:07:28.250142+00:00`
- Price records: `672`
- Market context records: `5065`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_1h` score `13.1479` n `97` status `ready` deltaP `2.8428` edge `1.1268` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0998` n `97` status `ready` deltaP `20.7207` edge `0.7224` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.2064` n `97` status `ready` deltaP `18.4546` edge `0.5161` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5514` n `97` status `ready` deltaP `17.0025` edge `0.5077` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `1.1887` n `97` status `ready` deltaP `8.698` edge `0.1227` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.98` n `97` status `ready` deltaP `10.5843` edge `0.119` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8879` n `97` status `ready` deltaP `8.7799` edge `0.0728` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7051` n `97` status `ready` deltaP `6.0112` edge `0.1718` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.6715` n `97` status `ready` deltaP `6.8847` edge `0.1024` maxDD `-4.7207`
- `market_context_high->unknown_24h` score `0.6622` n `76` status `ready` deltaP `27.3209` edge `-0.0927` maxDD `-1.4072`
- `market_context_high->metal_1h` score `0.4292` n `97` status `ready` deltaP `7.218` edge `0.0373` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0222` n `97` status `ready` deltaP `5.8147` edge `0.0392` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1728` n `76` status `ready` deltaP `7.0266` edge `0.0072` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.2743` n `97` status `ready` deltaP `1.9955` edge `0.0126` maxDD `-0.552`
- `market_context_high->commodity_1h` score `-0.5354` n `97` status `ready` deltaP `0.9985` edge `0.0147` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8407` n `97` status `ready` deltaP `7.2951` edge `0.0062` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9424` n `97` status `ready` deltaP `-3.2232` edge `-0.0004` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4699` n `97` status `ready` deltaP `-8.5792` edge `-0.0043` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.7136` n `76` status `ready` deltaP `3.8378` edge `0.0438` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-3.8592` n `76` status `ready` deltaP `2.8692` edge `-0.0598` maxDD `-24.3277`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
