# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T16:22:26.047571+00:00`
- Price records: `672`
- Market context records: `2679`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.1133` n `111` status `ready` deltaP `16.0051` edge `1.0021` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7373` n `111` status `ready` deltaP `17.8256` edge `0.6421` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `2.5047` n `131` status `ready` deltaP `19.9137` edge `0.3598` maxDD `-16.7069`
- `market_context_high->unknown_4h` score `1.4365` n `131` status `ready` deltaP `7.5568` edge `0.1743` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.0806` n `131` status `ready` deltaP `9.8527` edge `0.0288` maxDD `-2.3986`
- `market_context_high->crypto_major_4h` score `-0.0206` n `131` status `ready` deltaP `8.0106` edge `0.2021` maxDD `-16.3181`
- `market_context_high->index_1h` score `-0.1309` n `139` status `ready` deltaP `3.3624` edge `0.0102` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.2477` n `111` status `ready` deltaP `9.9522` edge `0.0002` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4349` n `139` status `ready` deltaP `1.9773` edge `0.0064` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4538` n `139` status `ready` deltaP `2.1604` edge `0.0206` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.489` n `139` status `ready` deltaP `-0.0269` edge `0.0038` maxDD `-0.2164`
- `market_context_high->index_24h` score `-0.4892` n `111` status `ready` deltaP `5.9263` edge `0.0178` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `-0.5163` n `111` status `ready` deltaP `7.9627` edge `0.1901` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.5682` n `131` status `ready` deltaP `0.8436` edge `0.0124` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-0.6204` n `139` status `ready` deltaP `6.6848` edge `0.0519` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7412` n `139` status `ready` deltaP `-1.6489` edge `-0.0017` maxDD `-2.9203`
- `market_context_high->crypto_major_1h` score `-1.0378` n `139` status `ready` deltaP `3.5077` edge `0.0305` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2354` n `139` status `ready` deltaP `-4.6342` edge `0.0118` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.237` n `131` status `ready` deltaP `3.4386` edge `0.0105` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.2769` n `111` status `ready` deltaP `5.9967` edge `0.5526` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
