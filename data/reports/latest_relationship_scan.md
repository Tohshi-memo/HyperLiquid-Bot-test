# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T18:07:29.371717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `risk_on_high->unknown_4h` score `7.9008` n `107` status `ready` deltaP `23.8788` edge `0.5609` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.9008` n `107` status `ready` deltaP `23.8788` edge `0.5609` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3535` n `159` status `ready` deltaP `20.5754` edge `0.4617` maxDD `-2.5526`
- `risk_on_high->crypto_alt_24h` score `3.6631` n `78` status `ready` deltaP `22.1154` edge `0.8423` maxDD `-33.2749`
- `risk_on_and_context->crypto_alt_24h` score `3.6631` n `78` status `ready` deltaP `22.1154` edge `0.8423` maxDD `-33.2749`
- `risk_on_high->unknown_1h` score `2.511` n `107` status `ready` deltaP `7.264` edge `0.2185` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.511` n `107` status `ready` deltaP `7.264` edge `0.2185` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.2871` n `159` status `ready` deltaP `6.6057` edge `0.2096` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.8758` n `78` status `ready` deltaP `12.7671` edge `0.17` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.8758` n `78` status `ready` deltaP `12.7671` edge `0.17` maxDD `-0.5706`
- `risk_on_high->fx_24h` score `1.8085` n `78` status `ready` deltaP `48.8114` edge `0.0307` maxDD `-2.273`
- `risk_on_and_context->fx_24h` score `1.8085` n `78` status `ready` deltaP `48.8114` edge `0.0307` maxDD `-2.273`
- `news_risk_high->unknown_1h` score `1.6053` n `61` status `ready` deltaP `4.3683` edge `0.1393` maxDD `-1.1049`
- `market_context_high->fx_24h` score `0.8196` n `121` status `ready` deltaP `31.1912` edge `0.0221` maxDD `-2.9393`
- `market_context_high->crypto_alt_24h` score `0.3241` n `121` status `ready` deltaP `10.365` edge `0.5122` maxDD `-35.343`
- `news_risk_high->commodity_4h` score `0.3048` n `61` status `ready` deltaP `8.2542` edge `0.0257` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2079` n `159` status `ready` deltaP `9.6298` edge `0.0181` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1707` n `61` status `ready` deltaP `10.9582` edge `0.0005` maxDD `-0.7461`
- `news_risk_high->commodity_24h` score `0.1519` n `44` status `ready` deltaP `4.6086` edge `0.0203` maxDD `-1.1904`
- `market_context_high->commodity_4h` score `0.1005` n `159` status `ready` deltaP `7.7284` edge `0.0466` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
