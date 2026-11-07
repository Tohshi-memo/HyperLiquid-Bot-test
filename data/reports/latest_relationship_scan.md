# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T06:07:30.580866+00:00`
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

- `news_risk_high->equity_4h` score `1.3214` n `62` status `ready` deltaP `12.7508` edge `0.1583` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8664` n `62` status `ready` deltaP `14.757` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.361` n `62` status `ready` deltaP `9.9294` edge `0.1469` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.184` n `62` status `ready` deltaP `-1.1817` edge `0.0674` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.1104` n `62` status `ready` deltaP `8.3977` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0908` n `62` status `ready` deltaP `-0.5988` edge `0.0473` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1721` n `62` status `ready` deltaP `2.1103` edge `0.0024` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2951` n `62` status `ready` deltaP `0.4425` edge `0.0038` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5719` n `62` status `ready` deltaP `-4.5731` edge `-0.0071` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0719` n `62` status `ready` deltaP `-0.8655` edge `-0.0411` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2413` n `62` status `ready` deltaP `-2.7429` edge `-0.0253` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2792` n `62` status `ready` deltaP `-3.1619` edge `0.0175` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5571` n `62` status `ready` deltaP `-10.7253` edge `-0.0023` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9559` n `62` status `ready` deltaP `-7.881` edge `-0.0287` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2615` n `62` status `ready` deltaP `-3.4667` edge `-0.0048` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8178` n `62` status `ready` deltaP `-5.9476` edge `-0.2602` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5299` n `62` status `ready` deltaP `-31.2795` edge `-0.0118` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8004` n `62` status `ready` deltaP `20.5197` edge `0.4064` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6611` n `62` status `ready` deltaP `-28.9651` edge `-0.1293` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5279` n `62` status `ready` deltaP `-31.4908` edge `-0.1504` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
