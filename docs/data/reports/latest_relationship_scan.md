# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T13:37:25.744740+00:00`
- Price records: `672`
- Market context records: `8414`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6252.8734` n `52` status `ready` deltaP `40.2244` edge `520.8467` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.5006` n `52` status `ready` deltaP `24.5427` edge `0.4378` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.5358` n `52` status `ready` deltaP `19.6338` edge `0.1113` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.3299` n `52` status `ready` deltaP `19.8171` edge `0.0811` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6088` n `52` status `ready` deltaP `12.4597` edge `0.0944` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.528` n `52` status `ready` deltaP `6.6252` edge `0.2211` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.5007` n `52` status `ready` deltaP `10.813` edge `0.0927` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2369` n `52` status `ready` deltaP `15.6544` edge `0.1934` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.3077` n `52` status `ready` deltaP `4.28` edge `0.0439` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1327` n `52` status `ready` deltaP `6.2414` edge `0.0035` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.109` n `52` status `ready` deltaP `3.3971` edge `0.0153` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3618` n `52` status `ready` deltaP `1.0019` edge `0.0035` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4692` n `52` status `ready` deltaP `4.3504` edge `0.0066` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9369` n `52` status `ready` deltaP `-6.4717` edge `-0.0397` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7697` n `52` status `ready` deltaP `-27.7244` edge `-0.0638` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.3534` n `52` status `ready` deltaP `-33.1463` edge `-0.1981` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.3669` n `52` status `ready` deltaP `-25.9029` edge `-0.1938` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3671` n `52` status `ready` deltaP `-25.2938` edge `-0.3117` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4487` n `52` status `ready` deltaP `-11.9124` edge `-0.364` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.6194` n `52` status `ready` deltaP `-23.3841` edge `-0.9415` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
