# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T11:52:28.162107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11994.8746` n `108` status `ready` deltaP `0.8373` edge `999.5871` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7446.7416` n `108` status `ready` deltaP `0.0621` edge `620.5898` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `14.4983` n `94` status `ready` deltaP `42.4165` edge `1.7376` maxDD `-10.9297`
- `market_context_high->crypto_alt_24h` score `11.2228` n `94` status `ready` deltaP `23.0091` edge `1.4434` maxDD `-8.9716`
- `market_context_high->crypto_major_4h` score `0.663` n `108` status `ready` deltaP `2.264` edge `0.3518` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.2613` n `108` status `ready` deltaP `2.7213` edge `0.2271` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.034` n `94` status `ready` deltaP `16.615` edge `0.2009` maxDD `-14.7068`
- `market_context_high->metal_4h` score `-0.0135` n `108` status `ready` deltaP `15.4302` edge `0.025` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.2467` n `108` status `ready` deltaP `3.2934` edge `0.0129` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.6771` n `108` status `ready` deltaP `2.6946` edge `0.0689` maxDD `-9.2267`
- `market_context_high->index_1h` score `-0.6991` n `108` status `ready` deltaP `-1.0091` edge `0.0033` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0157` n `108` status `ready` deltaP `-2.6835` edge `0.0287` maxDD `-6.9489`
- `market_context_high->index_4h` score `-1.207` n `108` status `ready` deltaP `-2.9415` edge `-0.0008` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.559` n `108` status `ready` deltaP `-11.0723` edge `-0.0012` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.436` n `108` status `ready` deltaP `-15.56` edge `-0.0045` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-2.5141` n `108` status `ready` deltaP `1.619` edge `-0.0166` maxDD `-10.9626`
- `market_context_high->commodity_1h` score `-2.5385` n `108` status `ready` deltaP `-11.344` edge `-0.0281` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-6.8311` n `94` status `ready` deltaP `-20.0724` edge `-0.0063` maxDD `-5.6645`
- `market_context_high->commodity_4h` score `-7.7456` n `108` status `ready` deltaP `-26.1574` edge `-0.1092` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.4054` n `94` status `ready` deltaP `-17.9632` edge `-0.1218` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
