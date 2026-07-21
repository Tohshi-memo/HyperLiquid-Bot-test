# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T04:37:25.337642+00:00`
- Price records: `672`
- Market context records: `7424`
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

- `risk_on_high->crypto_major_4h` score `6.3182` n `32` status `ready` deltaP `36.3567` edge `0.3034` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.3182` n `32` status `ready` deltaP `36.3567` edge `0.3034` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.7617` n `32` status `ready` deltaP `16.8403` edge `0.47` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.7617` n `32` status `ready` deltaP `16.8403` edge `0.47` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `4.9755` n `32` status `ready` deltaP `16.0061` edge `0.3509` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9755` n `32` status `ready` deltaP `16.0061` edge `0.3509` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.8024` n `32` status `ready` deltaP `27.8201` edge `0.2391` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.8024` n `32` status `ready` deltaP `27.8201` edge `0.2391` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.8216` n `32` status `ready` deltaP `17.1875` edge `0.34` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.8216` n `32` status `ready` deltaP `17.1875` edge `0.34` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.0866` n `32` status `ready` deltaP `19.0307` edge `0.0369` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0866` n `32` status `ready` deltaP `19.0307` edge `0.0369` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.975` n `31` status `ready` deltaP `13.2011` edge `0.2646` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.975` n `31` status `ready` deltaP `13.2011` edge `0.2646` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.4409` n `32` status `ready` deltaP `5.6494` edge `0.027` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.4409` n `32` status `ready` deltaP `5.6494` edge `0.027` maxDD `-0.2339`
- `risk_on_high->fx_24h` score `0.0385` n `31` status `ready` deltaP `9.4582` edge `-0.0125` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.0385` n `31` status `ready` deltaP `9.4582` edge `-0.0125` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.011` n `32` status `ready` deltaP `2.7027` edge `0.0211` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.011` n `32` status `ready` deltaP `2.7027` edge `0.0211` maxDD `-1.3497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
