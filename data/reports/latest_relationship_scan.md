# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T07:22:25.117308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4153`

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

- `news_risk_high->equity_4h` score `1.3173` n `62` status `ready` deltaP `12.5983` edge `0.1588` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8043` n `62` status `ready` deltaP `13.9949` edge `0.0215` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3101` n `62` status `ready` deltaP `9.235` edge `0.145` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.2154` n `62` status `ready` deltaP `-0.8345` edge `0.0677` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0863` n `62` status `ready` deltaP `7.9486` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0636` n `62` status `ready` deltaP `-0.1497` edge `0.0478` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1402` n `62` status `ready` deltaP `2.7091` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2539` n `62` status `ready` deltaP `1.2047` edge `0.004` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5392` n `62` status `ready` deltaP `-3.9743` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0307` n `62` status `ready` deltaP `-0.1033` edge `-0.0409` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2117` n `62` status `ready` deltaP `-2.4435` edge `-0.0235` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2903` n `62` status `ready` deltaP `-3.3143` edge `0.0171` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5703` n `62` status `ready` deltaP `-10.875` edge `-0.0024` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9451` n `62` status `ready` deltaP `-7.7313` edge `-0.0288` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2418` n `62` status `ready` deltaP `-3.1619` edge `-0.0043` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8303` n `62` status `ready` deltaP `-5.9476` edge `-0.2618` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5129` n `62` status `ready` deltaP `-31.1271` edge `-0.0114` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8714` n `62` status `ready` deltaP `20.5197` edge `0.3973` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6045` n `62` status `ready` deltaP `-28.6178` edge `-0.1269` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5399` n `62` status `ready` deltaP `-31.4908` edge `-0.1514` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
