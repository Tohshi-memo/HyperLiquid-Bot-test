# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T22:07:26.294449+00:00`
- Price records: `672`
- Market context records: `5497`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->crypto_major_24h` score `3.1944` n `190` status `ready` deltaP `16.2189` edge `0.6121` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.7716` n `193` status `ready` deltaP `12.7543` edge `0.3098` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.6845` n `193` status `ready` deltaP `14.7984` edge `0.3543` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2711` n `193` status `ready` deltaP `10.8658` edge `0.2809` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.1513` n `190` status `ready` deltaP `10.7511` edge `0.6155` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.5711` n `193` status `ready` deltaP `9.0325` edge `0.0839` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3042` n `190` status `ready` deltaP `12.2368` edge `0.0365` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1811` n `193` status `ready` deltaP `6.9948` edge `0.0178` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2915` n `193` status `ready` deltaP `1.134` edge `0.0643` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3704` n `193` status `ready` deltaP `0.1784` edge `0.0002` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4079` n `193` status `ready` deltaP `2.873` edge `0.0714` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.4852` n `193` status `ready` deltaP `2.1129` edge `0.013` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.7466` n `193` status `ready` deltaP `7.6662` edge `0.0476` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8054` n `193` status `ready` deltaP `3.6712` edge `0.0065` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5602` n `193` status `ready` deltaP `-3.8744` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7811` n `190` status `ready` deltaP `14.2708` edge `0.0752` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.7726` n `193` status `ready` deltaP `-9.6463` edge `-0.0387` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4204` n `193` status `ready` deltaP `-7.5714` edge `-0.0506` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1426` n `190` status `ready` deltaP `7.2442` edge `0.2262` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2619` n `190` status `ready` deltaP `-4.2379` edge `-0.165` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
