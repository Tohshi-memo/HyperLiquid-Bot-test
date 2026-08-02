# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T06:52:28.186189+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.6378` n `60` status `ready` deltaP `32.1548` edge `432.2142` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.1165` n `48` status `ready` deltaP `60.4709` edge `1.1463` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `5.2365` n `48` status `ready` deltaP `35.1495` edge `0.3284` maxDD `-7.1082`
- `news_risk_high->equity_4h` score `4.5095` n `68` status `ready` deltaP `16.3737` edge `0.343` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `1.0187` n `48` status `ready` deltaP `21.2399` edge `0.0229` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6492` n `68` status `ready` deltaP `9.9419` edge `0.0701` maxDD `-2.916`
- `market_context_high->commodity_4h` score `0.4341` n `48` status `ready` deltaP `8.6382` edge `0.0827` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.3106` n `48` status `ready` deltaP `5.2845` edge `0.1003` maxDD `-5.323`
- `news_risk_high->fx_4h` score `0.126` n `68` status `ready` deltaP `12.2938` edge `0.0243` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.0977` n `68` status `ready` deltaP `5.165` edge `0.0257` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0718` n `68` status `ready` deltaP `6.1818` edge `0.0362` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.035` n `68` status `ready` deltaP `3.4167` edge `0.005` maxDD `-0.2475`
- `market_context_high->fx_24h` score `-0.0597` n `48` status `ready` deltaP `7.1599` edge `0.0426` maxDD `-2.506`
- `market_context_high->fx_1h` score `-0.0625` n `48` status `ready` deltaP `6.1128` edge `0.0015` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0863` n `68` status `ready` deltaP `2.1663` edge `0.0068` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.1183` n `48` status `ready` deltaP `1.9461` edge `0.0218` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1598` n `68` status `ready` deltaP `2.1663` edge `0.0054` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2669` n `68` status `ready` deltaP `1.6203` edge `0.027` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6272` n `68` status `ready` deltaP `3.4167` edge `-0.0252` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
