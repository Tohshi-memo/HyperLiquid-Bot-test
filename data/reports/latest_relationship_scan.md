# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T10:37:34.917983+00:00`
- Price records: `672`
- Market context records: `3983`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `147.4799` n `40` status `ready` deltaP `-0.8841` edge `12.4771` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.4799` n `40` status `ready` deltaP `-0.8841` edge `12.4771` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `31.8513` n `151` status `ready` deltaP `-7.141` edge `3.2055` maxDD `-32.2896`
- `market_context_high->unknown_4h` score `19.8958` n `164` status `ready` deltaP `0.7622` edge `2.1938` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2927` n `40` status `ready` deltaP `42.0139` edge `0.4943` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2927` n `40` status `ready` deltaP `42.0139` edge `0.4943` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.7423` n `40` status `ready` deltaP `37.439` edge `0.067` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.7423` n `40` status `ready` deltaP `37.439` edge `0.067` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.5068` n `151` status `ready` deltaP `16.9254` edge `0.3309` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.328` n `151` status `ready` deltaP `25.8876` edge `0.2187` maxDD `-7.1159`
- `market_context_high->equity_24h` score `2.8943` n `151` status `ready` deltaP `18.8351` edge `0.4186` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8065` n `40` status `ready` deltaP `29.8611` edge `0.0348` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8065` n `40` status `ready` deltaP `29.8611` edge `0.0348` maxDD `0.0`
- `market_context_high->equity_4h` score `2.5262` n `164` status `ready` deltaP `20.4268` edge `0.2046` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.1695` n `164` status `ready` deltaP `19.2073` edge `0.2094` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9486` n `40` status `ready` deltaP `20.9756` edge `0.0891` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9486` n `40` status `ready` deltaP `20.9756` edge `0.0891` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.5196` n `164` status `ready` deltaP `11.9176` edge `0.1014` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1116` n `164` status `ready` deltaP `9.5772` edge `0.0852` maxDD `-2.1799`
- `market_context_high->crypto_alt_4h` score `0.9562` n `164` status `ready` deltaP `13.567` edge `0.1197` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
