# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T00:37:26.281260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10313`

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

- `market_context_high->unknown_24h` score `3386.5965` n `241` status `ready` deltaP `19.1354` edge `282.094` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `3357.288` n `117` status `ready` deltaP `19.9653` edge `279.6409` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3357.288` n `117` status `ready` deltaP `19.9653` edge `279.6409` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.5009` n `117` status `ready` deltaP `25.414` edge `0.6453` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.5009` n `117` status `ready` deltaP `25.414` edge `0.6453` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9492` n `117` status `ready` deltaP `31.5497` edge `0.3226` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9492` n `117` status `ready` deltaP `31.5497` edge `0.3226` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.3234` n `117` status `ready` deltaP `21.1005` edge `0.9486` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3234` n `117` status `ready` deltaP `21.1005` edge `0.9486` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8833` n `117` status `ready` deltaP `25.9811` edge `0.3196` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8833` n `117` status `ready` deltaP `25.9811` edge `0.3196` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.4535` n `241` status `ready` deltaP `18.0692` edge `0.3334` maxDD `-3.9523`
- `market_context_high->equity_24h` score `2.0927` n `241` status `ready` deltaP `11.4583` edge `0.098` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.4075` n `117` status `ready` deltaP `11.4583` edge `0.0409` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4075` n `117` status `ready` deltaP `11.4583` edge `0.0409` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4035` n `117` status `ready` deltaP `13.4081` edge `0.0318` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.4035` n `117` status `ready` deltaP `13.4081` edge `0.0318` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9993` n `117` status `ready` deltaP `4.3964` edge `0.0892` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9993` n `117` status `ready` deltaP `4.3964` edge `0.0892` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.682` n `241` status `ready` deltaP `8.5033` edge `0.0395` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
