# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T14:52:32.944042+00:00`
- Price records: `672`
- Market context records: `7888`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14709`

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

- `market_context_high->equity_24h` score `14.2165` n `107` status `ready` deltaP `29.6993` edge `1.1209` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.9684` n `107` status `ready` deltaP `15.2472` edge `0.41` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.7522` n `107` status `ready` deltaP `23.662` edge `0.3167` maxDD `-0.608`
- `market_context_high->commodity_24h` score `1.7231` n `107` status `ready` deltaP `21.5909` edge `0.158` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.6336` n `107` status `ready` deltaP `13.8224` edge `0.1557` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5016` n `107` status `ready` deltaP `15.5607` edge `0.1932` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.2511` n `107` status `ready` deltaP `33.099` edge `0.0485` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1891` n `113` status `ready` deltaP `13.2677` edge `0.0515` maxDD `-1.6021`
- `market_context_high->index_4h` score `0.9996` n `107` status `ready` deltaP `16.3345` edge `0.0614` maxDD `-0.9597`
- `market_context_high->equity_1h` score `0.8687` n `113` status `ready` deltaP `12.0651` edge `0.1127` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.7987` n `107` status `ready` deltaP `11.1622` edge `0.0515` maxDD `-1.0817`
- `market_context_high->metal_4h` score `0.7312` n `107` status `ready` deltaP `10.0201` edge `0.1022` maxDD `-0.979`
- `market_context_high->index_1h` score `0.5933` n `113` status `ready` deltaP `11.0779` edge `0.0186` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4353` n `113` status `ready` deltaP `5.3296` edge `0.044` maxDD `-1.4603`
- `market_context_high->index_24h` score `0.0895` n `107` status `ready` deltaP `1.2229` edge `0.1218` maxDD `-1.4662`
- `market_context_high->metal_1h` score `-0.0551` n `113` status `ready` deltaP `3.8723` edge `0.0241` maxDD `-0.6936`
- `market_context_high->commodity_1h` score `-0.2335` n `113` status `ready` deltaP `3.6182` edge `0.0028` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4513` n `113` status `ready` deltaP `0.19` edge `-0.0004` maxDD `-0.4112`
- `market_context_high->fx_4h` score `-0.5513` n `107` status `ready` deltaP `2.4171` edge `0.0014` maxDD `-1.3885`
- `market_context_high->crypto_alt_24h` score `-1.7354` n `107` status `ready` deltaP `11.4365` edge `0.2308` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
