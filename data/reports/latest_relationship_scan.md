# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T17:37:25.613424+00:00`
- Price records: `672`
- Market context records: `2887`
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

- `market_context_high->crypto_alt_24h` score `9.3834` n `142` status `ready` deltaP `8.7784` edge `1.1151` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.1686` n `142` status `ready` deltaP `10.1232` edge `0.5636` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `4.9752` n `142` status `ready` deltaP `10.2406` edge `0.3928` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2772` n `142` status `ready` deltaP `11.1062` edge `0.2138` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7412` n `142` status `ready` deltaP `15.5516` edge `0.3508` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.6197` n `142` status `ready` deltaP `14.5204` edge `0.0668` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.553` n `142` status `ready` deltaP `6.0331` edge `0.1112` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0391` n `142` status `ready` deltaP `4.198` edge `0.0164` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1646` n `142` status `ready` deltaP `4.4014` edge `0.0949` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.2246` n `142` status `ready` deltaP `4.3308` edge `0.0255` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.5906` n `142` status `ready` deltaP `-0.5819` edge `0.0035` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6094` n `142` status `ready` deltaP `5.2459` edge `0.0629` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.6213` n `142` status `ready` deltaP `14.4903` edge `0.2857` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.6521` n `142` status `ready` deltaP `-1.8849` edge `0.0026` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6793` n `142` status `ready` deltaP `-0.466` edge `0.0006` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7025` n `142` status `ready` deltaP `-1.5518` edge `0.0351` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.7136` n `142` status `ready` deltaP `5.2733` edge `0.0603` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0931` n `142` status `ready` deltaP `3.972` edge `0.0254` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2247` n `142` status `ready` deltaP `-4.3627` edge `0.0049` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3627` n `142` status `ready` deltaP `-1.8852` edge `-0.0138` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
