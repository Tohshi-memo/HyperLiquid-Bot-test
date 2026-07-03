# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T01:07:30.361702+00:00`
- Price records: `672`
- Market context records: `5510`
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

- `market_context_high->crypto_major_24h` score `2.772` n `190` status `ready` deltaP `16.2189` edge `0.5769` maxDD `-29.6555`
- `market_context_high->equity_24h` score `2.6893` n `190` status `ready` deltaP `11.4456` edge `0.6557` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.4099` n `193` status `ready` deltaP `14.0362` edge `0.3365` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.1466` n `193` status `ready` deltaP `11.0775` edge `0.2689` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8817` n `193` status `ready` deltaP `9.4938` edge `0.2576` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.4644` n `193` status `ready` deltaP `8.4337` edge `0.079` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3838` n `190` status `ready` deltaP `12.9312` edge `0.0385` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1212` n `193` status `ready` deltaP `6.396` edge `0.0168` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3371` n `193` status `ready` deltaP `0.9843` edge `0.0615` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3572` n `193` status `ready` deltaP `0.4778` edge `-0.0001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4715` n `193` status `ready` deltaP `2.5736` edge `0.0681` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6134` n `193` status `ready` deltaP `0.9153` edge `0.0103` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8236` n `193` status `ready` deltaP `3.5187` edge `0.006` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.9911` n `193` status `ready` deltaP `5.9894` edge `0.0384` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5123` n `193` status `ready` deltaP `-3.2756` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8232` n `190` status `ready` deltaP `14.2708` edge `0.0698` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9598` n `193` status `ready` deltaP `-11.4756` edge `-0.0505` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5503` n `193` status `ready` deltaP `-8.7909` edge `-0.0533` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.3009` n `190` status `ready` deltaP `-4.2379` edge `-0.17` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3022` n `190` status `ready` deltaP `7.2442` edge `0.2129` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
