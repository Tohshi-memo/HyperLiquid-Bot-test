# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T14:37:30.843184+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `5303.2737` n `97` status `ready` deltaP `13.3895` edge `441.8554` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `2785.8745` n `50` status `ready` deltaP `15.4514` edge `232.0532` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2785.8745` n `50` status `ready` deltaP `15.4514` edge `232.0532` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.2383` n `82` status `ready` deltaP `-4.9511` edge `32.0117` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.8161` n `59` status `ready` deltaP `55.3731` edge `1.7889` maxDD `-5.8705`
- `news_risk_high->crypto_alt_24h` score `17.8298` n `59` status `ready` deltaP `30.6615` edge `1.3302` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `17.7991` n `50` status `ready` deltaP `39.3056` edge `1.2442` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.7991` n `50` status `ready` deltaP `39.3056` edge `1.2442` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5532` n `97` status `ready` deltaP `32.8108` edge `1.1601` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.5131` n `59` status `ready` deltaP `35.3255` edge `0.8171` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.084` n `50` status `ready` deltaP `38.7153` edge `0.4989` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.084` n `50` status `ready` deltaP `38.7153` edge `0.4989` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7924` n `97` status `ready` deltaP `38.7153` edge `0.4746` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6663` n `50` status `ready` deltaP `42.3232` edge `0.4772` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6663` n `50` status `ready` deltaP `42.3232` edge `0.4772` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.4879` n `59` status `ready` deltaP `54.5139` edge `0.3439` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9534` n `59` status `ready` deltaP `51.9921` edge `0.3255` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.855` n `50` status `ready` deltaP `49.3819` edge `0.0796` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.855` n `50` status `ready` deltaP `49.3819` edge `0.0796` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1271` n `50` status `ready` deltaP `36.8171` edge `0.1078` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
