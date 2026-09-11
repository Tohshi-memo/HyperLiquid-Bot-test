# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T10:52:27.942106+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12406`

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

- `news_risk_high->unknown_1h` score `750.9425` n `59` status `ready` deltaP `-6.2088` edge `62.6621` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `22.4174` n `91` status `ready` deltaP `40.8597` edge `1.6187` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.4174` n `91` status `ready` deltaP `40.8597` edge `1.6187` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.9362` n `164` status `ready` deltaP `36.5981` edge `1.5001` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.2605` n `164` status `ready` deltaP `35.4167` edge `0.5356` maxDD `0.0`
- `risk_on_high->equity_24h` score `9.0997` n `91` status `ready` deltaP `35.4167` edge `0.5222` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0997` n `91` status `ready` deltaP `35.4167` edge `0.5222` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7421` n `91` status `ready` deltaP `41.3361` edge `0.4901` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7421` n `91` status `ready` deltaP `41.3361` edge `0.4901` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.3563` n `91` status `ready` deltaP `25.021` edge `1.1831` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3563` n `91` status `ready` deltaP `25.021` edge `1.1831` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `7.2543` n `91` status `ready` deltaP `31.4393` edge `0.4808` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.2543` n `91` status `ready` deltaP `31.4393` edge `0.4808` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.5238` n `91` status `ready` deltaP `51.2172` edge `0.1231` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.5238` n `91` status `ready` deltaP `51.2172` edge `0.1231` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3992` n `164` status `ready` deltaP `43.5383` edge `0.1157` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.4962` n `91` status `ready` deltaP `33.9554` edge `0.0743` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.4962` n `91` status `ready` deltaP `33.9554` edge `0.0743` maxDD `-0.079`
- `market_context_high->crypto_alt_4h` score `2.408` n `164` status `ready` deltaP `21.3415` edge `0.2698` maxDD `-10.9127`
- `market_context_high->equity_4h` score `2.3878` n `164` status `ready` deltaP `27.7439` edge `0.0967` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
