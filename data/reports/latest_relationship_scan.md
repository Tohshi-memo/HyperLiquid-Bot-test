# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T18:52:31.899047+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6812`

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

- `market_context_high->unknown_1h` score `337.841` n `50` status `ready` deltaP `8.479` edge `28.1018` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `285.394` n `50` status `ready` deltaP `6.8598` edge `23.7371` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3104` n `107` status `ready` deltaP `35.4572` edge `1.4771` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.1796` n `50` status `ready` deltaP `32.8681` edge `0.7708` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3996` n `50` status `ready` deltaP `19.6768` edge `0.5558` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.3142` n `50` status `ready` deltaP `11.3264` edge `0.5383` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.156` n `50` status `ready` deltaP `16.7988` edge `0.447` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.9424` n `107` status `ready` deltaP `20.9616` edge `0.5875` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.9253` n `50` status `ready` deltaP `19.0417` edge `0.5625` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.2974` n `120` status `ready` deltaP `26.7277` edge `0.1662` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1672` n `50` status `ready` deltaP `35.4329` edge `0.0412` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0479` n `50` status `ready` deltaP `14.7485` edge `0.2007` maxDD `-2.2692`
- `news_risk_high->equity_24h` score `2.9815` n `107` status `ready` deltaP `22.0697` edge `0.47` maxDD `-9.4579`
- `market_context_high->crypto_alt_1h` score `2.9422` n `50` status `ready` deltaP `13.6048` edge `0.2208` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4399` n `107` status `ready` deltaP `24.231` edge `0.0896` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2369` n `107` status `ready` deltaP `26.1731` edge `0.2397` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5765` n `50` status `ready` deltaP `21.8383` edge `0.0122` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9019` n `50` status `ready` deltaP `14.7917` edge `0.0741` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5086` n `50` status `ready` deltaP `14.4306` edge `0.0708` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.3979` n `120` status `ready` deltaP `6.5569` edge `0.0431` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
