# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T17:07:22.365911+00:00`
- Price records: `672`
- Market context records: `2988`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `16.4769` n `98` status `ready` deltaP `4.9426` edge `1.7318` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.0306` n `98` status `ready` deltaP `41.773` edge `0.7351` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.2923` n `98` status `ready` deltaP `17.3541` edge `0.8718` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.3401` n `98` status `ready` deltaP `15.742` edge `0.7071` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.6498` n `98` status `ready` deltaP `15.6994` edge `0.3809` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.4177` n `99` status `ready` deltaP `15.0669` edge `0.2233` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.3873` n `99` status `ready` deltaP `19.6015` edge `0.1471` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.3562` n `99` status `ready` deltaP `17.335` edge `0.1455` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.9442` n `99` status `ready` deltaP `24.4026` edge `0.4145` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3486` n `102` status `ready` deltaP `6.8627` edge `0.0302` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.0777` n `102` status `ready` deltaP `5.3804` edge `0.0442` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2137` n `102` status `ready` deltaP `-0.3669` edge `0.0176` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4924` n `102` status `ready` deltaP `-1.6467` edge `0.0012` maxDD `-0.1672`
- `market_context_high->crypto_alt_1h` score `-0.9932` n `102` status `ready` deltaP `8.1425` edge `0.0382` maxDD `-11.6869`
- `market_context_high->fx_4h` score `-1.0351` n `99` status `ready` deltaP `-8.5859` edge `0.0024` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.0603` n `102` status `ready` deltaP `-2.4393` edge `-0.0062` maxDD `-5.4112`
- `market_context_high->crypto_major_1h` score `-1.0631` n `102` status `ready` deltaP `5.4039` edge `0.0108` maxDD `-11.9831`
- `market_context_high->unknown_4h` score `-1.1272` n `99` status `ready` deltaP `-0.3141` edge `0.0135` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.7066` n `102` status `ready` deltaP `1.9755` edge `-0.0823` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.8888` n `99` status `ready` deltaP `9.6128` edge `0.2063` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
