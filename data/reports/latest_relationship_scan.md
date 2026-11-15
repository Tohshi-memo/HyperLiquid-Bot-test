# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T12:52:23.446938+00:00`
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

- `market_context_high->unknown_24h` score `555.9542` n `64` status `ready` deltaP `3.8128` edge `46.3041` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4422` n `50` status `ready` deltaP `48.8319` edge `3.4486` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.7597` n `64` status `ready` deltaP `45.2069` edge `3.1661` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.5333` n `64` status `ready` deltaP `60.4636` edge `2.4157` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.6786` n `50` status `ready` deltaP `46.3882` edge `2.8408` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2211` n `50` status `ready` deltaP `39.0671` edge `0.871` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.5311` n `50` status `ready` deltaP `16.9636` edge `1.4312` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.9421` n `64` status `ready` deltaP `47.9988` edge `0.3505` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `7.0235` n `50` status `ready` deltaP `46.2738` edge `0.2768` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3588` n `64` status `ready` deltaP `59.9383` edge `0.5048` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.3479` n `50` status `ready` deltaP `40.6863` edge `0.2881` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.2229` n `50` status `ready` deltaP `23.4329` edge `0.4166` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `5.1286` n `64` status `ready` deltaP `13.3882` edge `1.2719` maxDD `-69.0352`
- `news_risk_high->metal_4h` score `4.9222` n `50` status `ready` deltaP `44.5366` edge `0.1509` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.51` n `50` status `ready` deltaP `27.2988` edge `0.3374` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0151` n `50` status `ready` deltaP `21.6467` edge `0.2533` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6416` n `50` status `ready` deltaP `33.6768` edge `0.1043` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6841` n `50` status `ready` deltaP `26.1707` edge `0.0842` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2604` n `50` status `ready` deltaP `25.8922` edge `0.0412` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2951` n `50` status `ready` deltaP `17.1976` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
