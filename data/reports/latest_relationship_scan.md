# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T04:52:25.526658+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10656`

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

- `risk_on_high->unknown_4h` score `19.5384` n `133` status `ready` deltaP `7.4741` edge `1.6402` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5384` n `133` status `ready` deltaP `7.4741` edge `1.6402` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.0408` n `217` status `ready` deltaP `7.9107` edge `0.7702` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `7.4027` n `37` status `ready` deltaP `25.1783` edge `0.476` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3424` n `37` status `ready` deltaP `25.0` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8424` n `37` status `ready` deltaP `17.6376` edge `0.2439` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1798` n `37` status `ready` deltaP `21.8647` edge `0.058` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7875` n `37` status `ready` deltaP `10.0569` edge `0.102` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6698` n `37` status `ready` deltaP `13.9829` edge `0.085` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.4136` n `37` status `ready` deltaP `7.8128` edge `0.084` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2868` n `37` status `ready` deltaP `16.0706` edge `0.0135` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.2215` n `37` status `ready` deltaP `14.5655` edge `0.024` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `1.1108` n `37` status `ready` deltaP `9.7751` edge `0.0539` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `1.0572` n `37` status `ready` deltaP `8.3801` edge `0.0651` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.1618` n `37` status `ready` deltaP `11.7961` edge `0.0364` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0874` n `136` status `ready` deltaP `12.2006` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0874` n `136` status `ready` deltaP `12.2006` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0247` n `37` status `ready` deltaP `5.7251` edge `0.0033` maxDD `-0.9036`
- `news_risk_high->crypto_major_24h` score `-0.1359` n `37` status `ready` deltaP `11.3692` edge `0.1844` maxDD `-18.2098`
- `risk_on_high->index_1h` score `-0.187` n `136` status `ready` deltaP `3.6501` edge `-0.0036` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
