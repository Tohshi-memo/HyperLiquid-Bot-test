# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T10:07:26.395494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4713`

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

- `market_context_high->unknown_4h` score `117.1726` n `37` status `ready` deltaP `-3.9387` edge `9.8354` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.27` n `37` status `ready` deltaP `10.5074` edge `0.2484` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1449` n `37` status `ready` deltaP `33.9239` edge `0.0449` maxDD `-0.0521`
- `market_context_high->equity_24h` score `2.5771` n `32` status `ready` deltaP `7.8125` edge `0.7078` maxDD `-31.3588`
- `market_context_high->index_4h` score `2.067` n `37` status `ready` deltaP `26.9652` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_4h` score `1.8673` n `43` status `ready` deltaP `23.0502` edge `0.0147` maxDD `-0.0211`
- `news_risk_high->fx_24h` score `1.1317` n `40` status `ready` deltaP `4.8611` edge `0.084` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.825` n `37` status `ready` deltaP `10.0502` edge `0.0603` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.548` n `37` status `ready` deltaP `12.146` edge `0.0708` maxDD `-3.1881`
- `market_context_high->index_24h` score `0.4715` n `32` status `ready` deltaP `5.2083` edge `0.0888` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.3865` n `32` status `ready` deltaP `7.9861` edge `-0.0122` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.3727` n `37` status `ready` deltaP `6.4736` edge `0.015` maxDD `-0.1681`
- `news_risk_high->fx_1h` score `0.3659` n `43` status `ready` deltaP `9.4277` edge `0.0056` maxDD `-0.0567`
- `market_context_high->index_1h` score `0.3476` n `37` status `ready` deltaP `2.549` edge `0.039` maxDD `-0.1621`
- `news_risk_high->equity_4h` score `0.3326` n `43` status `ready` deltaP `-0.8969` edge `0.1076` maxDD `-4.2454`
- `market_context_high->commodity_24h` score `0.257` n `32` status `ready` deltaP `1.0417` edge `0.1455` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->index_4h` score `-0.0075` n `43` status `ready` deltaP `4.0236` edge `0.0201` maxDD `-0.4975`
- `market_context_high->commodity_4h` score `-0.0425` n `37` status `ready` deltaP `2.5297` edge `0.0231` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0793` n `37` status `ready` deltaP `0.9023` edge `0.0166` maxDD `-0.6226`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
