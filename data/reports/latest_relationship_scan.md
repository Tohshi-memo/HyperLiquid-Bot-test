# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T12:37:37.441315+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `350.2785` n `50` status `ready` deltaP `11.024` edge `29.1213` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `291.7411` n `50` status `ready` deltaP `10.8232` edge `24.2396` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5262` n `73` status `ready` deltaP `39.795` edge `1.0495` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.0081` n `73` status `ready` deltaP `34.6627` edge `0.6514` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.8429` n `50` status `ready` deltaP `33.9097` edge `0.7358` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0225` n `50` status `ready` deltaP `16.5347` edge `0.8126` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.667` n `50` status `ready` deltaP `16.3232` edge `0.5171` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6895` n `50` status `ready` deltaP `14.2073` edge `0.4254` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3235` n `111` status `ready` deltaP `18.9821` edge `0.3681` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `2.9649` n `50` status `ready` deltaP `14.0539` edge `0.2197` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9443` n `50` status `ready` deltaP `32.8415` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9088` n `50` status `ready` deltaP `14.0` edge `0.1941` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.3318` n `50` status `ready` deltaP `10.8819` edge `0.4126` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.3005` n `111` status `ready` deltaP `22.1559` edge `0.1136` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.0627` n `73` status `ready` deltaP `8.0741` edge `0.526` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.5023` n `50` status `ready` deltaP `20.9401` edge `0.012` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2416` n `73` status `ready` deltaP `11.9673` edge `0.2068` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.899` n `111` status `ready` deltaP `12.2872` edge `0.2643` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8659` n `50` status `ready` deltaP `14.4444` edge `0.0718` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8059` n `116` status `ready` deltaP `4.9505` edge `0.0904` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
