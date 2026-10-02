# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T06:52:26.321193+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4890`

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

- `market_context_high->unknown_1h` score `340.5984` n `50` status `ready` deltaP `9.5269` edge `28.3246` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.6033` n `50` status `ready` deltaP `8.8415` edge `23.908` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.5112` n `60` status `ready` deltaP `39.0278` edge `0.8867` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0639` n `50` status `ready` deltaP `36.1667` edge `0.8225` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.129` n `60` status `ready` deltaP `36.875` edge `0.5634` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.6582` n `50` status `ready` deltaP `16.3611` edge `0.7834` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8209` n `50` status `ready` deltaP `17.5427` edge `0.5218` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8125` n `50` status `ready` deltaP `15.5793` edge `0.4265` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.4918` n `88` status `ready` deltaP `13.7611` edge `0.3336` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.1237` n `50` status `ready` deltaP `14.875` edge `0.4875` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9081` n `50` status `ready` deltaP `32.689` edge `0.0379` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8054` n `50` status `ready` deltaP `13.4551` edge `0.2104` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.7877` n `50` status `ready` deltaP `13.5509` edge `0.187` maxDD `-2.2692`
- `market_context_high->fx_1h` score `1.4627` n `50` status `ready` deltaP `20.491` edge `0.0117` maxDD `-0.113`
- `news_risk_high->equity_4h` score `1.2616` n `88` status `ready` deltaP `21.577` edge `0.0875` maxDD `-2.9013`
- `market_context_high->index_24h` score `1.0178` n `50` status `ready` deltaP `16.1806` edge `0.0797` maxDD `-1.2338`
- `news_risk_high->commodity_24h` score `0.9665` n `60` status `ready` deltaP `17.9861` edge `0.1164` maxDD `-3.9922`
- `news_risk_high->crypto_alt_1h` score `0.7346` n `100` status `ready` deltaP `5.4551` edge `0.0811` maxDD `-2.4998`
- `news_risk_high->fx_24h` score `0.5991` n `60` status `ready` deltaP `15.7639` edge `0.0261` maxDD `-0.3507`
- `market_context_high->fx_24h` score `0.5001` n `50` status `ready` deltaP `14.4306` edge `0.0697` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
