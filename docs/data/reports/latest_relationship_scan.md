# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T06:52:19.795149+00:00`
- Price records: `527`
- Market context records: `623`
- Flow alert records: `1762`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.216` n `146` status `ready` deltaP `7.4357` edge `0.3899` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `5.1911` n `146` status `ready` deltaP `14.9827` edge `0.3661` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.094` n `146` status `ready` deltaP `8.9095` edge `0.0157` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3245` n `146` status `ready` deltaP `1.936` edge `0.0033` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5808` n `146` status `ready` deltaP `1.7024` edge `0.0377` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.717` n `146` status `ready` deltaP `-0.5055` edge `-0.0032` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0594` n `146` status `ready` deltaP `-3.4574` edge `-0.0049` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1805` n `146` status `ready` deltaP `5.6838` edge `-0.0048` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3204` n `146` status `ready` deltaP `-2.6249` edge `-0.0115` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.7066` n `146` status `ready` deltaP `4.7945` edge `0.0828` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.7194` n `146` status `ready` deltaP `5.4781` edge `-0.0075` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2874` n `146` status `ready` deltaP `14.1879` edge `0.0854` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.3326` n `146` status `ready` deltaP `-1.0065` edge `-0.0354` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.8399` n `146` status `ready` deltaP `-7.9417` edge `0.0158` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2989` n `146` status `ready` deltaP `-3.5706` edge `-0.0359` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3542` n `146` status `ready` deltaP `-4.8129` edge `-0.0515` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6943` n `146` status `ready` deltaP `-6.3846` edge `0.0848` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.267` n `146` status `ready` deltaP `-2.3804` edge `-0.014` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6465` n `146` status `ready` deltaP `2.4462` edge `-0.2157` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.8164` n `146` status `ready` deltaP `-11.3086` edge `-0.0655` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
