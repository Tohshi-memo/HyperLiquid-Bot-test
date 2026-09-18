# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T04:52:58.911846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8616`

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

- `market_context_high->unknown_4h` score `40.0504` n `149` status `ready` deltaP `-0.0061` edge `3.3609` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9291` n `52` status `ready` deltaP `-7.2467` edge `1.2316` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9291` n `52` status `ready` deltaP `-7.2467` edge `1.2316` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9512` n `52` status `ready` deltaP `50.0` edge `0.4126` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9512` n `52` status `ready` deltaP `50.0` edge `0.4126` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6521` n `149` status `ready` deltaP `43.2886` edge `0.4016` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.9401` n `52` status `ready` deltaP `32.9972` edge `0.06` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9401` n `52` status `ready` deltaP `32.9972` edge `0.06` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8398` n `149` status `ready` deltaP `29.4995` edge `0.0818` maxDD `-0.345`
- `news_risk_high->crypto_alt_24h` score `2.7402` n `31` status `ready` deltaP `22.2838` edge `0.2177` maxDD `-9.3661`
- `news_risk_high->index_24h` score `2.0098` n `31` status `ready` deltaP `16.0786` edge `0.0779` maxDD `-0.075`
- `news_risk_high->crypto_alt_4h` score `1.7098` n `68` status `ready` deltaP `13.6837` edge `0.3536` maxDD `-13.05`
- `risk_on_high->fx_24h` score `1.3858` n `52` status `ready` deltaP `22.3825` edge `-0.0295` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.3858` n `52` status `ready` deltaP `22.3825` edge `-0.0295` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.2509` n `149` status `ready` deltaP `19.6076` edge `-0.0049` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2415` n `149` status `ready` deltaP `17.2588` edge `0.0261` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6183` n `52` status `ready` deltaP `10.3409` edge `0.0178` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6183` n `52` status `ready` deltaP `10.3409` edge `0.0178` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4293` n `68` status `ready` deltaP `9.7292` edge `0.0546` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.1571` n `78` status `ready` deltaP `8.2067` edge `0.0176` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
