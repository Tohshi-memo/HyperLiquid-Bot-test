# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T17:37:28.361687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6617`

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

- `market_context_high->unknown_24h` score `7203.2935` n `55` status `ready` deltaP `1.3889` edge `600.2652` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.225` n `55` status `ready` deltaP `6.2611` edge `31.648` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `66.5534` n `55` status `ready` deltaP `4.2107` edge `5.5291` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1108` n `55` status `ready` deltaP `42.7999` edge `1.4975` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1952` n `94` status `ready` deltaP `30.9619` edge `1.0288` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5998` n `55` status `ready` deltaP `53.4722` edge `0.1935` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.27` n `55` status `ready` deltaP `44.0531` edge `0.2599` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1714` n `55` status `ready` deltaP `24.5122` edge `0.3803` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6793` n `55` status `ready` deltaP `31.3498` edge `0.2979` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5092` n `55` status `ready` deltaP `6.2001` edge `0.3213` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3539` n `55` status `ready` deltaP `31.5244` edge `0.0944` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.7417` n `124` status `ready` deltaP `11.4477` edge `0.2908` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3536` n `55` status `ready` deltaP `9.9906` edge `0.3028` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8872` n `55` status `ready` deltaP `-4.2992` edge `0.4224` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6884` n `55` status `ready` deltaP `19.7228` edge `0.0517` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5776` n `55` status `ready` deltaP `3.4758` edge `0.1608` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.4866` n `55` status `ready` deltaP `4.5237` edge `0.1608` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4695` n `55` status `ready` deltaP `8.6309` edge `0.1259` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9762` n `55` status `ready` deltaP `12.074` edge `0.0257` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5553` n `55` status `ready` deltaP `13.4867` edge `-0.0003` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
