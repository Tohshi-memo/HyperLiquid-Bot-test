# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T14:22:26.796594+00:00`
- Price records: `672`
- Market context records: `2874`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `7.1952` n `142` status `ready` deltaP `6.5215` edge `0.9478` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.3503` n `142` status `ready` deltaP `8.5045` edge `0.3523` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.0905` n `142` status `ready` deltaP `7.8663` edge `0.4888` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.0751` n `142` status `ready` deltaP `10.0646` edge `0.2039` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6685` n `142` status `ready` deltaP `15.378` edge `0.3459` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.895` n `142` status `ready` deltaP `6.0331` edge `0.1397` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.7484` n `142` status `ready` deltaP `15.435` edge `0.0772` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.015` n `142` status `ready` deltaP `4.6471` edge `0.0165` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.0253` n `142` status `ready` deltaP `4.1811` edge `0.0431` maxDD `-3.1801`
- `market_context_high->equity_4h` score `-0.0506` n `142` status `ready` deltaP `4.4014` edge `0.1044` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.5013` n `142` status `ready` deltaP `14.4903` edge `0.2957` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.6046` n `142` status `ready` deltaP `-0.7316` edge `0.0027` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6784` n `142` status `ready` deltaP `-2.1843` edge `0.0024` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.7271` n `142` status `ready` deltaP `4.4974` edge `0.0528` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7557` n `142` status `ready` deltaP `-0.9151` edge `-0.0062` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.772` n `142` status `ready` deltaP `-2.0009` edge `0.0323` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8594` n `142` status `ready` deltaP `4.3751` edge `0.0476` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1401` n `142` status `ready` deltaP `3.6671` edge `0.0214` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2917` n `142` status `ready` deltaP `-5.1249` edge `0.0044` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3903` n `142` status `ready` deltaP `-1.8852` edge `-0.0161` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
