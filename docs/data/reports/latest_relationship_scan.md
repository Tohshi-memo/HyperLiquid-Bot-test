# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T03:07:30.394506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `377.9124` n `83` status `ready` deltaP `-20.9007` edge `31.7215` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.5224` n `83` status `ready` deltaP `38.3513` edge `1.2591` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.1222` n `83` status `ready` deltaP `30.4175` edge `1.2569` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.3283` n `83` status `ready` deltaP `39.6503` edge `0.8571` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.7039` n `52` status `ready` deltaP `43.2292` edge `0.3538` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7039` n `52` status `ready` deltaP `43.2292` edge `0.3538` maxDD `0.0`
- `news_risk_high->index_24h` score `6.4936` n `83` status `ready` deltaP `45.0803` edge `0.2582` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.4048` n `149` status `ready` deltaP `36.5178` edge `0.3428` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.683` n `83` status `ready` deltaP `31.9905` edge `0.2224` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5735` n `52` status `ready` deltaP `33.4936` edge `-0.0046` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5735` n `52` status `ready` deltaP `33.4936` edge `-0.0046` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4386` n `149` status `ready` deltaP `30.7187` edge `0.02` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2222` n `52` status `ready` deltaP `28.1191` edge `0.0327` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2222` n `52` status `ready` deltaP `28.1191` edge `0.0327` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.122` n `149` status `ready` deltaP `24.6214` edge `0.0545` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.918` n `149` status `ready` deltaP `14.4145` edge `0.0181` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3651` n `83` status `ready` deltaP `11.736` edge `0.0314` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2947` n `52` status `ready` deltaP `7.4966` edge `0.0098` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2947` n `52` status `ready` deltaP `7.4966` edge `0.0098` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.156` n `52` status `ready` deltaP `6.4141` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
