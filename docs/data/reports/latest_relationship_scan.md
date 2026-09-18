# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T03:37:35.094771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_4h` score `37.69` n `149` status `ready` deltaP `-0.0061` edge `3.1642` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.5687` n `52` status `ready` deltaP `-7.2467` edge `1.0349` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.5687` n `52` status `ready` deltaP `-7.2467` edge `1.0349` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.992` n `52` status `ready` deltaP `50.0` edge `0.416` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.992` n `52` status `ready` deltaP `50.0` edge `0.416` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6929` n `149` status `ready` deltaP `43.2886` edge `0.405` maxDD `-0.8682`
- `news_risk_high->unknown_4h` score `6.2294` n `68` status `ready` deltaP `-7.5861` edge `0.5979` maxDD `-0.9232`
- `news_risk_high->crypto_alt_24h` score `5.5601` n `36` status `ready` deltaP `25.8681` edge `0.4288` maxDD `-9.3661`
- `risk_on_high->commodity_4h` score `2.9993` n `52` status `ready` deltaP `33.3021` edge `0.0629` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9993` n `52` status `ready` deltaP `33.3021` edge `0.0629` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.899` n `149` status `ready` deltaP `29.8044` edge `0.0847` maxDD `-0.345`
- `news_risk_high->index_24h` score `2.8601` n `36` status `ready` deltaP `21.0069` edge `0.1159` maxDD `-0.075`
- `risk_on_high->fx_24h` score `1.4876` n `52` status `ready` deltaP `23.2505` edge `-0.0268` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.4876` n `52` status `ready` deltaP `23.2505` edge `-0.0268` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.3528` n `149` status `ready` deltaP `20.4756` edge `-0.0022` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2463` n `149` status `ready` deltaP `17.2588` edge `0.0265` maxDD `-0.3491`
- `news_risk_high->equity_24h` score `0.9505` n `36` status `ready` deltaP `-4.1667` edge `0.2844` maxDD `-6.5262`
- `news_risk_high->crypto_alt_4h` score `0.8057` n `68` status `ready` deltaP `13.6837` edge `0.2377` maxDD `-13.05`
- `news_risk_high->equity_4h` score `0.6237` n `68` status `ready` deltaP `9.7292` edge `0.0708` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.6231` n `52` status `ready` deltaP `10.3409` edge `0.0182` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
