# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T06:07:25.113786+00:00`
- Price records: `672`
- Market context records: `2839`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.4013` n `142` status `ready` deltaP `3.2961` edge `0.2246` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.1893` n `142` status `ready` deltaP `0.7923` edge `0.4855` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8668` n `142` status `ready` deltaP `6.4904` edge `0.1343` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7219` n `142` status `ready` deltaP `11.2114` edge `0.2948` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3412` n `142` status `ready` deltaP `13.4533` edge `0.0382` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0766` n `142` status `ready` deltaP `4.4805` edge `0.0496` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.096` n `142` status `ready` deltaP `4.0483` edge `0.0101` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.1929` n `142` status `ready` deltaP `4.3354` edge `0.0531` maxDD `-2.5127`
- `market_context_high->fx_1h` score `-0.5778` n `142` status `ready` deltaP `-0.9867` edge `0.0028` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6109` n `142` status `ready` deltaP `-0.2825` edge `-0.0011` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7214` n `142` status `ready` deltaP `-0.0169` edge `-0.0078` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7482` n `142` status `ready` deltaP `4.6471` edge `0.0491` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.9698` n `142` status `ready` deltaP `-2.8991` edge `0.0218` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9763` n `142` status `ready` deltaP `3.6266` edge `0.0376` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0366` n `142` status `ready` deltaP `1.9624` edge `0.0385` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1311` n `142` status `ready` deltaP `-3.4481` edge `0.0066` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3641` n `142` status `ready` deltaP `1.6854` edge `0.0059` maxDD `-10.0279`
- `market_context_high->crypto_alt_4h` score `-1.4573` n `142` status `ready` deltaP `13.8805` edge `0.2201` maxDD `-28.7261`
- `market_context_high->equity_24h` score `-1.4607` n `142` status `ready` deltaP `2.1371` edge `0.0644` maxDD `-12.6963`
- `market_context_high->fx_24h` score `-1.4974` n `142` status `ready` deltaP `-2.5797` edge `-0.0204` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
