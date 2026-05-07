# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T21:22:17.155805+00:00`
- Price records: `585`
- Market context records: `685`
- Flow alert records: `1940`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `9.7262` n `146` status `ready` deltaP `24.0916` edge `0.6833` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5446` n `146` status `ready` deltaP `8.5176` edge `0.4934` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1922` n `147` status `ready` deltaP `7.5299` edge `0.0123` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2755` n `149` status `ready` deltaP `2.9521` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5405` n `149` status `ready` deltaP `2.0262` edge `0.0389` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5824` n `149` status `ready` deltaP `0.9573` edge `0.0043` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1668` n `149` status `ready` deltaP `-1.6203` edge `-0.0054` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.266` n `149` status `ready` deltaP `-4.6899` edge `-0.0139` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.373` n `149` status `ready` deltaP `4.5674` edge `-0.0134` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5515` n `147` status `ready` deltaP `3.387` edge `0.0004` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6777` n `149` status `ready` deltaP `5.5494` edge `-0.0045` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7361` n `147` status `ready` deltaP `16.0683` edge `0.1188` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.8494` n `147` status `ready` deltaP `4.9735` edge `0.0697` maxDD `-15.2248`
- `market_context_high->index_24h` score `-1.8528` n `146` status `ready` deltaP `-5.608` edge `0.0825` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.5719` n `147` status `ready` deltaP `-1.0378` edge `0.0078` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-3.2909` n `146` status `ready` deltaP `-7.7503` edge `0.0379` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.3105` n `149` status `ready` deltaP `-4.7765` edge `-0.0481` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.824` n `147` status `ready` deltaP `-6.1911` edge `0.0727` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4737` n `147` status `ready` deltaP `2.2811` edge `-0.2002` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8637` n `146` status `ready` deltaP `-9.7896` edge `-0.0411` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
