# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T10:07:32.315646+00:00`
- Price records: `672`
- Market context records: `7017`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2845` n `226` status `ready` deltaP `1.6533` edge `0.001` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.4868` n `213` status `ready` deltaP `-6.0299` edge `0.4328` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.5941` n `226` status `ready` deltaP `1.2943` edge `0.0283` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6748` n `226` status `ready` deltaP `-1.5341` edge `0.0005` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6851` n `226` status `ready` deltaP `0.3722` edge `0.0008` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7182` n `226` status `ready` deltaP `2.9344` edge `0.0236` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-1.0523` n `226` status `ready` deltaP `9.8492` edge `0.0058` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2646` n `226` status `ready` deltaP `-2.525` edge `-0.0164` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2763` n `226` status `ready` deltaP `-2.0031` edge `-0.0029` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.7035` n `226` status `ready` deltaP `-4.588` edge `-0.0397` maxDD `-5.5157`
- `market_context_high->index_4h` score `-1.7978` n `226` status `ready` deltaP `7.5626` edge `-0.011` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8769` n `226` status `ready` deltaP `3.463` edge `-0.0083` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.903` n `226` status `ready` deltaP `6.5617` edge `0.0106` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.4024` n `226` status `ready` deltaP `-5.8723` edge `0.0719` maxDD `-9.9695`
- `market_context_high->crypto_alt_4h` score `-2.7387` n `226` status `ready` deltaP `1.2937` edge `0.0188` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.9055` n `213` status `ready` deltaP `-4.2963` edge `-0.0826` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.1479` n `213` status `ready` deltaP `-5.4186` edge `-0.0153` maxDD `-4.8722`
- `market_context_high->crypto_major_4h` score `-4.8741` n `226` status `ready` deltaP `1.7065` edge `0.0109` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.4906` n `226` status `ready` deltaP `4.5543` edge `-0.0662` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.4162` n `213` status `ready` deltaP `-9.9423` edge `-0.0548` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
