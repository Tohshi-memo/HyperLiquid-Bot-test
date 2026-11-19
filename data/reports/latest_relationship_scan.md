# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T06:52:24.191063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2636`

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

- `market_context_high->unknown_1h` score `11504.463` n `112` status `ready` deltaP `0.9678` edge `958.7186` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `8105.1517` n `101` status `ready` deltaP `-0.1464` edge `675.4587` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.7258` n `98` status `ready` deltaP `39.594` edge `1.6946` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.7318` n `98` status `ready` deltaP `23.2249` edge `1.4334` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2329` n `98` status `ready` deltaP `15.3557` edge `0.2007` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.2334` n `112` status `ready` deltaP `3.4431` edge `0.0136` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.6574` n `101` status `ready` deltaP `10.864` edge `0.0038` maxDD `-6.1475`
- `market_context_high->index_1h` score `-0.7785` n `112` status `ready` deltaP `-0.7218` edge `0.0037` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8023` n `112` status `ready` deltaP `2.8443` edge `0.0649` maxDD `-10.2705`
- `market_context_high->crypto_alt_4h` score `-0.9659` n `101` status `ready` deltaP `-1.0233` edge `0.164` maxDD `-17.1476`
- `market_context_high->crypto_alt_1h` score `-1.0143` n `112` status `ready` deltaP `-1.3259` edge `0.0291` maxDD `-7.6911`
- `market_context_high->crypto_major_4h` score `-1.0592` n `101` status `ready` deltaP `-3.3083` edge `0.2445` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.3818` n `112` status `ready` deltaP `-8.9019` edge `-0.0009` maxDD `-0.392`
- `market_context_high->commodity_1h` score `-2.5966` n `112` status `ready` deltaP `-12.0402` edge `-0.0283` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.6082` n `101` status `ready` deltaP `-9.5568` edge `-0.0193` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7264` n `112` status `ready` deltaP `1.358` edge `-0.0185` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.4114` n `101` status `ready` deltaP `-22.9534` edge `-0.0103` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6624` n `98` status `ready` deltaP `-18.1194` edge `-0.0035` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5689` n `101` status `ready` deltaP `-24.7857` edge `-0.1061` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1009` n `98` status `ready` deltaP `-16.4222` edge `-0.1067` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
