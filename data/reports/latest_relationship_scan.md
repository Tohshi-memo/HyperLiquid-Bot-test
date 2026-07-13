# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T10:07:26.050192+00:00`
- Price records: `672`
- Market context records: `6592`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `4.174` n `160` status `ready` deltaP `5.8592` edge `0.6388` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.01` n `210` status `ready` deltaP `-5.4291` edge `0.2938` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7805` n `160` status `ready` deltaP `10.7351` edge `0.1803` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.302` n `210` status `ready` deltaP `1.7565` edge `0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4781` n `210` status `ready` deltaP `6.2988` edge `0.0233` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5121` n `210` status `ready` deltaP `0.6387` edge `-0.0016` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5717` n `210` status `ready` deltaP `-0.6801` edge `0.0032` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6552` n `210` status `ready` deltaP `4.3941` edge `0.018` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9152` n `210` status `ready` deltaP `9.142` edge `0.0097` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2208` n `210` status `ready` deltaP `1.6325` edge `-0.0016` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2341` n `210` status `ready` deltaP `-0.5168` edge `-0.0053` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3866` n `210` status `ready` deltaP `-4.625` edge `-0.004` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6641` n `210` status `ready` deltaP `1.4489` edge `-0.0018` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7629` n `210` status `ready` deltaP `-17.6756` edge `0.2115` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9043` n `210` status `ready` deltaP `6.3618` edge `0.0449` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1933` n `210` status `ready` deltaP `-1.8061` edge `0.0169` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2063` n `210` status `ready` deltaP `3.4088` edge `0.0346` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.7688` n `160` status `ready` deltaP `-4.362` edge `-0.0006` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-3.8472` n `160` status `ready` deltaP `1.8556` edge `0.0673` maxDD `-9.0215`
- `market_context_high->equity_4h` score `-4.7723` n `210` status `ready` deltaP `7.3534` edge `-0.0198` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
