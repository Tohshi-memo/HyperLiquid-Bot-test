# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T17:07:25.867642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10109`

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

- `risk_on_high->unknown_24h` score `145.5516` n `107` status `ready` deltaP `25.3213` edge `11.9704` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `145.5516` n `107` status `ready` deltaP `25.3213` edge `11.9704` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `15.6446` n `107` status `ready` deltaP `29.3841` edge `1.3353` maxDD `-13.8648`
- `risk_on_and_context->crypto_major_24h` score `15.6446` n `107` status `ready` deltaP `29.3841` edge `1.3353` maxDD `-13.8648`
- `risk_on_high->crypto_alt_24h` score `6.8289` n `107` status `ready` deltaP `17.619` edge `0.6926` maxDD `-13.9457`
- `risk_on_and_context->crypto_alt_24h` score `6.8289` n `107` status `ready` deltaP `17.619` edge `0.6926` maxDD `-13.9457`
- `market_context_high->equity_24h` score `4.5985` n `196` status `ready` deltaP `18.7145` edge `0.3775` maxDD `-5.1909`
- `market_context_high->crypto_alt_24h` score `3.9987` n `196` status `ready` deltaP `17.1804` edge `0.485` maxDD `-15.3052`
- `risk_on_high->equity_24h` score `2.7352` n `107` status `ready` deltaP `13.1977` edge `0.259` maxDD `-5.1909`
- `risk_on_and_context->equity_24h` score `2.7352` n `107` status `ready` deltaP `13.1977` edge `0.259` maxDD `-5.1909`
- `market_context_high->index_24h` score `0.5028` n `196` status `ready` deltaP `16.238` edge `0.082` maxDD `-3.8685`
- `risk_on_high->index_24h` score `0.2214` n `107` status `ready` deltaP `12.1707` edge `0.0543` maxDD `-3.3591`
- `risk_on_and_context->index_24h` score `0.2214` n `107` status `ready` deltaP `12.1707` edge `0.0543` maxDD `-3.3591`
- `risk_on_high->crypto_alt_1h` score `-0.1141` n `129` status `ready` deltaP `3.8516` edge `0.0665` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1141` n `129` status `ready` deltaP `3.8516` edge `0.0665` maxDD `-5.4685`
- `risk_on_high->index_1h` score `-0.1268` n `129` status `ready` deltaP `4.7927` edge `-0.0035` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1268` n `129` status `ready` deltaP `4.7927` edge `-0.0035` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.3367` n `129` status `ready` deltaP `4.6059` edge `-0.0031` maxDD `-1.6615`
- `risk_on_and_context->metal_1h` score `-0.3367` n `129` status `ready` deltaP `4.6059` edge `-0.0031` maxDD `-1.6615`
- `risk_on_high->equity_1h` score `-0.3984` n `129` status `ready` deltaP `7.4816` edge `-0.0139` maxDD `-2.6312`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
