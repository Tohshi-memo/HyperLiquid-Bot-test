# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T19:22:28.137293+00:00`
- Price records: `672`
- Market context records: `2691`
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

- `market_context_high->crypto_alt_24h` score `9.6257` n `111` status `ready` deltaP `16.0051` edge `1.0448` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6587` n `111` status `ready` deltaP `17.652` edge `0.6367` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.875` n `139` status `ready` deltaP `5.5481` edge `0.1409` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2267` n `139` status `ready` deltaP `11.6566` edge `0.0355` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1355` n `143` status `ready` deltaP `3.35` edge `0.0097` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1523` n `143` status `ready` deltaP `2.8988` edge `0.0408` maxDD `-3.1587`
- `market_context_high->commodity_1h` score `-0.4408` n `143` status `ready` deltaP `1.8488` edge `0.0065` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.4516` n `111` status `ready` deltaP `7.8688` edge `-0.0029` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-0.4668` n `143` status `ready` deltaP `0.2513` edge `0.0038` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5377` n `143` status `ready` deltaP `6.4445` edge `0.0641` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.5569` n `139` status `ready` deltaP `16.4195` edge `0.276` maxDD `-28.5496`
- `market_context_high->fx_4h` score `-0.6981` n `139` status `ready` deltaP `-0.5549` edge `0.0109` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.7455` n `111` status `ready` deltaP `7.0946` edge `0.1665` maxDD `-12.4171`
- `market_context_high->metal_1h` score `-0.7676` n `143` status `ready` deltaP `-1.5494` edge `-0.0035` maxDD `-3.0996`
- `market_context_high->index_24h` score `-0.8189` n `111` status `ready` deltaP `4.1902` edge `0.0019` maxDD `-2.5127`
- `market_context_high->crypto_major_24h` score `-0.8502` n `111` status `ready` deltaP `5.9967` edge `0.6073` maxDD `-44.169`
- `market_context_high->crypto_major_1h` score `-0.9986` n `143` status `ready` deltaP `3.4976` edge `0.0356` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0323` n `139` status `ready` deltaP `4.6149` edge `0.0289` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2259` n `143` status `ready` deltaP `-4.4857` edge `0.0116` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-2.0536` n `139` status `ready` deltaP `-1.4531` edge `-0.021` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
