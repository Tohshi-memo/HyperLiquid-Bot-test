# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T07:52:16.967248+00:00`
- Price records: `672`
- Market context records: `1926`
- Flow alert records: `7443`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7534`

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

- `market_context_high->crypto_alt_4h` score `7.5354` n `205` status `ready` deltaP `23.6281` edge `0.5849` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0472` n `205` status `ready` deltaP `28.7804` edge `0.52` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.6809` n `205` status `ready` deltaP `17.2256` edge `0.3943` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.3702` n `205` status `ready` deltaP `14.6952` edge `0.209` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.7248` n `217` status `ready` deltaP `8.3874` edge `0.1031` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6178` n `196` status `ready` deltaP `13.818` edge `0.4914` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.5258` n `217` status `ready` deltaP `7.3629` edge `0.1061` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3822` n `196` status `ready` deltaP `12.2626` edge `0.1927` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.3384` n `205` status `ready` deltaP `9.3598` edge `0.0747` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.2018` n `196` status `ready` deltaP `4.2233` edge `0.1115` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1597` n `217` status `ready` deltaP `4.7504` edge `0.0344` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2393` n `196` status `ready` deltaP `10.1793` edge `0.0171` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6386` n `217` status `ready` deltaP `0.2332` edge `0.0084` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6602` n `217` status `ready` deltaP `4.8504` edge `0.0166` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6696` n `217` status `ready` deltaP `-3.468` edge `0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.8759` n `205` status `ready` deltaP `-3.4756` edge `-0.0003` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-0.9468` n `205` status `ready` deltaP `10.1829` edge `0.1224` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.1933` n `217` status `ready` deltaP `2.1676` edge `-0.0187` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.3573` n `196` status `ready` deltaP `6.5902` edge `0.3328` maxDD `-33.1875`
- `market_context_high->commodity_1h` score `-2.0111` n `217` status `ready` deltaP `1.0141` edge `-0.0088` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
