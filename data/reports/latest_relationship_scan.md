# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T01:37:29.303919+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7517`

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

- `market_context_high->unknown_24h` score `7660.1419` n `54` status `ready` deltaP `1.3889` edge `638.3359` maxDD `0.0`
- `market_context_high->unknown_4h` score `344.7783` n `54` status `ready` deltaP `7.4469` edge `28.6862` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `27.5576` n `57` status `ready` deltaP `4.8929` edge `2.2749` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.2617` n `54` status `ready` deltaP `42.7662` edge `1.5103` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.5482` n `94` status `ready` deltaP `32.5244` edge `1.0478` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1686` n `54` status `ready` deltaP `49.1319` edge `0.1865` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1628` n `54` status `ready` deltaP `25.0791` edge `0.3758` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.913` n `54` status `ready` deltaP `40.625` edge `0.253` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.5446` n `54` status `ready` deltaP `31.5267` edge `0.2855` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.1866` n `54` status `ready` deltaP `30.262` edge `0.0847` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.045` n `54` status `ready` deltaP `4.3586` edge `0.2949` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4019` n `54` status `ready` deltaP `10.1852` edge `0.3077` maxDD `-3.0799`
- `news_risk_high->crypto_alt_4h` score `2.2968` n `126` status `ready` deltaP `9.4706` edge `0.2669` maxDD `-7.4246`
- `market_context_high->crypto_alt_24h` score `2.0639` n `54` status `ready` deltaP `-3.6458` edge `0.4407` maxDD `-8.8096`
- `market_context_high->equity_1h` score `1.8304` n `57` status `ready` deltaP `5.841` edge `0.1661` maxDD `-1.5336`
- `market_context_high->metal_4h` score `1.6912` n `54` status `ready` deltaP `19.9977` edge `0.0501` maxDD `-0.7323`
- `market_context_high->crypto_major_1h` score `1.2339` n `57` status `ready` deltaP `5.841` edge `0.1179` maxDD `-1.6544`
- `market_context_high->crypto_alt_1h` score `1.1054` n `57` status `ready` deltaP `1.476` edge `0.1435` maxDD `-2.2314`
- `market_context_high->metal_1h` score `0.9257` n `57` status `ready` deltaP `11.4875` edge `0.0254` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.7296` n `57` status `ready` deltaP `16.0679` edge `0.0045` maxDD `-0.1128`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
