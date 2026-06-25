# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T05:37:32.552802+00:00`
- Price records: `672`
- Market context records: `4694`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9760`

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

- `market_context_high->unknown_1h` score `78.7025` n `138` status `ready` deltaP `12.9003` edge `6.5143` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2132` n `135` status `ready` deltaP `10.9169` edge `0.4827` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2699` n `135` status `ready` deltaP `12.0139` edge `0.2014` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3462` n `138` status `ready` deltaP `1.7421` edge `0.0236` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7804` n `135` status `ready` deltaP `3.7692` edge `-0.0129` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9362` n `135` status `ready` deltaP `-1.4826` edge `-0.0019` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.1309` n `138` status `ready` deltaP `-4.977` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-1.1886` n `138` status `ready` deltaP `-1.8984` edge `0.0123` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2351` n `135` status `ready` deltaP `5.5511` edge `0.0154` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2638` n `135` status `ready` deltaP `1.3946` edge `0.0056` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6984` n `138` status `ready` deltaP `-4.4433` edge `-0.0115` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8309` n `138` status `ready` deltaP `-4.3544` edge `-0.0771` maxDD `-17.2107`
- `market_context_high->crypto_alt_1h` score `-3.37` n `138` status `ready` deltaP `-1.3234` edge `-0.0945` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-4.0995` n `138` status `ready` deltaP `-4.0484` edge `-0.1233` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.722` n `135` status `ready` deltaP `14.6759` edge `0.0591` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7678` n `135` status `ready` deltaP `-12.8704` edge `-0.0155` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.3963` n `135` status `ready` deltaP `-10.6366` edge `-0.0913` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6275` n `135` status `ready` deltaP `-3.1595` edge `-0.2193` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1307` n `135` status `ready` deltaP `-0.5488` edge `-0.2816` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6056` n `135` status `ready` deltaP `-3.5953` edge `-0.3739` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
