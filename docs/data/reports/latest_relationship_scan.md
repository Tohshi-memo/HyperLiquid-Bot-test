# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T07:37:25.579356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.6758` n `51` status `ready` deltaP `11.6319` edge `3.8121` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.7306` n `53` status `ready` deltaP `22.6933` edge `0.8362` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.7138` n `51` status `ready` deltaP `31.5972` edge `0.5155` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.0965` n `51` status `ready` deltaP `29.9939` edge `0.4845` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0592` n `51` status `ready` deltaP `40.2676` edge `0.085` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7743` n `53` status `ready` deltaP `33.4388` edge `0.0217` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7531` n `53` status `ready` deltaP `15.5632` edge `0.1612` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4558` n `134` status `ready` deltaP `20.891` edge `0.1062` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7763` n `53` status `ready` deltaP `19.7365` edge `0.0935` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.4661` n `51` status `ready` deltaP `29.1156` edge `-0.0677` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `1.0714` n `136` status `ready` deltaP `11.637` edge `0.0566` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.0435` n `53` status `ready` deltaP `14.7215` edge `0.0058` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4793` n `53` status `ready` deltaP `13.2245` edge `0.0097` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4547` n `53` status `ready` deltaP `10.9762` edge `-0.004` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.0707` n `53` status `ready` deltaP `5.8991` edge `0.0063` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0628` n `53` status `ready` deltaP `3.9996` edge `0.0006` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4606` n `136` status `ready` deltaP `2.2631` edge `-0.0009` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.475` n `53` status `ready` deltaP `-0.7626` edge `-0.0119` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6885` n `53` status `ready` deltaP `3.2904` edge `-0.0262` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0451` n `53` status `ready` deltaP `-2.1255` edge `0.0035` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
