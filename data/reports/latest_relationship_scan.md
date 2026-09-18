# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T07:07:27.800260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8260`

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

- `market_context_high->unknown_4h` score `39.8476` n `149` status `ready` deltaP `-0.0061` edge `3.344` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7263` n `52` status `ready` deltaP `-7.2467` edge `1.2147` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7263` n `52` status `ready` deltaP `-7.2467` edge `1.2147` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8924` n `52` status `ready` deltaP `50.0` edge `0.4077` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8924` n `52` status `ready` deltaP `50.0` edge `0.4077` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5933` n `149` status `ready` deltaP `43.2886` edge `0.3967` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8811` n `52` status `ready` deltaP `32.8447` edge `0.0561` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8811` n `52` status `ready` deltaP `32.8447` edge `0.0561` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7808` n `149` status `ready` deltaP `29.347` edge `0.0779` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.7622` n `72` status `ready` deltaP `17.0393` edge `0.4556` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.2212` n `149` status `ready` deltaP `17.1091` edge `0.0254` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.2128` n `52` status `ready` deltaP `20.82` edge `-0.0335` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.2128` n `52` status `ready` deltaP `20.82` edge `-0.0335` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.0779` n `149` status `ready` deltaP `18.0451` edge `-0.0089` maxDD `-0.0593`
- `news_risk_high->equity_4h` score `0.7471` n `72` status `ready` deltaP `11.7717` edge `0.101` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.5979` n `52` status `ready` deltaP `10.1912` edge `0.0171` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5979` n `52` status `ready` deltaP `10.1912` edge `0.0171` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3814` n `84` status `ready` deltaP `11.3202` edge `0.0256` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1867` n `72` status `ready` deltaP `6.5549` edge `0.0249` maxDD `-0.2398`
- `market_context_high->fx_1h` score `0.0112` n `149` status `ready` deltaP `3.9033` edge `0.0012` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
