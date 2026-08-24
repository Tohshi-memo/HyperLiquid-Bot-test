# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T16:22:38.237905+00:00`
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

- `news_risk_high->unknown_24h` score `46.6285` n `51` status `ready` deltaP `14.2361` edge `3.7908` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.4575` n `51` status `ready` deltaP `40.237` edge `0.9463` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8677` n `51` status `ready` deltaP `24.1063` edge `0.9162` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4856` n `51` status `ready` deltaP `48.9481` edge `0.146` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.9674` n `84` status `ready` deltaP `8.2837` edge `0.388` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.111` n `51` status `ready` deltaP `27.995` edge `0.233` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5658` n `51` status `ready` deltaP `16.3349` edge `0.2187` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.326` n `51` status `ready` deltaP `39.1499` edge `0.0296` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6632` n `130` status `ready` deltaP `19.144` edge `0.0518` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0771` n `51` status `ready` deltaP `15.0735` edge `0.029` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0301` n `51` status `ready` deltaP `18.9415` edge `0.0422` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.8331` n `51` status `ready` deltaP `28.0739` edge `-0.1135` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.2726` edge `0.0056` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2327` n `51` status `ready` deltaP `8.8382` edge `-0.0087` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1317` n `130` status `ready` deltaP `11.0202` edge `-0.0166` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0229` n `130` status `ready` deltaP `10.9051` edge `-0.0259` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1154` n `51` status `ready` deltaP `2.1927` edge `-0.0071` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2943` n `51` status `ready` deltaP `6.1484` edge `-0.0124` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4155` n `130` status `ready` deltaP `2.8604` edge `0.0009` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
