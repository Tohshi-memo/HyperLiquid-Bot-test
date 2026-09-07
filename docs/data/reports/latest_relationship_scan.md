# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T19:37:26.612687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10225`

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

- `risk_on_high->unknown_24h` score `150.6001` n `109` status `ready` deltaP `22.3958` edge `12.4007` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `150.6001` n `109` status `ready` deltaP `22.3958` edge `12.4007` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `13.1933` n `109` status `ready` deltaP `26.3698` edge `1.1791` maxDD `-15.1034`
- `risk_on_and_context->crypto_major_24h` score `13.1933` n `109` status `ready` deltaP `26.3698` edge `1.1791` maxDD `-15.1034`
- `risk_on_high->crypto_alt_24h` score `11.6288` n `109` status `ready` deltaP `29.4151` edge `0.7791` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.6288` n `109` status `ready` deltaP `29.4151` edge `0.7791` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.835` n `222` status `ready` deltaP `23.1419` edge `0.4728` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7752` n `117` status `ready` deltaP `30.635` edge `0.3142` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7752` n `117` status `ready` deltaP `30.635` edge `0.3142` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.0187` n `117` status `ready` deltaP `26.7433` edge `0.3258` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0187` n `117` status `ready` deltaP `26.7433` edge `0.3258` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.7024` n `222` status `ready` deltaP `14.9306` edge `0.209` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.8972` n `109` status `ready` deltaP `14.9306` edge `0.1419` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.8972` n `109` status `ready` deltaP `14.9306` edge `0.1419` maxDD `0.0`
- `risk_on_high->index_24h` score `1.8594` n `109` status `ready` deltaP `16.6921` edge `0.0479` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.8594` n `109` status `ready` deltaP `16.6921` edge `0.0479` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.1199` n `222` status `ready` deltaP `11.3363` edge `0.0571` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9861` n `117` status `ready` deltaP `4.5461` edge `0.0871` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9861` n `117` status `ready` deltaP `4.5461` edge `0.0871` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.5253` n `117` status `ready` deltaP `14.3726` edge `0.0011` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
