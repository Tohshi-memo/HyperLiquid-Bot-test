# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T16:52:22.338247+00:00`
- Price records: `672`
- Market context records: `2160`
- Flow alert records: `8113`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.4797` n `142` status `ready` deltaP `37.4613` edge `0.9672` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8265` n `142` status `ready` deltaP `41.5707` edge `0.7614` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.8591` n `142` status `ready` deltaP `24.1756` edge `0.402` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.2784` n `142` status `ready` deltaP `25.3028` edge `0.2973` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0535` n `41` status `ready` deltaP `31.8598` edge `0.3744` maxDD `-3.0367`
- `market_context_high->crypto_major_1h` score `3.3714` n `142` status `ready` deltaP `17.8439` edge `0.2097` maxDD `-1.817`
- `market_context_high->index_24h` score `3.2861` n `142` status `ready` deltaP `12.9866` edge `0.3101` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `3.2677` n `142` status `ready` deltaP `16.4966` edge `0.2487` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.1265` n `142` status `ready` deltaP `23.6259` edge `0.1714` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.6651` n `142` status `ready` deltaP `27.4843` edge `0.5709` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.4376` n `142` status `ready` deltaP `24.8215` edge `0.5275` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.3553` n `41` status `ready` deltaP `29.7257` edge `0.0165` maxDD `-0.1382`
- `market_context_high->metal_4h` score `2.3393` n `142` status `ready` deltaP `19.7977` edge `0.2017` maxDD `-4.7664`
- `market_context_high->crypto_major_24h` score `2.1542` n `142` status `ready` deltaP `20.0338` edge `1.0012` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.3965` n `41` status `ready` deltaP `14.0244` edge `0.0952` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0843` n `43` status `ready` deltaP `19.0189` edge `0.0105` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `0.8669` n `41` status `ready` deltaP `-3.8109` edge `0.2573` maxDD `-4.6598`
- `market_context_high->equity_1h` score `0.8044` n `142` status `ready` deltaP `10.6752` edge `0.0747` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7947` n `43` status `ready` deltaP `10.6148` edge `0.0991` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.58` n `142` status `ready` deltaP `9.4543` edge `0.0523` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
