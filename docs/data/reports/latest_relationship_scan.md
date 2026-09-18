# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T02:22:54.789466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.6412` n `149` status `ready` deltaP `-0.311` edge `2.9955` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `24.0342` n `68` status `ready` deltaP `-4.9498` edge `2.0572` maxDD `-0.3746`
- `risk_on_high->unknown_4h` score `9.5199` n `52` status `ready` deltaP `-7.5516` edge `0.8662` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5199` n `52` status `ready` deltaP `-7.5516` edge `0.8662` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0316` n `52` status `ready` deltaP `50.0` edge `0.4193` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0316` n `52` status `ready` deltaP `50.0` edge `0.4193` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.7325` n `149` status `ready` deltaP `43.2886` edge `0.4083` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `7.5145` n `41` status `ready` deltaP `28.5781` edge `0.5736` maxDD `-9.3661`
- `news_risk_high->index_24h` score `3.4606` n `41` status `ready` deltaP `24.7332` edge `0.1411` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0233` n `52` status `ready` deltaP `33.3021` edge `0.0649` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0233` n `52` status `ready` deltaP `33.3021` edge `0.0649` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.923` n `149` status `ready` deltaP `29.8044` edge `0.0867` maxDD `-0.345`
- `news_risk_high->equity_24h` score `2.6634` n `41` status `ready` deltaP `3.6246` edge `0.3752` maxDD `-6.5262`
- `risk_on_high->fx_24h` score `1.5859` n `52` status `ready` deltaP `24.1186` edge `-0.0244` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.5859` n `52` status `ready` deltaP `24.1186` edge `-0.0244` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.451` n `149` status `ready` deltaP `21.3437` edge `0.0002` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2439` n `149` status `ready` deltaP `17.2588` edge `0.0263` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7353` n `68` status `ready` deltaP `9.7292` edge `0.0801` maxDD `-3.3619`
- `news_risk_high->metal_24h` score `0.735` n `41` status `ready` deltaP `4.5097` edge `0.0766` maxDD `-0.6334`
- `risk_on_high->commodity_1h` score `0.6207` n `52` status `ready` deltaP `10.3409` edge `0.018` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
