# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T05:22:30.115917+00:00`
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

- `news_risk_high->equity_4h` score `1.2193` n `64` status `ready` deltaP `10.9375` edge `0.1573` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.9511` n `64` status `ready` deltaP `15.8155` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.4178` n `64` status `ready` deltaP `11.1111` edge `0.1463` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.1594` n `64` status `ready` deltaP `9.3095` edge `0.0037` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.0546` n `64` status `ready` deltaP `-2.0833` edge `0.0627` maxDD `-0.2073`
- `news_risk_high->equity_1h` score `-0.0298` n `64` status `ready` deltaP `0.5146` edge `0.0477` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2005` n `64` status `ready` deltaP `1.6093` edge `0.0021` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2508` n `64` status `ready` deltaP `1.2957` edge `0.0038` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5072` n `64` status `ready` deltaP `-3.3589` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.1628` n `64` status `ready` deltaP `-2.6296` edge `-0.041` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.3553` n `64` status `ready` deltaP `-3.7051` edge `-0.0335` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.4275` n `64` status `ready` deltaP `-4.5732` edge `0.0079` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.7024` n `64` status `ready` deltaP `-11.8357` edge `-0.0024` maxDD `-1.1781`
- `news_risk_high->crypto_major_1h` score `-1.8789` n `64` status `ready` deltaP `-7.4289` edge `-0.0253` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.4192` n `64` status `ready` deltaP `-4.878` edge `-0.0156` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.7078` n `64` status `ready` deltaP `-4.6875` edge `-0.2545` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-4.4251` n `64` status `ready` deltaP `21.5278` edge `0.4478` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.4523` n `64` status `ready` deltaP `-30.5259` edge `-0.0103` maxDD `-3.9106`
- `news_risk_high->commodity_24h` score `-10.5365` n `64` status `ready` deltaP `-29.1667` edge `-0.1171` maxDD `-27.9862`
- `news_risk_high->crypto_major_24h` score `-13.9014` n `64` status `ready` deltaP `-28.8194` edge `-0.116` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
