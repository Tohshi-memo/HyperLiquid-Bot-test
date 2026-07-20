# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T05:52:26.991948+00:00`
- Price records: `672`
- Market context records: `7325`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14831`

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

- `risk_on_high->crypto_major_4h` score `7.2367` n `32` status `ready` deltaP `39.5579` edge `0.3586` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.2367` n `32` status `ready` deltaP `39.5579` edge `0.3586` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.9391` n `32` status `ready` deltaP `32.6982` edge `0.3013` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.9391` n `32` status `ready` deltaP `32.6982` edge `0.3013` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3035` n `32` status `ready` deltaP `18.1402` edge `0.364` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3035` n `32` status `ready` deltaP `18.1402` edge `0.364` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.3025` n `32` status `ready` deltaP `20.378` edge `0.0556` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3025` n `32` status `ready` deltaP `20.378` edge `0.0556` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2295` n `32` status `ready` deltaP `4.1479` edge `0.0194` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2295` n `32` status `ready` deltaP `4.1479` edge `0.0194` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2123` n `32` status `ready` deltaP `4.2042` edge `0.0369` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2123` n `32` status `ready` deltaP `4.2042` edge `0.0369` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1843` n `32` status `ready` deltaP `0.8982` edge `0.0547` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1843` n `32` status `ready` deltaP `0.8982` edge `0.0547` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0338` n `32` status `ready` deltaP `0.3049` edge `0.0775` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0338` n `32` status `ready` deltaP `0.3049` edge `0.0775` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1691` n `129` status `ready` deltaP `4.089` edge `0.0` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5956` n `129` status `ready` deltaP `6.0762` edge `0.119` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7268` n `129` status `ready` deltaP `-3.2649` edge `-0.0142` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7711` n `129` status `ready` deltaP `-4.7105` edge `-0.0066` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
