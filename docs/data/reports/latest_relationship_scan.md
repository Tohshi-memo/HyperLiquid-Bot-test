# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T13:37:27.635815+00:00`
- Price records: `672`
- Market context records: `4832`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.7427` n `109` status `ready` deltaP `11.038` edge `1.1134` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9864` n `105` status `ready` deltaP `20.0189` edge `0.7289` maxDD `-4.0797`
- `market_context_high->unknown_24h` score `3.5408` n `98` status `ready` deltaP `17.9811` edge `0.2365` maxDD `-2.2379`
- `market_context_high->index_4h` score `0.7335` n `105` status `ready` deltaP `9.7344` edge `0.0429` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.5304` n `105` status `ready` deltaP `11.6768` edge `0.1283` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.2682` n `105` status `ready` deltaP `13.9649` edge `0.0585` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1439` n `109` status `ready` deltaP `5.2683` edge `0.0315` maxDD `-1.1869`
- `market_context_high->equity_1h` score `-0.1608` n `109` status `ready` deltaP `3.0421` edge `0.0207` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.3257` n `105` status `ready` deltaP `4.0955` edge `0.0029` maxDD `-1.0904`
- `market_context_high->index_1h` score `-0.5656` n `109` status `ready` deltaP `-0.5892` edge `0.0069` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.0554` n `109` status `ready` deltaP `-2.8196` edge `-0.0042` maxDD `-0.8626`
- `market_context_high->crypto_alt_4h` score `-1.5333` n `105` status `ready` deltaP `11.2195` edge `0.1031` maxDD `-26.2914`
- `market_context_high->fx_24h` score `-2.2403` n `98` status `ready` deltaP `-10.1793` edge `-0.0178` maxDD `-2.749`
- `market_context_high->metal_1h` score `-2.2958` n `109` status `ready` deltaP `-1.4723` edge `-0.0742` maxDD `-13.4916`
- `market_context_high->crypto_alt_1h` score `-2.3078` n `109` status `ready` deltaP `3.3222` edge `-0.0221` maxDD `-12.7225`
- `market_context_high->commodity_24h` score `-2.675` n `98` status `ready` deltaP `16.0395` edge `0.061` maxDD `-27.5371`
- `market_context_high->crypto_major_1h` score `-3.4749` n `109` status `ready` deltaP `2.0477` edge `-0.0457` maxDD `-17.9354`
- `market_context_high->crypto_major_4h` score `-3.7262` n `105` status `ready` deltaP `7.8296` edge `0.0122` maxDD `-39.7028`
- `market_context_high->index_24h` score `-4.1245` n `98` status `ready` deltaP `-4.0994` edge `-0.1106` maxDD `-23.2678`
- `market_context_high->metal_4h` score `-5.3953` n `105` status `ready` deltaP `7.336` edge `-0.2061` maxDD `-39.4275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
