# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T17:52:25.852553+00:00`
- Price records: `672`
- Market context records: `7588`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_24h` score `0.0891` n `146` status `ready` deltaP `13.7965` edge `0.0738` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.0717` n `154` status `ready` deltaP `8.8169` edge `0.0232` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.0111` n `154` status `ready` deltaP `5.7994` edge `0.0116` maxDD `-0.9072`
- `market_context_high->unknown_24h` score `-0.1061` n `147` status `ready` deltaP `10.7249` edge `0.1001` maxDD `-7.4832`
- `market_context_high->commodity_1h` score `-0.2155` n `154` status `ready` deltaP `5.4386` edge `0.003` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.4109` n `146` status `ready` deltaP `8.9686` edge `0.0168` maxDD `-3.2001`
- `market_context_high->crypto_alt_1h` score `-0.464` n `154` status `ready` deltaP `0.4997` edge `0.0118` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4788` n `154` status `ready` deltaP `6.2447` edge `0.0122` maxDD `-5.5504`
- `market_context_high->index_4h` score `-0.631` n `154` status `ready` deltaP `9.3213` edge `0.0296` maxDD `-3.4775`
- `market_context_high->equity_1h` score `-0.6396` n `154` status `ready` deltaP `5.6004` edge `0.0502` maxDD `-8.8965`
- `market_context_high->fx_1h` score `-0.6475` n `154` status `ready` deltaP `-0.3939` edge `-0.0014` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.9186` n `154` status `ready` deltaP `1.6953` edge `0.0167` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9643` n `154` status `ready` deltaP `0.0486` edge `-0.0616` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.2188` n `154` status `ready` deltaP `1.3383` edge `0.0446` maxDD `-10.1158`
- `market_context_high->crypto_major_4h` score `-1.6368` n `154` status `ready` deltaP `6.1886` edge `0.0526` maxDD `-16.63`
- `market_context_high->metal_4h` score `-1.6843` n `154` status `ready` deltaP `-1.762` edge `0.044` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.7758` n `154` status `ready` deltaP `1.9878` edge `0.1958` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.3381` n `154` status `ready` deltaP `-3.5069` edge `-0.003` maxDD `-2.1439`
- `market_context_high->equity_24h` score `-2.3406` n `146` status `ready` deltaP `16.4575` edge `0.4591` maxDD `-62.5118`
- `market_context_high->unknown_4h` score `-2.6848` n `154` status `ready` deltaP `10.7955` edge `-0.1916` maxDD `-5.2989`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
