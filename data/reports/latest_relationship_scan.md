# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T02:07:24.461402+00:00`
- Price records: `672`
- Market context records: `7414`
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

- `risk_on_high->crypto_major_4h` score `6.3614` n `32` status `ready` deltaP `36.3567` edge `0.307` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.3614` n `32` status `ready` deltaP `36.3567` edge `0.307` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.4473` n `32` status `ready` deltaP `16.8403` edge `0.4438` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.4473` n `32` status `ready` deltaP `16.8403` edge `0.4438` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `5.0601` n `32` status `ready` deltaP `16.4634` edge `0.3549` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.0601` n `32` status `ready` deltaP `16.4634` edge `0.3549` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.8132` n `32` status `ready` deltaP `27.8201` edge `0.24` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.8132` n `32` status `ready` deltaP `27.8201` edge `0.24` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.8068` n `32` status `ready` deltaP `17.1875` edge `0.3381` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.8068` n `32` status `ready` deltaP `17.1875` edge `0.3381` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.1419` n `32` status `ready` deltaP `19.6295` edge `0.04` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1419` n `32` status `ready` deltaP `19.6295` edge `0.04` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.5982` n `31` status `ready` deltaP `13.2011` edge `0.2332` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.5982` n `31` status `ready` deltaP `13.2011` edge `0.2332` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.4241` n `32` status `ready` deltaP `5.4992` edge `0.0266` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.4241` n `32` status `ready` deltaP `5.4992` edge `0.0266` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1218` n `32` status `ready` deltaP `3.4535` edge `0.0303` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1218` n `32` status `ready` deltaP `3.4535` edge `0.0303` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0059` n `32` status `ready` deltaP `-0.2994` edge `0.0383` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0059` n `32` status `ready` deltaP `-0.2994` edge `0.0383` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
