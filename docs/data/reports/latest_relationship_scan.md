# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T20:07:31.801607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9004`

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

- `news_risk_high->unknown_4h` score `429.6978` n `76` status `ready` deltaP `-15.4926` edge `35.9884` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.292` n `52` status `ready` deltaP `50.0` edge `0.441` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.292` n `52` status `ready` deltaP `50.0` edge `0.441` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.39` n `66` status `ready` deltaP `29.2613` edge `0.642` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9929` n `149` status `ready` deltaP `43.2886` edge `0.43` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.0454` n `66` status `ready` deltaP `24.8737` edge `0.5987` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.1232` n `66` status `ready` deltaP `34.8958` edge `0.2119` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.7155` n `66` status `ready` deltaP `17.0928` edge `0.6901` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.2591` n `66` status `ready` deltaP `23.911` edge `0.1576` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `3.0243` n `52` status `ready` deltaP `33.1496` edge `0.066` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0243` n `52` status `ready` deltaP `33.1496` edge `0.066` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.924` n `149` status `ready` deltaP `29.6519` edge `0.0878` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8835` n `52` status `ready` deltaP `26.5491` edge `-0.0158` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8835` n `52` status `ready` deltaP `26.5491` edge `-0.0158` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.7486` n `149` status `ready` deltaP `23.7742` edge `0.0088` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.4766` n `76` status `ready` deltaP `21.0206` edge `0.0295` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.22` n `149` status `ready` deltaP `16.9594` edge `0.0263` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5967` n `52` status `ready` deltaP `10.0415` edge `0.018` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5967` n `52` status `ready` deltaP `10.0415` edge `0.018` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2135` n `149` status `ready` deltaP `10.4957` edge `0.005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
