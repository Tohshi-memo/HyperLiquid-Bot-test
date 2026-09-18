# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T02:52:27.758157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8568`

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

- `market_context_high->unknown_4h` score `36.3604` n `149` status `ready` deltaP `-0.0061` edge `3.0534` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `17.7266` n `68` status `ready` deltaP `-7.5861` edge `1.556` maxDD `-0.9232`
- `risk_on_high->unknown_4h` score `10.2391` n `52` status `ready` deltaP `-7.2467` edge `0.9241` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.2391` n `52` status `ready` deltaP `-7.2467` edge `0.9241` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0148` n `52` status `ready` deltaP `50.0` edge `0.4179` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0148` n `52` status `ready` deltaP `50.0` edge `0.4179` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.7157` n `149` status `ready` deltaP `43.2886` edge `0.4069` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `6.8957` n `39` status `ready` deltaP `27.5775` edge `0.5287` maxDD `-9.3661`
- `news_risk_high->index_24h` score `3.2365` n `39` status `ready` deltaP `23.3574` edge `0.1316` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0149` n `52` status `ready` deltaP `33.3021` edge `0.0642` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0149` n `52` status `ready` deltaP `33.3021` edge `0.0642` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9146` n `149` status `ready` deltaP `29.8044` edge `0.086` maxDD `-0.345`
- `news_risk_high->equity_24h` score `2.0685` n `39` status `ready` deltaP `0.7478` edge `0.3448` maxDD `-6.5262`
- `risk_on_high->fx_24h` score `1.5497` n `52` status `ready` deltaP `23.7713` edge `-0.0251` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.5497` n `52` status `ready` deltaP `23.7713` edge `-0.0251` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.4148` n `149` status `ready` deltaP `20.9964` edge `-0.0005` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2308` n `149` status `ready` deltaP `17.1091` edge `0.0262` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7113` n `68` status `ready` deltaP `9.7292` edge `0.0781` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.6075` n `52` status `ready` deltaP `10.1912` edge `0.0179` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6075` n `52` status `ready` deltaP `10.1912` edge `0.0179` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
