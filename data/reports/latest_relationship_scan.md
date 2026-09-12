# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T15:52:31.387871+00:00`
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

- `market_context_high->unknown_24h` score `6297.2919` n `92` status `ready` deltaP `13.2775` edge `524.691` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `3792.7681` n `47` status `ready` deltaP `15.4514` edge `315.961` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3792.7681` n `47` status `ready` deltaP `15.4514` edge `315.961` maxDD `0.0`
- `news_risk_high->unknown_1h` score `382.9516` n `82` status `ready` deltaP `-5.6996` edge `31.9928` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.1855` n `62` status `ready` deltaP `51.7305` edge `1.6773` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.5234` n `47` status `ready` deltaP `39.5353` edge `1.2197` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.5234` n `47` status `ready` deltaP `39.5353` edge `1.2197` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `16.9951` n `62` status `ready` deltaP `27.593` edge `1.2811` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.3649` n `92` status `ready` deltaP `32.7823` edge `1.1446` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `11.417` n `62` status `ready` deltaP `31.5188` edge `0.769` maxDD `-1.2164`
- `risk_on_high->equity_24h` score `9.3131` n `47` status `ready` deltaP `39.5833` edge `0.5122` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3131` n `47` status `ready` deltaP `39.5833` edge `0.5122` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0083` n `92` status `ready` deltaP `39.5833` edge `0.4868` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5924` n `47` status `ready` deltaP `41.9402` edge `0.4736` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5924` n `47` status `ready` deltaP `41.9402` edge `0.4736` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.7597` n `62` status `ready` deltaP `49.8488` edge `0.3302` maxDD `-0.2708`
- `news_risk_high->index_24h` score `7.3959` n `62` status `ready` deltaP `47.8383` edge `0.3109` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.878` n `47` status `ready` deltaP `49.5198` edge `0.0806` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.878` n `47` status `ready` deltaP `49.5198` edge `0.0806` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1335` n `47` status `ready` deltaP `36.6114` edge `0.1097` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
