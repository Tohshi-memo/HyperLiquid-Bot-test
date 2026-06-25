# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T09:07:32.129770+00:00`
- Price records: `672`
- Market context records: `4709`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9644`

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

- `market_context_high->unknown_1h` score `76.9136` n `144` status `ready` deltaP `13.7143` edge `6.3598` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1755` n `140` status `ready` deltaP `12.7701` edge `0.4672` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.7643` n `135` status `ready` deltaP `14.4445` edge `0.2264` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3061` n `144` status `ready` deltaP `2.4077` edge `0.0243` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6679` n `140` status `ready` deltaP `5.257` edge `-0.0084` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9722` n `140` status `ready` deltaP `-2.0558` edge `-0.0027` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-1.0498` n `140` status `ready` deltaP `7.6612` edge `0.0251` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.1712` n `140` status `ready` deltaP `2.1994` edge `0.0121` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1822` n `144` status `ready` deltaP `-1.5926` edge `0.0108` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2948` n `144` status `ready` deltaP `-5.1356` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6445` n `144` status `ready` deltaP `-3.9338` edge `-0.0104` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2478` n `144` status `ready` deltaP `-1.3889` edge `-0.0784` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.7628` n `144` status `ready` deltaP `-1.7299` edge `-0.0956` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.4197` n `135` status `ready` deltaP `16.7592` edge `0.0704` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4593` n `144` status `ready` deltaP `-5.6263` edge `-0.0773` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7937` n `135` status `ready` deltaP `-13.044` edge `-0.0165` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.096` n `140` status `ready` deltaP `-1.79` edge `-0.1603` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.3999` n `135` status `ready` deltaP `-10.6366` edge `-0.0916` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.7698` n `140` status `ready` deltaP `2.3563` edge `-0.2547` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.9574` n `140` status `ready` deltaP `-2.1994` edge `-0.3001` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
