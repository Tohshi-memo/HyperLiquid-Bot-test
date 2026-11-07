# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T06:22:30.270583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.3229` n `62` status `ready` deltaP `12.7508` edge `0.1585` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8542` n `62` status `ready` deltaP `14.6046` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3579` n `62` status `ready` deltaP `9.9294` edge `0.1465` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.2003` n `62` status `ready` deltaP `-1.0081` edge `0.0676` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.1104` n `62` status `ready` deltaP `8.3977` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.09` n `62` status `ready` deltaP `-0.5988` edge `0.0474` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1643` n `62` status `ready` deltaP `2.26` edge `0.0024` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2872` n `62` status `ready` deltaP `0.595` edge `0.0038` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5641` n `62` status `ready` deltaP `-4.4234` edge `-0.0071` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0639` n `62` status `ready` deltaP `-0.713` edge `-0.0411` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2281` n `62` status `ready` deltaP `-2.5932` edge `-0.0246` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2784` n `62` status `ready` deltaP `-3.1619` edge `0.0176` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5559` n `62` status `ready` deltaP `-10.7253` edge `-0.0022` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9583` n `62` status `ready` deltaP `-7.881` edge `-0.0289` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2482` n `62` status `ready` deltaP `-3.3143` edge `-0.0041` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8201` n `62` status `ready` deltaP `-5.9476` edge `-0.2605` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5165` n `62` status `ready` deltaP `-31.1271` edge `-0.0117` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8168` n `62` status `ready` deltaP `20.5197` edge `0.4043` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6551` n `62` status `ready` deltaP `-28.9651` edge `-0.1288` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5303` n `62` status `ready` deltaP `-31.4908` edge `-0.1506` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
