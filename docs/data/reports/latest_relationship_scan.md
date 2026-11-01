# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T06:22:27.392346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6341`

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

- `market_context_high->unknown_24h` score `6742.7221` n `57` status `ready` deltaP `4.8611` edge `561.8611` maxDD `0.0`
- `market_context_high->unknown_4h` score `354.4926` n `57` status `ready` deltaP `5.4102` edge `29.5093` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `80.2552` n `108` status `ready` deltaP `-5.1951` edge `6.7512` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `40.6547` n `57` status `ready` deltaP `2.7971` edge `3.3803` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.8485` n `57` status `ready` deltaP `43.5215` edge `1.475` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2838` n `98` status `ready` deltaP `31.2004` edge `1.0346` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.8589` n `57` status `ready` deltaP `57.2551` edge `0.1993` maxDD `-0.0877`
- `market_context_high->commodity_24h` score `6.1585` n `57` status `ready` deltaP `43.549` edge `0.2589` maxDD `-1.2149`
- `market_context_high->crypto_alt_4h` score `5.1376` n `57` status `ready` deltaP `21.0954` edge `0.3217` maxDD `-1.7361`
- `news_risk_high->crypto_alt_4h` score `4.9977` n `108` status `ready` deltaP `18.9024` edge `0.4291` maxDD `-7.4246`
- `market_context_high->crypto_major_4h` score `4.9327` n `57` status `ready` deltaP `27.9579` edge `0.2583` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.0882` n `57` status `ready` deltaP `4.4636` edge `0.2978` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.0542` n `57` status `ready` deltaP `29.3271` edge `0.0924` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.3662` n `57` status `ready` deltaP `10.1882` edge `0.3031` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7587` n `57` status `ready` deltaP `-5.3911` edge `0.4132` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.659` n `57` status `ready` deltaP `19.7155` edge `0.0493` maxDD `-0.7323`
- `market_context_high->crypto_major_1h` score `1.2814` n `57` status `ready` deltaP `7.745` edge `0.1175` maxDD `-2.3215`
- `market_context_high->equity_1h` score `1.2294` n `57` status `ready` deltaP `0.4281` edge `0.1521` maxDD `-1.5336`
- `market_context_high->metal_1h` score `0.981` n `57` status `ready` deltaP `12.194` edge `0.0253` maxDD `-0.3209`
- `market_context_high->crypto_alt_1h` score `0.915` n `57` status `ready` deltaP `2.2245` edge `0.1421` maxDD `-2.7875`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
