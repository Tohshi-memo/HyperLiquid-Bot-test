# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T15:22:35.650420+00:00`
- Price records: `672`
- Market context records: `5891`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10264`

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

- `news_risk_high->fx_4h` score `3.6973` n `30` status `ready` deltaP `38.4756` edge `0.0562` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0753` n `30` status `ready` deltaP `25.1297` edge `0.0193` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9455` n `30` status `ready` deltaP `11.5369` edge `0.091` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8322` n `225` status `ready` deltaP `7.2412` edge `0.1311` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2606` n `30` status `ready` deltaP `5.1697` edge `0.0451` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2431` n `227` status `ready` deltaP `4.7792` edge `0.0296` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.303` n `227` status `ready` deltaP `3.4108` edge `0.0055` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4437` n `30` status `ready` deltaP `1.2375` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5626` n `227` status `ready` deltaP `-1.7898` edge `-0.0031` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5897` n `227` status `ready` deltaP `3.2697` edge `0.0347` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.61` n `227` status `ready` deltaP `0.4597` edge `0.0035` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.669` n `227` status `ready` deltaP `2.2475` edge `0.0327` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8258` n `227` status `ready` deltaP `-2.8292` edge `-0.0011` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2611` n `30` status `ready` deltaP `-12.8443` edge `-0.0246` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8118` n `30` status `ready` deltaP `-13.7296` edge `-0.0532` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.8275` n `225` status `ready` deltaP `8.6023` edge `0.1456` maxDD `-25.6458`
- `market_context_high->fx_24h` score `-1.9834` n `220` status `ready` deltaP `2.8219` edge `0.0087` maxDD `-5.5435`
- `market_context_high->index_4h` score `-2.0115` n `225` status `ready` deltaP `-1.3042` edge `0.0098` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.293` n `30` status `ready` deltaP `-16.8598` edge `-0.0782` maxDD `-2.9371`
- `market_context_high->equity_24h` score `-2.3447` n `220` status `ready` deltaP `10.7481` edge `0.1398` maxDD `-31.6316`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
