# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T01:22:24.662933+00:00`
- Price records: `672`
- Market context records: `5511`
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

- `market_context_high->equity_24h` score `2.7452` n `190` status `ready` deltaP `11.6192` edge `0.6592` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.7264` n `190` status `ready` deltaP `16.2189` edge `0.5731` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3845` n `193` status `ready` deltaP `13.8838` edge `0.3354` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.096` n `193` status `ready` deltaP `10.9251` edge `0.2657` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8491` n `193` status `ready` deltaP `9.3414` edge `0.2559` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.4212` n `193` status `ready` deltaP `8.284` edge `0.0764` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3862` n `190` status `ready` deltaP `12.9312` edge `0.0387` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.102` n `193` status `ready` deltaP `6.2463` edge `0.0162` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3564` n `193` status `ready` deltaP `0.4778` edge `0.0` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3959` n `193` status `ready` deltaP `0.8346` edge `0.0576` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5243` n `193` status `ready` deltaP `2.4239` edge `0.0647` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.641` n `193` status `ready` deltaP `0.7656` edge `0.009` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8236` n `193` status `ready` deltaP `3.5187` edge `0.006` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0129` n `193` status `ready` deltaP `5.8369` edge `0.0376` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5123` n `193` status `ready` deltaP `-3.2756` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8271` n `190` status `ready` deltaP `14.2708` edge `0.0693` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9802` n `193` status `ready` deltaP `-11.628` edge `-0.0521` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5539` n `193` status `ready` deltaP `-8.7909` edge `-0.0536` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.3087` n `190` status `ready` deltaP `-4.2379` edge `-0.171` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3202` n `190` status `ready` deltaP `7.2442` edge `0.2114` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
