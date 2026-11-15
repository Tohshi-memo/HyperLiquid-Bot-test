# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T23:22:26.848992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_24h` score `881.8005` n `45` status `ready` deltaP `3.9861` edge `73.4568` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.7349` n `50` status `ready` deltaP `50.565` edge `3.6281` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `40.4335` n `65` status `ready` deltaP `8.9939` edge `3.3095` maxDD `0.0`
- `market_context_high->equity_24h` score `38.2137` n `45` status `ready` deltaP `40.3428` edge `3.0697` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.0946` n `45` status `ready` deltaP `58.8253` edge `2.4734` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.0388` n `50` status `ready` deltaP `43.7886` edge `2.6479` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.0809` n `45` status `ready` deltaP `16.8997` edge `1.5062` maxDD `-30.9696`
- `news_risk_high->equity_4h` score `11.69` n `50` status `ready` deltaP `36.628` edge `0.843` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1899` n `50` status `ready` deltaP `20.6031` edge `1.4914` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.6482` n `45` status `ready` deltaP `47.5794` edge `0.3288` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7451` n `50` status `ready` deltaP `42.2461` edge `0.3108` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.286` n `50` status `ready` deltaP `41.0745` edge `0.25` maxDD `0.0`
- `market_context_high->metal_24h` score `5.4937` n `45` status `ready` deltaP `58.5404` edge `0.4032` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.9022` n `50` status `ready` deltaP `43.9268` edge `0.1533` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.354` n `50` status `ready` deltaP `20.5366` edge `0.3635` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.001` n `50` status `ready` deltaP `25.3171` edge `0.3082` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.7526` n `50` status `ready` deltaP `19.8503` edge `0.2434` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6258` n `50` status `ready` deltaP `33.5244` edge `0.104` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.403` n `50` status `ready` deltaP `23.122` edge `0.0811` maxDD `-0.7999`
- `market_context_high->fx_24h` score `2.2723` n `45` status `ready` deltaP `25.207` edge `0.067` maxDD `-0.6554`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
