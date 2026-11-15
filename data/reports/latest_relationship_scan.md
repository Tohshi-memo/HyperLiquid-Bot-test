# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T12:07:29.327554+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_24h` score `559.5253` n `64` status `ready` deltaP `3.4662` edge `46.604` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4206` n `50` status `ready` deltaP `48.8319` edge `3.4468` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.7381` n `64` status `ready` deltaP `45.2069` edge `3.1643` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.4181` n `64` status `ready` deltaP `60.4636` edge `2.4061` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7106` n `50` status `ready` deltaP `46.3882` edge `2.8449` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2877` n `50` status `ready` deltaP `39.5244` edge `0.8735` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.4562` n `50` status `ready` deltaP `16.9636` edge `1.4216` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.9247` n `64` status `ready` deltaP `47.8255` edge `0.3502` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `7.1047` n `50` status `ready` deltaP `46.7938` edge `0.2801` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3305` n `50` status `ready` deltaP `40.513` edge `0.2878` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.3061` n `64` status `ready` deltaP `59.4183` edge `0.5015` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.3685` n `50` status `ready` deltaP `23.7378` edge `0.4267` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `5.1778` n `64` status `ready` deltaP `13.3882` edge `1.276` maxDD `-69.0352`
- `news_risk_high->metal_4h` score `4.966` n `50` status `ready` deltaP `44.9939` edge `0.1515` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6798` n `50` status `ready` deltaP `27.7561` edge `0.3485` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0271` n `50` status `ready` deltaP `21.7964` edge `0.2533` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6148` n `50` status `ready` deltaP `33.372` edge `0.1041` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7243` n `50` status `ready` deltaP `26.628` edge `0.0845` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2736` n `50` status `ready` deltaP `26.0419` edge `0.0413` maxDD `-0.3692`
- `market_context_high->unknown_4h` score `2.2697` n `83` status `ready` deltaP `8.8415` edge `0.1302` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
