# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T08:37:26.266574+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4082`

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

- `news_risk_high->equity_4h` score `1.3086` n `62` status `ready` deltaP `12.4459` edge `0.1587` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7409` n `62` status `ready` deltaP `13.2327` edge `0.0213` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2976` n `62` status `ready` deltaP `9.235` edge `0.1434` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1713` n `62` status `ready` deltaP `-1.3553` edge `0.0675` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0699` n `62` status `ready` deltaP `7.6492` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0947` n `62` status `ready` deltaP `-0.5988` edge `0.0468` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.116` n `62` status `ready` deltaP `3.1582` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2199` n `62` status `ready` deltaP `1.8145` edge `0.0043` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5719` n `62` status `ready` deltaP `-4.5731` edge `-0.0071` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0061` n `62` status `ready` deltaP `0.354` edge `-0.0408` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2545` n `62` status `ready` deltaP `-2.8926` edge `-0.026` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.332` n `62` status `ready` deltaP `-3.7716` edge `0.0148` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5979` n `62` status `ready` deltaP `-11.1744` edge `-0.0027` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-2.0254` n `62` status `ready` deltaP `-8.3301` edge `-0.0315` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2835` n `62` status `ready` deltaP `-3.6192` edge `-0.0066` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8357` n `62` status `ready` deltaP `-5.9476` edge `-0.2625` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5287` n `62` status `ready` deltaP `-31.2795` edge `-0.0117` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.9315` n `62` status `ready` deltaP `20.5197` edge `0.3896` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.575` n `62` status `ready` deltaP `-28.4442` edge `-0.1256` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5675` n `62` status `ready` deltaP `-31.4908` edge `-0.1537` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
