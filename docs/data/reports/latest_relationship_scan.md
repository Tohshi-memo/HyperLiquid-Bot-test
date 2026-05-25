# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T02:07:19.116977+00:00`
- Price records: `672`
- Market context records: `1799`
- Flow alert records: `7075`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.0057` n `188` status `ready` deltaP `28.487` edge `0.6365` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4678` n `30` status `ready` deltaP `29.2582` edge `0.4094` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7176` n `191` status `ready` deltaP `21.1179` edge `0.5123` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.6597` n `191` status `ready` deltaP `23.656` edge `0.458` maxDD `-9.8583`
- `market_context_high->unknown_4h` score `4.092` n `191` status `ready` deltaP `16.2798` edge `0.4481` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2326` n `30` status `ready` deltaP `24.5709` edge `0.1373` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.8659` n `191` status `ready` deltaP `15.9415` edge `0.242` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.7264` n `188` status `ready` deltaP `13.4456` edge `0.2604` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.6928` n `188` status `ready` deltaP `16.1717` edge `0.5231` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `0.954` n `188` status `ready` deltaP `11.691` edge `0.5336` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.8964` n `30` status `ready` deltaP `21.6362` edge `-0.0021` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8276` n `191` status `ready` deltaP `11.9652` edge `0.0981` maxDD `-3.7119`
- `news_risk_high->unknown_4h` score `0.3776` n `30` status `ready` deltaP `9.9796` edge `0.0542` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.2994` n `193` status `ready` deltaP `6.8102` edge `0.0907` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.258` n `193` status `ready` deltaP `5.1178` edge `0.086` maxDD `-3.2225`
- `market_context_high->equity_1h` score `-0.2091` n `193` status `ready` deltaP `3.8736` edge `0.0376` maxDD `-2.8014`
- `news_risk_high->unknown_1h` score `-0.4232` n `30` status `ready` deltaP `17.006` edge `-0.1204` maxDD `-2.1115`
- `market_context_high->index_1h` score `-0.4357` n `193` status `ready` deltaP `1.8244` edge `0.0147` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.4663` n `188` status `ready` deltaP `8.3924` edge `0.0101` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4718` n `30` status `ready` deltaP `-5.1297` edge `-0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
