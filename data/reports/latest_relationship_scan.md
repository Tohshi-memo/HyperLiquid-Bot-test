# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T03:22:31.145832+00:00`
- Price records: `672`
- Market context records: `4788`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `7.6968` n `122` status `ready` deltaP `12.8792` edge `0.5973` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.6683` n `122` status `ready` deltaP `18.4152` edge `0.6373` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.976` n `107` status `ready` deltaP `11.52` edge `0.1802` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1525` n `122` status `ready` deltaP `5.6812` edge `0.0336` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0823` n `122` status `ready` deltaP `11.8153` edge `0.049` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.2844` n `122` status `ready` deltaP `7.6245` edge `0.0813` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4322` n `122` status `ready` deltaP `6.385` edge `0.0089` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4614` n `122` status `ready` deltaP `2.5165` edge `0.0017` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7463` n `122` status `ready` deltaP `1.2688` edge `0.0061` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9112` n `122` status `ready` deltaP `-1.1829` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.4063` n `122` status `ready` deltaP `-1.6467` edge `-0.0058` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2592` n `107` status `ready` deltaP `19.055` edge `0.0942` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.261` n `122` status `ready` deltaP `-0.7976` edge `-0.067` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.0812` n `122` status `ready` deltaP `0.8982` edge `-0.0388` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.4374` n `107` status `ready` deltaP `-16.2887` edge `-0.0229` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4047` n `122` status `ready` deltaP `0.6847` edge `-0.0626` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.8808` n `122` status `ready` deltaP `4.2883` edge `-0.0119` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.651` n `107` status `ready` deltaP `-5.1029` edge `-0.1035` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.1812` n `122` status `ready` deltaP `3.0488` edge `-0.1461` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.4294` n `122` status `ready` deltaP `5.7727` edge `-0.2951` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
