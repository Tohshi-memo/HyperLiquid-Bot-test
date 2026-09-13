# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T07:37:29.800135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12880`

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

- `market_context_high->unknown_24h` score `17567.7149` n `57` status `ready` deltaP `13.5051` edge `1463.8914` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.1927` n `82` status `ready` deltaP `-5.2505` edge `31.5099` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.6937` n `82` status `ready` deltaP `31.8851` edge `1.3107` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.65` n `82` status `ready` deltaP `37.589` edge `1.3673` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `9.9506` n `57` status `ready` deltaP `20.8881` edge `0.7727` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.4774` n `57` status `ready` deltaP `45.2576` edge `0.5321` maxDD `-2.5225`
- `news_risk_high->equity_24h` score `7.0013` n `82` status `ready` deltaP `20.033` edge `0.6279` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.3954` n `82` status `ready` deltaP `45.2574` edge `0.2489` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5807` n `82` status `ready` deltaP `24.0515` edge `0.2668` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2942` n `57` status `ready` deltaP `42.1875` edge `0.0766` maxDD `0.0`
- `market_context_high->index_24h` score `3.8852` n `57` status `ready` deltaP `41.8129` edge `0.0835` maxDD `-0.4124`
- `market_context_high->metal_24h` score `0.8459` n `57` status `ready` deltaP `12.1345` edge `0.115` maxDD `-1.9958`
- `news_risk_high->index_4h` score `0.332` n `82` status `ready` deltaP `11.2805` edge `0.0302` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.2509` n `65` status `ready` deltaP `9.6951` edge `0.135` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2509` n `65` status `ready` deltaP `9.6951` edge `0.135` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.1592` n `65` status `ready` deltaP `5.3017` edge `0.0035` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1592` n `65` status `ready` deltaP `5.3017` edge `0.0035` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.2487` n `131` status `ready` deltaP `1.849` edge `-0.0014` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
