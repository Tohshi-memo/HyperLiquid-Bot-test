# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T12:37:25.132035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9980`

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

- `market_context_high->unknown_24h` score `555.9212` n `64` status `ready` deltaP `3.6395` edge `46.3025` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4374` n `50` status `ready` deltaP `48.8319` edge `3.4482` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.7549` n `64` status `ready` deltaP `45.2069` edge `3.1657` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.5021` n `64` status `ready` deltaP `60.4636` edge `2.4131` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.6942` n `50` status `ready` deltaP `46.3882` edge `2.8428` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2429` n `50` status `ready` deltaP `39.2195` edge `0.8718` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.5108` n `50` status `ready` deltaP `16.9636` edge `1.4286` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.9409` n `64` status `ready` deltaP `47.9988` edge `0.3504` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `7.0506` n `50` status `ready` deltaP `46.4471` edge `0.2779` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3467` n `50` status `ready` deltaP `40.6863` edge `0.288` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.3412` n `64` status `ready` deltaP `59.7649` edge `0.5037` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.2699` n `50` status `ready` deltaP `23.5854` edge `0.4195` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `5.1526` n `64` status `ready` deltaP `13.3882` edge `1.2739` maxDD `-69.0352`
- `news_risk_high->metal_4h` score `4.9356` n `50` status `ready` deltaP `44.689` edge `0.151` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.563` n `50` status `ready` deltaP `27.4512` edge `0.3408` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0283` n `50` status `ready` deltaP `21.7964` edge `0.2534` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6282` n `50` status `ready` deltaP `33.5244` edge `0.1042` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6975` n `50` status `ready` deltaP `26.3232` edge `0.0843` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2736` n `50` status `ready` deltaP `26.0419` edge `0.0413` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2951` n `50` status `ready` deltaP `17.1976` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
