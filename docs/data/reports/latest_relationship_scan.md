# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T05:07:24.766415+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12280`

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

- `news_risk_high->unknown_1h` score `796.4892` n `57` status `ready` deltaP `-7.0701` edge `66.4634` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `328.8147` n `45` status `ready` deltaP `-30.1863` edge `27.6918` maxDD `-4.1464`
- `risk_on_high->crypto_alt_24h` score `21.0167` n `91` status `ready` deltaP `36.8666` edge `1.5286` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.0167` n `91` status `ready` deltaP `36.8666` edge `1.5286` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.1239` n `186` status `ready` deltaP `33.7589` edge `1.368` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8811` n `91` status `ready` deltaP `41.1837` edge `0.5027` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8811` n `91` status `ready` deltaP `41.1837` edge `0.5027` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.7047` n `186` status `ready` deltaP `31.4236` edge `0.5159` maxDD `0.0`
- `risk_on_high->equity_24h` score `7.7015` n `91` status `ready` deltaP `31.4236` edge `0.4323` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.7015` n `91` status `ready` deltaP `31.4236` edge `0.4323` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6979` n `91` status `ready` deltaP `32.0491` edge `0.5137` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6979` n `91` status `ready` deltaP `32.0491` edge `0.5137` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2846` n `91` status `ready` deltaP `25.021` edge `1.1739` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2846` n `91` status `ready` deltaP `25.021` edge `1.1739` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.0748` n `91` status `ready` deltaP `47.2241` edge `0.1123` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0748` n `91` status `ready` deltaP `47.2241` edge `0.1123` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.0852` n `186` status `ready` deltaP `40.8434` edge `0.1075` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.7504` n `91` status `ready` deltaP `34.7176` edge `0.0904` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.7504` n `91` status `ready` deltaP `34.7176` edge `0.0904` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5604` n `186` status `ready` deltaP `27.8701` edge `0.1131` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
