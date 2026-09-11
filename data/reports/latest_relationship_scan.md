# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T02:52:30.121773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11394`

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

- `news_risk_high->unknown_1h` score `1055.7655` n `48` status `ready` deltaP `-8.6452` edge `88.0735` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `976.7975` n `36` status `ready` deltaP `-23.628` edge `81.6217` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.6415` n `91` status `ready` deltaP `36.3458` edge `1.5008` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.6415` n `91` status `ready` deltaP `36.3458` edge `1.5008` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `16.836` n `194` status `ready` deltaP `30.5001` edge `1.2824` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0299` n `91` status `ready` deltaP `42.0983` edge `0.509` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0299` n `91` status `ready` deltaP `42.0983` edge `0.509` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.2869` n `194` status `ready` deltaP `29.8611` edge `0.4915` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8491` n `91` status `ready` deltaP `32.9637` edge `0.5202` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8491` n `91` status `ready` deltaP `32.9637` edge `0.5202` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2596` n `91` status `ready` deltaP `25.021` edge `1.1707` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2596` n `91` status `ready` deltaP `25.021` edge `1.1707` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.9909` n `91` status `ready` deltaP `29.8611` edge `0.3835` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.9909` n `91` status `ready` deltaP `29.8611` edge `0.3835` maxDD `0.0`
- `risk_on_high->index_24h` score `4.8682` n `91` status `ready` deltaP `45.6616` edge `0.1055` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8682` n `91` status `ready` deltaP `45.6616` edge `0.1055` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.9321` n `194` status `ready` deltaP `39.6799` edge `0.1025` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6024` n `91` status `ready` deltaP `33.4981` edge `0.0862` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6024` n `91` status `ready` deltaP `33.4981` edge `0.0862` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.4311` n `194` status `ready` deltaP `26.6894` edge `0.1102` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
