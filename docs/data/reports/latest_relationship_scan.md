# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T03:37:30.140686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.1811` n `94` status `ready` deltaP `7.192` edge `0.2546` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5887` n `96` status `ready` deltaP `13.2049` edge `0.0745` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.526` n `96` status `ready` deltaP `8.8668` edge `0.1569` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.3386` n `94` status `ready` deltaP `16.1754` edge `0.2471` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1562` n `96` status `ready` deltaP `17.4796` edge `0.0374` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9705` n `96` status `ready` deltaP `11.3059` edge `0.1076` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8719` n `96` status `ready` deltaP `15.1634` edge `0.0103` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.4018` n `96` status `ready` deltaP `10.9756` edge `0.0873` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.3487` n `96` status `ready` deltaP `9.3563` edge `-0.0106` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1368` n `96` status `ready` deltaP `5.8196` edge `0.0113` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.0193` n `96` status `ready` deltaP `6.7327` edge `0.0029` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.0221` n `96` status `ready` deltaP `6.4278` edge `0.0208` maxDD `-0.5728`
- `market_context_high->unknown_24h` score `-0.1315` n `94` status `ready` deltaP `14.3802` edge `-0.0683` maxDD `-0.7485`
- `market_context_high->fx_1h` score `-0.3292` n `96` status `ready` deltaP `-1.3224` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.3294` n `96` status `ready` deltaP `3.2747` edge `0.0161` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.3954` n `96` status `ready` deltaP `2.5324` edge `0.0169` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.496` n `96` status `ready` deltaP `1.9563` edge `0.0084` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8627` n `96` status `ready` deltaP `-7.2917` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9917` n `94` status `ready` deltaP `-2.582` edge `0.0717` maxDD `-10.4531`
- `market_context_high->fx_24h` score `-4.196` n `94` status `ready` deltaP `-25.0332` edge `-0.0281` maxDD `-1.7079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
