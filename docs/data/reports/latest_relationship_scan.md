# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T22:07:31.976051+00:00`
- Price records: `672`
- Market context records: `5708`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.8775` n `266` status `ready` deltaP `11.5922` edge `0.2163` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0442` n `216` status `ready` deltaP `16.8403` edge `0.5295` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.7374` n `266` status `ready` deltaP `8.8586` edge `0.1633` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1683` n `266` status `ready` deltaP `6.674` edge `0.1334` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2372` n `278` status `ready` deltaP `2.518` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.3301` n `278` status `ready` deltaP `4.1378` edge `0.0405` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4244` n `278` status `ready` deltaP `2.0107` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4996` n `278` status `ready` deltaP `2.252` edge `0.0377` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5516` n `278` status `ready` deltaP `3.9342` edge `0.0285` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6312` n `278` status `ready` deltaP `0.2725` edge `0.0041` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.1066` n `216` status `ready` deltaP `10.9954` edge `0.0421` maxDD `-3.5823`
- `market_context_high->commodity_1h` score `-1.1139` n `278` status `ready` deltaP `-1.231` edge `-0.0039` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.2479` n `266` status `ready` deltaP `-0.204` edge `0.0101` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2698` n `266` status `ready` deltaP `2.2556` edge `0.0056` maxDD `-1.3415`
- `market_context_high->metal_4h` score `-2.6477` n `266` status `ready` deltaP `-7.7228` edge `-0.0504` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8926` n `216` status `ready` deltaP `1.9676` edge `0.0305` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.9119` n `266` status `ready` deltaP `-4.2958` edge `-0.0298` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4347` n `216` status `ready` deltaP `5.9607` edge `0.0364` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9275` n `216` status `ready` deltaP `-7.1759` edge `-0.2409` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.085` n `216` status `ready` deltaP `-11.0532` edge `-0.0725` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
