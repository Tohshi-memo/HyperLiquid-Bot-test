# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T19:22:26.603346+00:00`
- Price records: `672`
- Market context records: `2895`
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

- `market_context_high->crypto_alt_24h` score `10.3036` n `142` status `ready` deltaP `9.6465` edge `1.186` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.6042` n `142` status `ready` deltaP `11.3385` edge `0.5918` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.1` n `142` status `ready` deltaP `10.2406` edge `0.4032` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1759` n `142` status `ready` deltaP `10.0646` edge `0.2123` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7352` n `142` status `ready` deltaP `15.5516` edge `0.3503` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4956` n `142` status `ready` deltaP `13.4533` edge `0.058` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.3112` n `142` status `ready` deltaP `5.5758` edge `0.0941` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0742` n `142` status `ready` deltaP `3.7489` edge `0.0149` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1379` n `142` status `ready` deltaP `4.7063` edge `0.0951` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.2714` n `142` status `ready` deltaP `4.3308` edge `0.0216` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.6015` n `142` status `ready` deltaP `-0.5819` edge `0.0021` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6149` n `142` status `ready` deltaP `-1.4358` edge `0.0027` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.657` n `142` status `ready` deltaP `4.7968` edge `0.0598` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.6845` n `142` status `ready` deltaP `-1.4021` edge `0.0356` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.7026` n `142` status `ready` deltaP `-0.7654` edge `-0.0004` maxDD `-3.0996`
- `market_context_high->crypto_alt_4h` score `-0.7299` n `142` status `ready` deltaP `14.0329` edge `0.2797` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.7502` n `142` status `ready` deltaP `4.9739` edge `0.0576` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1072` n `142` status `ready` deltaP `3.8195` edge `0.0246` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.1955` n `142` status `ready` deltaP `-4.0579` edge `0.0053` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3423` n `142` status `ready` deltaP `-1.8852` edge `-0.0121` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
