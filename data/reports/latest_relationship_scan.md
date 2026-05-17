# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T11:22:15.324509+00:00`
- Price records: `672`
- Market context records: `1007`
- Flow alert records: `4807`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.079` n `205` status `ready` deltaP `32.035` edge `0.9352` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1686` n `205` status `ready` deltaP `10.9626` edge `0.3977` maxDD `-9.5387`
- `market_context_high->index_24h` score `-0.4151` n `205` status `ready` deltaP `4.0886` edge `0.1333` maxDD `-5.6116`
- `market_context_high->fx_1h` score `-0.5192` n `205` status `ready` deltaP `2.2054` edge `0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5964` n `205` status `ready` deltaP `2.1126` edge `0.017` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7075` n `205` status `ready` deltaP `3.1342` edge `0.0055` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7092` n `205` status `ready` deltaP `1.0975` edge `0.0014` maxDD `-1.6381`
- `market_context_high->equity_1h` score `-0.7184` n `205` status `ready` deltaP `0.1351` edge `0.0161` maxDD `-4.4826`
- `market_context_high->equity_24h` score `-1.0258` n `205` status `ready` deltaP `4.3939` edge `0.1457` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2391` n `205` status `ready` deltaP `4.7167` edge `-0.018` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3823` n `205` status `ready` deltaP `-1.3874` edge `-0.024` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5173` n `205` status `ready` deltaP `1.494` edge `0.0788` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7499` n `205` status `ready` deltaP `-1.7988` edge `0.018` maxDD `-6.4798`
- `market_context_high->metal_1h` score `-1.8347` n `205` status `ready` deltaP `-0.1175` edge `-0.0385` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.9385` n `205` status `ready` deltaP `6.7988` edge `0.0804` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.1222` n `205` status `ready` deltaP `-1.1281` edge `0.0641` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.304` n `205` status `ready` deltaP `-2.0732` edge `0.0163` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.4588` n `205` status `ready` deltaP `-1.0873` edge `-0.0221` maxDD `-19.7935`
- `market_context_high->metal_4h` score `-4.5826` n `205` status `ready` deltaP `-4.3903` edge `-0.1654` maxDD `-24.7606`
- `market_context_high->commodity_24h` score `-8.3274` n `205` status `ready` deltaP `2.2305` edge `0.3823` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
