# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T18:07:26.772926+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6619`

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

- `market_context_high->unknown_24h` score `7235.6707` n `55` status `ready` deltaP `1.3889` edge `602.9633` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.3286` n `55` status `ready` deltaP `6.5659` edge `31.6546` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `60.917` n `55` status `ready` deltaP `4.2107` edge `5.0594` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1276` n `55` status `ready` deltaP `42.7999` edge `1.4989` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1964` n `94` status `ready` deltaP `30.9619` edge `1.0289` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5648` n `55` status `ready` deltaP `53.125` edge `0.1929` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2326` n `55` status `ready` deltaP `43.7058` edge `0.2591` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1642` n `55` status `ready` deltaP `24.5122` edge `0.3797` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6661` n `55` status `ready` deltaP `31.3498` edge `0.2968` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5044` n `55` status `ready` deltaP `6.2001` edge `0.3209` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3527` n `55` status `ready` deltaP `31.5244` edge `0.0943` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.4863` n `126` status `ready` deltaP `10.3852` edge `0.2766` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3665` n `55` status `ready` deltaP `10.1642` edge `0.3033` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.888` n `55` status `ready` deltaP `-4.2992` edge `0.4225` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7018` n `55` status `ready` deltaP `19.8752` edge `0.0518` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6052` n `55` status `ready` deltaP `3.7752` edge `0.1611` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.489` n `55` status `ready` deltaP `4.5237` edge `0.161` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4707` n `55` status `ready` deltaP `8.6309` edge `0.126` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9642` n `55` status `ready` deltaP `11.9243` edge `0.0257` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5467` n `55` status `ready` deltaP `13.337` edge `-0.0004` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
