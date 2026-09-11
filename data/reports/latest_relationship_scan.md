# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T03:22:35.300574+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11396`

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

- `news_risk_high->unknown_1h` score `986.2399` n `50` status `ready` deltaP `-11.0958` edge `82.3028` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `806.0484` n `38` status `ready` deltaP `-25.9548` edge `67.4087` maxDD `-2.1975`
- `risk_on_high->crypto_alt_24h` score `20.7315` n `91` status `ready` deltaP `36.3458` edge `1.5083` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.7315` n `91` status `ready` deltaP `36.3458` edge `1.5083` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.1942` n `192` status `ready` deltaP `31.4236` edge `1.3061` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0045` n `91` status `ready` deltaP `41.9459` edge `0.5079` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0045` n `91` status `ready` deltaP `41.9459` edge `0.5079` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.3723` n `192` status `ready` deltaP `30.2083` edge `0.4963` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8431` n `91` status `ready` deltaP `32.9637` edge `0.5197` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8431` n `91` status `ready` deltaP `32.9637` edge `0.5197` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.276` n `91` status `ready` deltaP `25.021` edge `1.1728` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.276` n `91` status `ready` deltaP `25.021` edge `1.1728` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `7.1543` n `91` status `ready` deltaP `30.2083` edge `0.3948` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.1543` n `91` status `ready` deltaP `30.2083` edge `0.3948` maxDD `0.0`
- `risk_on_high->index_24h` score `4.9163` n `91` status `ready` deltaP `46.0089` edge `0.1072` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9163` n `91` status `ready` deltaP `46.0089` edge `0.1072` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.963` n `192` status `ready` deltaP `39.9306` edge `0.1034` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6218` n `91` status `ready` deltaP `33.6505` edge `0.0868` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6218` n `91` status `ready` deltaP `33.6505` edge `0.0868` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.4918` n `192` status `ready` deltaP `27.2231` edge `0.1117` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
