# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T12:22:29.385989+00:00`
- Price records: `672`
- Market context records: `7353`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `7.0473` n `32` status `ready` deltaP `38.7957` edge `0.3479` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.0473` n `32` status `ready` deltaP `38.7957` edge `0.3479` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.7895` n `32` status `ready` deltaP `32.0884` edge `0.2929` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.7895` n `32` status `ready` deltaP `32.0884` edge `0.2929` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.37` n `32` status `ready` deltaP `18.5976` edge `0.3665` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.37` n `32` status `ready` deltaP `18.5976` edge `0.3665` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2254` n `32` status `ready` deltaP `19.9289` edge `0.0487` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2254` n `32` status `ready` deltaP `19.9289` edge `0.0487` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2583` n `32` status `ready` deltaP `4.1479` edge `0.0218` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2583` n `32` status `ready` deltaP `4.1479` edge `0.0218` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1843` n `32` status `ready` deltaP `4.2042` edge `0.0333` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1843` n `32` status `ready` deltaP `4.2042` edge `0.0333` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1219` n `32` status `ready` deltaP `0.5988` edge `0.0487` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1219` n `32` status `ready` deltaP `0.5988` edge `0.0487` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.125` n `32` status `ready` deltaP `-0.6098` edge `0.076` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.125` n `32` status `ready` deltaP `-0.6098` edge `0.076` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1715` n `129` status `ready` deltaP `4.089` edge `-0.0003` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5524` n `129` status `ready` deltaP `6.5336` edge `0.1215` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7081` n `129` status `ready` deltaP `-3.2649` edge `-0.0118` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.8093` n `129` status `ready` deltaP `-5.3111` edge `-0.0075` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
