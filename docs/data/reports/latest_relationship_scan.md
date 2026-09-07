# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T20:52:30.014345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10353`

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

- `risk_on_high->unknown_24h` score `1982.9135` n `112` status `ready` deltaP `22.0486` edge `165.0958` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1982.9135` n `112` status `ready` deltaP `22.0486` edge `165.0958` maxDD `0.0`
- `market_context_high->unknown_24h` score `548.1219` n `227` status `ready` deltaP `21.1675` edge `45.5409` maxDD `-0.0819`
- `risk_on_high->crypto_major_24h` score `11.4408` n `112` status `ready` deltaP `24.3056` edge `1.0949` maxDD `-17.9494`
- `risk_on_and_context->crypto_major_24h` score `11.4408` n `112` status `ready` deltaP `24.3056` edge `1.0949` maxDD `-17.9494`
- `risk_on_high->crypto_alt_24h` score `11.0089` n `112` status `ready` deltaP `28.5962` edge `0.7329` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.0089` n `112` status `ready` deltaP `28.5962` edge `0.7329` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.415` n `227` status `ready` deltaP `22.4524` edge `0.4424` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7644` n `117` status `ready` deltaP `30.635` edge `0.3133` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7644` n `117` status `ready` deltaP `30.635` edge `0.3133` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9123` n `117` status `ready` deltaP `26.1335` edge `0.321` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9123` n `117` status `ready` deltaP `26.1335` edge `0.321` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.309` n `227` status `ready` deltaP `14.0625` edge `0.182` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.5062` n `112` status `ready` deltaP `14.0625` edge `0.1151` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.5062` n `112` status `ready` deltaP `14.0625` edge `0.1151` maxDD `0.0`
- `risk_on_high->index_24h` score `1.7443` n `112` status `ready` deltaP `15.8978` edge `0.0436` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.7443` n `112` status `ready` deltaP `15.8978` edge `0.0436` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.0119` n `227` status `ready` deltaP `10.6469` edge `0.0527` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9681` n `117` status `ready` deltaP `4.3964` edge `0.0866` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9681` n `117` status `ready` deltaP `4.3964` edge `0.0866` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
