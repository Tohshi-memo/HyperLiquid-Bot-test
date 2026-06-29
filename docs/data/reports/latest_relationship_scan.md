# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T20:22:26.165305+00:00`
- Price records: `672`
- Market context records: `5178`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `24.6906` n `76` status `ready` deltaP `32.584` edge `1.8593` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.9484` n `76` status `ready` deltaP `23.8396` edge `1.1196` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.3243` n `76` status `ready` deltaP `25.0091` edge `0.949` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.0089` n `149` status `ready` deltaP `20.1987` edge `0.4683` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.9615` n `149` status `ready` deltaP `15.2213` edge `0.4719` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.6321` n `149` status `ready` deltaP `14.184` edge `0.5207` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6671` n `155` status `ready` deltaP `9.7363` edge `0.2215` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.3516` n `149` status `ready` deltaP `8.9397` edge `0.2169` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5529` n `155` status `ready` deltaP `4.3539` edge `0.1132` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5393` n `155` status `ready` deltaP `6.553` edge `0.1258` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3544` n `155` status `ready` deltaP `8.5136` edge `0.0693` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0238` n `155` status `ready` deltaP `5.7833` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0436` n `155` status `ready` deltaP `5.309` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.0545` n `76` status `ready` deltaP `9.9142` edge `0.0189` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.2409` n `155` status `ready` deltaP `2.1084` edge `0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4212` n `149` status `ready` deltaP `5.9164` edge `0.0372` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5614` n `149` status `ready` deltaP `3.6933` edge `0.0068` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6211` n `155` status `ready` deltaP `0.2762` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `-1.1407` n `76` status `ready` deltaP `9.6491` edge `0.059` maxDD `-12.5658`
- `market_context_high->index_24h` score `-1.2096` n `76` status `ready` deltaP `3.9931` edge `-0.0182` maxDD `-7.413`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
