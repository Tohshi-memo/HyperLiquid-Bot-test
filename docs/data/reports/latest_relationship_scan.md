# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T12:52:24.645903+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `202.8299` n `88` status `ready` deltaP `-21.512` edge `26.4156` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.5841` n `88` status `ready` deltaP `41.3037` edge `0.3624` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.5922` n `121` status `ready` deltaP `15.4342` edge `0.0769` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.1023` n `125` status `ready` deltaP `1.9066` edge `0.0199` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.1601` n `121` status `ready` deltaP `4.9713` edge `0.0068` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.1635` n `125` status `ready` deltaP `0.8539` edge `0.0015` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5432` n `125` status `ready` deltaP `1.2048` edge `-0.0061` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8169` n `125` status `ready` deltaP `-7.4359` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9702` n `121` status `ready` deltaP `7.0651` edge `-0.0141` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.5785` n `88` status `ready` deltaP `-9.7538` edge `0.0234` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6736` n `125` status `ready` deltaP `-9.7329` edge `-0.0457` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.6904` n `88` status `ready` deltaP `-6.1395` edge `0.0754` maxDD `-7.0954`
- `market_context_high->index_24h` score `-1.9745` n `88` status `ready` deltaP `-4.6717` edge `-0.068` maxDD `-2.3194`
- `market_context_high->crypto_alt_1h` score `-1.9951` n `125` status `ready` deltaP `-1.5461` edge `-0.022` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.0085` n `125` status `ready` deltaP `-4.5497` edge `-0.0317` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.0936` n `121` status `ready` deltaP `-12.5441` edge `-0.0096` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5576` n `121` status `ready` deltaP `0.8063` edge `-0.0661` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6416` n `88` status `ready` deltaP `-3.267` edge `0.0124` maxDD `-35.189`
- `market_context_high->equity_4h` score `-5.4123` n `121` status `ready` deltaP `-29.5064` edge `-0.1926` maxDD `-15.3661`
- `market_context_high->unknown_1h` score `-7.1916` n `125` status `ready` deltaP `-0.297` edge `-0.5516` maxDD `-1.3246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
