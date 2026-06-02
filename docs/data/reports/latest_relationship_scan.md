# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T16:52:27.942367+00:00`
- Price records: `672`
- Market context records: `2681`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.1697` n `111` status `ready` deltaP `16.0051` edge `1.0068` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.774` n `111` status `ready` deltaP `17.9993` edge `0.644` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `1.9807` n `132` status `ready` deltaP `19.4337` edge `0.3452` maxDD `-18.7758`
- `market_context_high->unknown_4h` score `1.372` n `132` status `ready` deltaP `7.2755` edge `0.1708` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.1075` n `132` status `ready` deltaP `10.1303` edge `0.0304` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1633` n `141` status `ready` deltaP `2.8454` edge `0.0095` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2059` n `141` status `ready` deltaP `2.8135` edge `0.0369` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.2839` n `111` status `ready` deltaP `9.6049` edge `-0.0005` maxDD `-0.6418`
- `market_context_high->crypto_major_4h` score `-0.3636` n `132` status `ready` deltaP `7.5943` edge `0.1877` maxDD `-18.4617`
- `market_context_high->commodity_1h` score `-0.3925` n `141` status `ready` deltaP `2.3718` edge `0.0092` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.452` n `141` status `ready` deltaP `6.9977` edge `0.0714` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.4799` n `141` status `ready` deltaP `0.0871` edge `0.0038` maxDD `-0.2164`
- `market_context_high->commodity_24h` score `-0.5249` n `111` status `ready` deltaP `7.9627` edge `0.189` maxDD `-12.4171`
- `market_context_high->index_24h` score `-0.565` n `111` status `ready` deltaP `5.579` edge `0.0138` maxDD `-2.5127`
- `market_context_high->fx_4h` score `-0.5896` n `132` status `ready` deltaP `0.5913` edge `0.0123` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-0.7974` n `141` status `ready` deltaP `-2.0332` edge `-0.0058` maxDD `-2.9635`
- `market_context_high->crypto_major_1h` score `-0.9493` n `141` status `ready` deltaP `3.8614` edge `0.0395` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1548` n `141` status `ready` deltaP `-4.0015` edge `0.0143` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2175` n `132` status `ready` deltaP `3.4691` edge `0.0128` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.2301` n `111` status `ready` deltaP `5.9967` edge `0.5586` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
