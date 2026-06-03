# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T18:22:31.552742+00:00`
- Price records: `672`
- Market context records: `2788`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.1748` n `142` status `ready` deltaP `5.9003` edge `0.2717` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.5443` n `142` status `ready` deltaP `3.5701` edge `0.5799` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8592` n `142` status `ready` deltaP `6.1856` edge `0.1357` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5485` n `142` status `ready` deltaP `11.0377` edge `0.2815` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3066` n `142` status `ready` deltaP `13.1484` edge `0.0358` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0745` n `142` status `ready` deltaP `3.8817` edge `0.041` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0898` n `142` status `ready` deltaP `4.198` edge `0.0099` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5371` n `142` status `ready` deltaP `-0.5376` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6256` n `142` status `ready` deltaP `0.5819` edge `0.0005` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6935` n `142` status `ready` deltaP `-0.8813` edge `-0.0077` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.717` n `142` status `ready` deltaP `4.9465` edge `0.0511` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9466` n `142` status `ready` deltaP `3.6266` edge `0.0414` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0334` n `142` status `ready` deltaP `-3.1985` edge `0.0185` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.0947` n `142` status `ready` deltaP `-3.1432` edge `0.0076` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.2538` n `142` status `ready` deltaP `1.9624` edge `0.0204` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.3285` n `142` status `ready` deltaP `14.1854` edge `0.2288` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4587` n `142` status `ready` deltaP `-1.8852` edge `-0.0218` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6569` n `142` status `ready` deltaP `-0.6012` edge `-0.0164` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.1166` n `142` status `ready` deltaP `-0.4659` edge `-0.0132` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4145` n `142` status `ready` deltaP `5.7347` edge `0.1428` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
