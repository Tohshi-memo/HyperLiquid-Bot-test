# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T21:52:29.209066+00:00`
- Price records: `672`
- Market context records: `5496`
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

- `market_context_high->crypto_major_24h` score `3.2064` n `190` status `ready` deltaP `16.2189` edge `0.6131` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.8114` n `193` status `ready` deltaP `12.9068` edge `0.3121` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.6869` n `193` status `ready` deltaP `14.7984` edge `0.3545` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2819` n `193` status `ready` deltaP `10.8658` edge `0.2818` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.1081` n `190` status `ready` deltaP `10.7511` edge `0.6119` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.5723` n `193` status `ready` deltaP `9.0325` edge `0.084` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.288` n `190` status `ready` deltaP `12.0632` edge `0.0363` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1811` n `193` status `ready` deltaP `6.9948` edge `0.0178` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.276` n `193` status `ready` deltaP `1.2837` edge `0.0646` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3626` n `193` status `ready` deltaP `0.3281` edge `0.0002` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4115` n `193` status `ready` deltaP `2.873` edge `0.0711` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.4852` n `193` status `ready` deltaP `2.1129` edge `0.013` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.7284` n `193` status `ready` deltaP `7.8186` edge `0.0481` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8066` n `193` status `ready` deltaP `3.6712` edge `0.0064` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5602` n `193` status `ready` deltaP `-3.8744` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7787` n `190` status `ready` deltaP `14.2708` edge `0.0755` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.76` n `193` status `ready` deltaP `-9.4938` edge `-0.0381` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4058` n `193` status `ready` deltaP `-7.419` edge `-0.0504` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1438` n `190` status `ready` deltaP `7.2442` edge `0.2261` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.258` n `190` status `ready` deltaP `-4.2379` edge `-0.1645` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
