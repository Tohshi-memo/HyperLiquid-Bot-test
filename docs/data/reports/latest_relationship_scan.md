# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T09:52:25.105025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3905`

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

- `news_risk_high->equity_4h` score `1.2968` n `62` status `ready` deltaP `12.2934` edge `0.1582` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6763` n `62` status `ready` deltaP `12.4705` edge `0.021` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3149` n `62` status `ready` deltaP `9.5822` edge `0.1433` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1122` n `62` status `ready` deltaP `-2.0498` edge `0.0672` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0544` n `62` status `ready` deltaP `7.3498` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0986` n `62` status `ready` deltaP `-0.5988` edge `0.0463` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1324` n `62` status `ready` deltaP `2.8588` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2032` n `62` status `ready` deltaP `2.1194` edge `0.0044` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5478` n `62` status `ready` deltaP `-4.124` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9641` n `62` status `ready` deltaP `1.1162` edge `-0.0405` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1946` n `62` status `ready` deltaP `-2.1441` edge `-0.0233` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2974` n `62` status `ready` deltaP `-3.4667` edge `0.0172` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6086` n `62` status `ready` deltaP `-11.3241` edge `-0.0026` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9858` n `62` status `ready` deltaP `-8.0307` edge `-0.0302` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2002` n `62` status `ready` deltaP `-2.857` edge `-0.001` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.7918` n `62` status `ready` deltaP `-5.2532` edge `-0.2615` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5311` n `62` status `ready` deltaP `-31.2795` edge `-0.0119` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8771` n `62` status `ready` deltaP `21.0405` edge `0.3931` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6287` n `62` status `ready` deltaP `-28.9651` edge `-0.1266` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.4455` n `62` status `ready` deltaP `-30.97` edge `-0.147` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
