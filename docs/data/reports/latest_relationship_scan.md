# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T22:52:13.534078+00:00`
- Price records: `591`
- Market context records: `693`
- Flow alert records: `1959`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.1746` n `146` status `ready` deltaP `24.9121` edge `0.7152` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6185` n `146` status `ready` deltaP `8.406` edge `0.5003` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2044` n `149` status `ready` deltaP `7.2803` edge `0.0124` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.273` n `149` status `ready` deltaP `3.0011` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5113` n `149` status `ready` deltaP `2.1665` edge `0.0404` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5711` n `149` status `ready` deltaP `1.0545` edge `0.0051` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0784` n `149` status `ready` deltaP `-1.1604` edge `-0.0011` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.2148` n `149` status `ready` deltaP `15.3394` edge `0.1126` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2171` n `149` status `ready` deltaP `-4.3184` edge `-0.0123` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3589` n `149` status `ready` deltaP `4.6545` edge `-0.0128` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.5502` n `146` status `ready` deltaP `-4.6606` edge `0.1014` maxDD `-5.9609`
- `market_context_high->index_4h` score `-1.6062` n `149` status `ready` deltaP `2.9878` edge `-0.0015` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6165` n `149` status `ready` deltaP `6.0895` edge `-0.003` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9635` n `149` status `ready` deltaP `4.3583` edge `0.0643` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6305` n `149` status `ready` deltaP `-1.2153` edge `0.0041` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-2.8449` n `146` status `ready` deltaP `-6.7349` edge `0.0683` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.2712` n `149` status `ready` deltaP `-4.5402` edge `-0.0464` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7652` n `149` status `ready` deltaP `-5.9356` edge `0.0759` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4872` n `149` status `ready` deltaP `2.0683` edge `-0.1999` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9253` n `146` status `ready` deltaP `-10.5404` edge `-0.044` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
