# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T21:37:32.618392+00:00`
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

- `market_context_high->equity_24h` score `7.239` n `84` status `ready` deltaP `4.9852` edge `0.876` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.8633` n `84` status `ready` deltaP `14.3601` edge `0.2838` maxDD `-2.2743`
- `market_context_high->index_24h` score `1.5491` n `84` status `ready` deltaP `11.88` edge `0.2012` maxDD `-5.7715`
- `market_context_high->fx_24h` score `1.5405` n `84` status `ready` deltaP `31.002` edge `0.0636` maxDD `-2.1562`
- `market_context_high->commodity_4h` score `1.5013` n `106` status `ready` deltaP `15.8853` edge `0.0865` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.1453` n `106` status `ready` deltaP `13.6566` edge `0.0387` maxDD `-0.7439`
- `market_context_high->equity_1h` score `0.0261` n `106` status `ready` deltaP `7.1602` edge `0.0373` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.3695` n `106` status `ready` deltaP `3.429` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.405` n `106` status `ready` deltaP `-1.9602` edge `-0.0041` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.4717` n `106` status `ready` deltaP `0.9348` edge `-0.0062` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.5755` n `106` status `ready` deltaP `4.2108` edge `-0.0007` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.8384` n `106` status `ready` deltaP `0.3452` edge `-0.0089` maxDD `-2.7373`
- `market_context_high->metal_1h` score `-0.9388` n `106` status `ready` deltaP `-3.3527` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.1828` n `106` status `ready` deltaP `6.8338` edge `-0.0104` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.4897` n `106` status `ready` deltaP `-6.6179` edge `-0.0171` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-2.0064` n `84` status `ready` deltaP `8.9534` edge `-0.0675` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1873` n `106` status `ready` deltaP `-5.8101` edge `-0.0439` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.4817` n `84` status `ready` deltaP `-20.7093` edge `-0.164` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.5814` n `106` status `ready` deltaP `-6.6987` edge `-0.0886` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1626` n `106` status `ready` deltaP `-9.1579` edge `-0.189` maxDD `-18.7465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
