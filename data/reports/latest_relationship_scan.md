# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T02:07:25.179279+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11368`

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

- `news_risk_high->unknown_1h` score `1171.4653` n `45` status `ready` deltaP `-6.4338` edge `97.7004` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `760.6375` n `33` status `ready` deltaP `-22.4177` edge `63.6003` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.5136` n `91` status `ready` deltaP `36.1722` edge `1.4913` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.5136` n `91` status `ready` deltaP `36.1722` edge `1.4913` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `16.4043` n `197` status `ready` deltaP `29.484` edge `1.2532` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0335` n `91` status `ready` deltaP `42.0983` edge `0.5093` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0335` n `91` status `ready` deltaP `42.0983` edge `0.5093` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.1864` n `197` status `ready` deltaP `29.3403` edge `0.4866` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8213` n `91` status `ready` deltaP `32.8113` edge `0.5189` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8213` n `91` status `ready` deltaP `32.8113` edge `0.5189` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2425` n `91` status `ready` deltaP `25.021` edge `1.1685` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2425` n `91` status `ready` deltaP `25.021` edge `1.1685` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.7596` n `91` status `ready` deltaP `29.3403` edge `0.3677` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.7596` n `91` status `ready` deltaP `29.3403` edge `0.3677` maxDD `0.0`
- `risk_on_high->index_24h` score `4.7977` n `91` status `ready` deltaP `45.1408` edge `0.1031` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.7977` n `91` status `ready` deltaP `45.1408` edge `0.1031` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.8886` n `197` status `ready` deltaP `39.3004` edge `0.1014` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5672` n `91` status `ready` deltaP `33.1932` edge `0.0853` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5672` n `91` status `ready` deltaP `33.1932` edge `0.0853` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.3668` n `197` status `ready` deltaP `26.081` edge `0.1089` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
