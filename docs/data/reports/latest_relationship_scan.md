# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T02:22:27.577332+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7284`

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

- `market_context_high->unknown_4h` score `54.7437` n `95` status `ready` deltaP `0.8408` edge `4.5899` maxDD `-1.016`
- `market_context_high->unknown_1h` score `2.5127` n `107` status `ready` deltaP `2.1574` edge `0.2439` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.5294` n `49` status `ready` deltaP `20.2133` edge `0.0836` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.3663` n `95` status `ready` deltaP `6.5885` edge `0.047` maxDD `-1.165`
- `market_context_high->fx_1h` score `-0.3307` n `107` status `ready` deltaP `-1.3977` edge `0.0024` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.357` n `107` status `ready` deltaP `1.5474` edge `0.01` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6677` n `107` status `ready` deltaP `-1.9965` edge `-0.0071` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.6694` n `95` status `ready` deltaP `-4.4977` edge `0.0042` maxDD `-0.4691`
- `market_context_high->metal_1h` score `-0.9237` n `107` status `ready` deltaP `1.1836` edge `-0.0055` maxDD `-1.6824`
- `market_context_high->fx_24h` score `-1.0776` n `49` status `ready` deltaP `-1.6369` edge `-0.0002` maxDD `-1.2952`
- `market_context_high->crypto_major_24h` score `-1.1808` n `49` status `ready` deltaP `5.7115` edge `0.0196` maxDD `-12.0583`
- `market_context_high->crypto_major_1h` score `-1.252` n `107` status `ready` deltaP `3.8293` edge `-0.024` maxDD `-9.63`
- `market_context_high->equity_1h` score `-2.5325` n `107` status `ready` deltaP `-0.3498` edge `-0.0921` maxDD `-12.4203`
- `market_context_high->metal_4h` score `-2.8615` n `95` status `ready` deltaP `-4.7016` edge `-0.03` maxDD `-5.8357`
- `market_context_high->metal_24h` score `-2.9819` n `49` status `ready` deltaP `-9.1943` edge `-0.0018` maxDD `-6.8318`
- `market_context_high->crypto_alt_1h` score `-3.1758` n `107` status `ready` deltaP `-0.277` edge `-0.0584` maxDD `-13.3524`
- `market_context_high->crypto_alt_24h` score `-3.8473` n `49` status `ready` deltaP `8.879` edge `-0.0365` maxDD `-35.942`
- `market_context_high->index_4h` score `-4.3977` n `95` status `ready` deltaP `-18.0728` edge `-0.0501` maxDD `-5.0046`
- `market_context_high->index_24h` score `-7.3396` n `49` status `ready` deltaP `-36.756` edge `-0.1838` maxDD `-6.2903`
- `market_context_high->crypto_major_4h` score `-11.7117` n `95` status `ready` deltaP `-18.2252` edge `-0.2737` maxDD `-39.7952`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
