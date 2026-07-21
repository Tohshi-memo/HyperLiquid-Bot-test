# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T00:07:25.117147+00:00`
- Price records: `672`
- Market context records: `7405`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `risk_on_high->crypto_major_4h` score `6.359` n `32` status `ready` deltaP `36.3567` edge `0.3068` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.359` n `32` status `ready` deltaP `36.3567` edge `0.3068` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `5.0323` n `32` status `ready` deltaP `16.311` edge `0.3536` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.0323` n `32` status `ready` deltaP `16.311` edge `0.3536` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.8144` n `32` status `ready` deltaP `27.8201` edge `0.2401` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.8144` n `32` status `ready` deltaP `27.8201` edge `0.2401` maxDD `-0.9492`
- `risk_on_high->crypto_major_24h` score `4.7688` n `31` status `ready` deltaP `15.9341` edge `0.3933` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `4.7688` n `31` status `ready` deltaP `15.9341` edge `0.3933` maxDD `-5.8371`
- `risk_on_high->crypto_alt_24h` score `2.3547` n `31` status `ready` deltaP `15.6944` edge `0.2901` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.3547` n `31` status `ready` deltaP `15.6944` edge `0.2901` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.1186` n `32` status `ready` deltaP `19.3301` edge `0.039` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1186` n `32` status `ready` deltaP `19.3301` edge `0.039` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.4373` n `32` status `ready` deltaP `5.6494` edge `0.0267` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.4373` n `32` status `ready` deltaP `5.6494` edge `0.0267` maxDD `-0.2339`
- `risk_on_high->equity_24h` score `0.4139` n `30` status `ready` deltaP `14.0324` edge `0.2123` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.4139` n `30` status `ready` deltaP `14.0324` edge `0.2123` maxDD `-19.375`
- `risk_on_high->equity_1h` score `0.1132` n `32` status `ready` deltaP `3.4535` edge `0.0292` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1132` n `32` status `ready` deltaP `3.4535` edge `0.0292` maxDD `-1.3497`
- `risk_on_high->fx_24h` score `0.0636` n `30` status `ready` deltaP `9.0468` edge `-0.0127` maxDD `-1.1563`
- `risk_on_and_context->fx_24h` score `0.0636` n `30` status `ready` deltaP `9.0468` edge `-0.0127` maxDD `-1.1563`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
