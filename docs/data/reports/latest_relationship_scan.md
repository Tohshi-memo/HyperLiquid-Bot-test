# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T22:32:02.638575+00:00`
- Price records: `672`
- Market context records: `5601`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.5191` n `174` status `ready` deltaP `15.0084` edge `0.7011` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4448` n `215` status `ready` deltaP `12.9822` edge `0.2631` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1689` n `174` status `ready` deltaP `20.7436` edge `0.0565` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.7679` n `215` status `ready` deltaP `8.0807` edge `0.1742` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5291` n `215` status `ready` deltaP `6.5485` edge `0.1643` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.297` n `227` status `ready` deltaP `6.1265` edge `0.0351` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3224` n `227` status `ready` deltaP `0.7848` edge `0.001` maxDD `-0.472`
- `market_context_high->metal_1h` score `-0.564` n `227` status `ready` deltaP `-0.7934` edge `0.0005` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5644` n `227` status `ready` deltaP `1.3236` edge `0.0403` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5963` n `227` status `ready` deltaP `4.0439` edge `0.0479` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.8443` n `227` status `ready` deltaP `0.9173` edge `0.0062` maxDD `-0.9472`
- `market_context_high->crypto_major_24h` score `-0.9704` n `174` status `ready` deltaP `10.6741` edge `0.302` maxDD `-29.6555`
- `market_context_high->commodity_1h` score `-1.1839` n `227` status `ready` deltaP `-2.2818` edge `-0.0069` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.5676` n `215` status `ready` deltaP `1.8506` edge `0.0078` maxDD `-1.0614`
- `market_context_high->index_4h` score `-1.5886` n `215` status `ready` deltaP `2.3157` edge `0.0131` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3374` n `174` status `ready` deltaP `10.6082` edge `0.0283` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9235` n `215` status `ready` deltaP `-12.0519` edge `-0.0561` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1973` n `215` status `ready` deltaP `-5.7629` edge `-0.0438` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.1283` n `174` status `ready` deltaP `-9.1954` edge `-0.2447` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.0321` n `174` status `ready` deltaP `0.461` edge `-0.0527` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
