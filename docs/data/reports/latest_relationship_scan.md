# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T04:52:26.587636+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4184`

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

- `news_risk_high->equity_4h` score `1.1163` n `66` status `ready` deltaP `9.2433` edge `0.1554` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7944` n `66` status `ready` deltaP `13.932` edge `0.0211` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3158` n `66` status `ready` deltaP `9.375` edge `0.1448` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0815` n `66` status `ready` deltaP `7.857` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.0572` n `66` status `ready` deltaP `-1.4363` edge `0.0586` maxDD `-0.2073`
- `news_risk_high->equity_1h` score `-0.1142` n `66` status `ready` deltaP `-0.8982` edge `0.0463` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.1962` n `66` status `ready` deltaP `2.3744` edge `0.0036` maxDD `-0.2336`
- `news_risk_high->fx_1h` score `-0.2922` n `66` status `ready` deltaP `-0.0952` edge `0.0017` maxDD `-0.0826`
- `news_risk_high->metal_1h` score `-0.4322` n `66` status `ready` deltaP `-1.9461` edge `-0.0067` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2474` n `66` status `ready` deltaP `-4.2868` edge `-0.0408` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.583` n `66` status `ready` deltaP `-5.899` edge `-0.0032` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.8883` n `66` status `ready` deltaP `-12.72` edge `-0.0028` maxDD `-1.2475`
- `news_risk_high->crypto_major_1h` score `-2.0676` n `66` status `ready` deltaP `-8.5103` edge `-0.0302` maxDD `-3.4957`
- `news_risk_high->crypto_alt_1h` score `-2.3064` n `66` status `ready` deltaP `-4.7315` edge `-0.0451` maxDD `-5.2444`
- `news_risk_high->crypto_alt_4h` score `-2.6254` n `66` status `ready` deltaP `-6.2038` edge `-0.0332` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.6088` n `66` status `ready` deltaP `-3.5038` edge `-0.2497` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-4.12` n `66` status `ready` deltaP `22.4748` edge `0.4806` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5137` n `66` status `ready` deltaP `-31.0467` edge `-0.0105` maxDD `-4.0262`
- `news_risk_high->commodity_24h` score `-10.4175` n `66` status `ready` deltaP `-29.3561` edge `-0.1052` maxDD `-28.0438`
- `news_risk_high->crypto_major_24h` score `-13.6717` n `66` status `ready` deltaP `-28.993` edge `-0.0957` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
