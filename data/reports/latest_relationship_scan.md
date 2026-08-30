# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T22:07:23.282814+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11736`

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

- `risk_on_high->crypto_alt_24h` score `24.3991` n `48` status `ready` deltaP `49.4792` edge `1.7034` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `24.3991` n `48` status `ready` deltaP `49.4792` edge `1.7034` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `13.3339` n `48` status `ready` deltaP `37.6736` edge `0.8751` maxDD `-0.5414`
- `risk_on_and_context->crypto_major_24h` score `13.3339` n `48` status `ready` deltaP `37.6736` edge `0.8751` maxDD `-0.5414`
- `risk_on_high->unknown_4h` score `8.6354` n `78` status `ready` deltaP `29.71` edge `0.5644` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.6354` n `78` status `ready` deltaP `29.71` edge `0.5644` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2308` n `48` status `ready` deltaP `69.9653` edge `0.0528` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2308` n `48` status `ready` deltaP `69.9653` edge `0.0528` maxDD `0.0`
- `risk_on_high->metal_24h` score `5.5958` n `48` status `ready` deltaP `49.4791` edge `0.1473` maxDD `-0.201`
- `risk_on_and_context->metal_24h` score `5.5958` n `48` status `ready` deltaP `49.4791` edge `0.1473` maxDD `-0.201`
- `market_context_high->unknown_4h` score `5.0021` n `149` status `ready` deltaP `21.054` edge `0.3235` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.4131` n `117` status `ready` deltaP `35.6971` edge `0.2317` maxDD `-3.1535`
- `risk_on_high->equity_24h` score `4.3843` n `48` status `ready` deltaP `30.382` edge `0.1767` maxDD `-0.1108`
- `risk_on_and_context->equity_24h` score `4.3843` n `48` status `ready` deltaP `30.382` edge `0.1767` maxDD `-0.1108`
- `market_context_high->crypto_major_24h` score `4.0743` n `117` status `ready` deltaP `17.4279` edge `0.4891` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `3.2206` n `88` status `ready` deltaP `10.6084` edge `0.2221` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.2206` n `88` status `ready` deltaP `10.6084` edge `0.2221` maxDD `-0.2885`
- `market_context_high->crypto_alt_24h` score `3.1058` n `117` status `ready` deltaP `15.2912` edge `0.7152` maxDD `-27.517`
- `risk_on_high->crypto_alt_4h` score `2.5786` n `78` status `ready` deltaP `12.6681` edge `0.2211` maxDD `-4.9205`
- `risk_on_and_context->crypto_alt_4h` score `2.5786` n `78` status `ready` deltaP `12.6681` edge `0.2211` maxDD `-4.9205`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
