# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T11:52:39.877373+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `101.5701` n `30` status `ready` deltaP `3.9861` edge `8.4376` maxDD `0.0`
- `news_risk_high->equity_24h` score `51.442` n `50` status `ready` deltaP `55.7643` edge `3.9857` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.4101` n `50` status `ready` deltaP `42.2288` edge `2.5777` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.2501` n `30` status `ready` deltaP `14.0959` edge `1.5813` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `12.5763` n `50` status `ready` deltaP `40.207` edge `0.893` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5456` n `30` status `ready` deltaP `44.2288` edge `1.6406` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.0871` n `50` status `ready` deltaP `24.7626` edge `1.5787` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.5616` n `50` status `ready` deltaP `46.7522` edge `0.3488` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.028` n `50` status `ready` deltaP `41.0745` edge `0.2285` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0889` n `50` status `ready` deltaP `45.3607` edge `0.1593` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.8134` n `50` status `ready` deltaP `28.1218` edge `0.3572` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.4734` n `50` status `ready` deltaP `21.9696` edge `0.3639` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9385` n `50` status `ready` deltaP `20.2242` edge `0.2564` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.9071` n `30` status `ready` deltaP `47.9492` edge `0.2704` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.6552` n `50` status `ready` deltaP `34.207` edge `0.1019` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6182` n `50` status `ready` deltaP `25.032` edge `0.0863` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1727` n `50` status `ready` deltaP `24.6158` edge `0.0424` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2925` n `50` status `ready` deltaP `17.1211` edge `0.0237` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0286` n `50` status `ready` deltaP `19.2825` edge `0.2206` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8299` n `50` status `ready` deltaP `17.9611` edge `0.0846` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
