# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T15:07:39.722097+00:00`
- Price records: `672`
- Market context records: `5890`
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

- `news_risk_high->fx_4h` score `3.7107` n `30` status `ready` deltaP `38.628` edge `0.0563` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0621` n `30` status `ready` deltaP `24.98` edge `0.0192` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9494` n `30` status `ready` deltaP `11.5369` edge `0.0915` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8838` n `225` status `ready` deltaP `7.2412` edge `0.1354` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2606` n `30` status `ready` deltaP `5.1697` edge `0.0451` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2235` n `228` status `ready` deltaP `4.7957` edge `0.032` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3079` n `228` status `ready` deltaP `3.3171` edge `0.0055` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4352` n `30` status `ready` deltaP `1.3872` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5556` n `228` status `ready` deltaP `-1.7019` edge `-0.0028` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5646` n `228` status `ready` deltaP `3.4668` edge `0.0366` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6056` n `228` status `ready` deltaP `0.5148` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.6405` n `228` status `ready` deltaP `2.4504` edge `0.035` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8198` n `228` status `ready` deltaP `-2.7393` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2712` n `30` status `ready` deltaP `-12.994` edge `-0.0249` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.739` n `225` status `ready` deltaP `8.8943` edge `0.155` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.8102` n `30` status `ready` deltaP `-13.7296` edge `-0.053` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.9634` n `221` status `ready` deltaP `3.0873` edge `0.0095` maxDD `-5.5435`
- `market_context_high->index_4h` score `-2.0067` n `225` status `ready` deltaP `-1.3042` edge `0.0102` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.2946` n `30` status `ready` deltaP `-16.8598` edge `-0.0784` maxDD `-2.9371`
- `market_context_high->equity_24h` score `-2.3021` n `221` status `ready` deltaP `10.6979` edge `0.1456` maxDD `-31.6316`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
