# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T21:22:30.444919+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6821`

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

- `market_context_high->unknown_24h` score `7440.3379` n `55` status `ready` deltaP `1.3889` edge `620.0189` maxDD `0.0`
- `market_context_high->unknown_4h` score `351.0278` n `55` status `ready` deltaP `7.1757` edge `29.2088` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `43.6838` n `55` status `ready` deltaP `4.2107` edge `3.6233` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.214` n `55` status `ready` deltaP `42.7999` edge `1.5061` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2384` n `94` status `ready` deltaP `30.9619` edge `1.0324` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.3422` n `55` status `ready` deltaP `50.8681` edge `0.1894` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2554` n `55` status `ready` deltaP `24.5122` edge `0.3873` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `6.003` n `55` status `ready` deltaP `41.7961` edge `0.2527` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6901` n `55` status `ready` deltaP `31.3498` edge `0.2988` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.4901` n `55` status `ready` deltaP `6.3525` edge `0.3187` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.1978` n `55` status `ready` deltaP `30.4573` edge `0.0885` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5775` n `126` status `ready` deltaP `10.3852` edge `0.2842` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4115` n `55` status `ready` deltaP `10.685` edge `0.3056` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9153` n `55` status `ready` deltaP `-4.2992` edge `0.426` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7735` n `55` status `ready` deltaP `20.6374` edge `0.0527` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5932` n `55` status `ready` deltaP `3.6255` edge `0.1611` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4444` n `55` status `ready` deltaP `8.3315` edge `0.1258` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.4363` n `55` status `ready` deltaP `3.9249` edge `0.1606` maxDD `-2.3659`
- `market_context_high->metal_1h` score `1.0049` n `55` status `ready` deltaP `12.3734` edge `0.0261` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5809` n `55` status `ready` deltaP `13.9358` edge `0.0` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
