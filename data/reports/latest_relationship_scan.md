# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T04:22:28.575034+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11414`

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

- `news_risk_high->unknown_1h` score `865.3566` n `54` status `ready` deltaP `-8.5773` edge `72.2124` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `514.04` n `42` status `ready` deltaP `-27.6278` edge `43.101` maxDD `-3.412`
- `risk_on_high->crypto_alt_24h` score `20.9074` n `91` status `ready` deltaP `36.5194` edge `1.5218` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.9074` n `91` status `ready` deltaP `36.5194` edge `1.5218` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.8041` n `188` status `ready` deltaP `32.9713` edge `1.3466` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9113` n `91` status `ready` deltaP `41.3361` edge `0.5042` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9113` n `91` status `ready` deltaP `41.3361` edge `0.5042` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.543` n `188` status `ready` deltaP `30.9028` edge `0.5059` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.7511` n `91` status `ready` deltaP `32.3539` edge `0.5161` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7511` n `91` status `ready` deltaP `32.3539` edge `0.5161` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `7.4774` n `91` status `ready` deltaP `30.9028` edge `0.4171` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.4774` n `91` status `ready` deltaP `30.9028` edge `0.4171` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.2955` n `91` status `ready` deltaP `25.021` edge `1.1753` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2955` n `91` status `ready` deltaP `25.021` edge `1.1753` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.0091` n `91` status `ready` deltaP `46.7033` edge `0.1103` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0091` n `91` status `ready` deltaP `46.7033` edge `0.1103` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.0278` n `188` status `ready` deltaP `40.4255` edge `0.1055` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6982` n `91` status `ready` deltaP `34.2603` edge `0.0891` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6982` n `91` status `ready` deltaP `34.2603` edge `0.0891` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5244` n `188` status `ready` deltaP `27.5558` edge `0.1122` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
