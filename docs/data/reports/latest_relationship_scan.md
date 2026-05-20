# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T01:52:16.501755+00:00`
- Price records: `672`
- Market context records: `1276`
- Flow alert records: `5583`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.9569` n `128` status `ready` deltaP `41.5798` edge `1.3324` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.76` n `128` status `ready` deltaP `6.5972` edge `1.0194` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.8697` n `128` status `ready` deltaP `25.7812` edge `0.7689` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.7345` n `134` status `ready` deltaP `4.8939` edge `0.5669` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.3027` n `128` status `ready` deltaP `27.6042` edge `0.3665` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9109` n `128` status `ready` deltaP `25.3472` edge `0.5651` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.2834` n `134` status `ready` deltaP `16.477` edge `0.2301` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3742` n `128` status `ready` deltaP `1.5625` edge `0.4604` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.663` n `128` status `ready` deltaP `-12.8472` edge `0.3724` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.5772` n `134` status `ready` deltaP `12.1997` edge `0.1184` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.8274` n `134` status `ready` deltaP `17.5418` edge `0.0951` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.456` n `146` status `ready` deltaP `5.1473` edge `0.0464` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.4531` n `146` status `ready` deltaP `7.7783` edge `0.0231` maxDD `-0.9758`
- `market_context_high->metal_1h` score `0.4468` n `146` status `ready` deltaP `11.8612` edge `0.0192` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.156` n `128` status `ready` deltaP `4.2535` edge `0.0311` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `-0.1773` n `134` status `ready` deltaP `7.1646` edge `0.1609` maxDD `-11.512`
- `market_context_high->crypto_alt_1h` score `-0.3197` n `146` status `ready` deltaP `1.1792` edge `0.0382` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.484` n `146` status `ready` deltaP `1.2653` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.7398` n `146` status `ready` deltaP `0.363` edge `0.0048` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8096` n `134` status `ready` deltaP `7.7039` edge `0.1768` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
