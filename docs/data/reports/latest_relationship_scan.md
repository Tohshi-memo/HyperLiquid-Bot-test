# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T02:22:28.911902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_1h` score `331.9601` n `55` status `ready` deltaP `11.7828` edge `27.5897` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6992` n `50` status `ready` deltaP `12.8049` edge `26.7229` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.1291` n `50` status `ready` deltaP `28.9393` edge `1.0715` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `12.1685` n `59` status `ready` deltaP `32.2151` edge `0.8093` maxDD `-0.1353`
- `market_context_high->crypto_major_24h` score `10.9898` n `50` status `ready` deltaP `34.6863` edge `0.8262` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.9222` n `65` status `ready` deltaP `40.0211` edge `0.6637` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3197` n `65` status `ready` deltaP `24.2073` edge `0.583` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.007` n `50` status `ready` deltaP `15.7134` edge `0.5495` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4288` n `50` status `ready` deltaP `14.2073` edge `0.4866` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.1272` n `59` status `ready` deltaP `35.8752` edge `0.1881` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8464` n `65` status `ready` deltaP `26.3696` edge `0.206` maxDD `-2.9013`
- `news_risk_high->crypto_major_1h` score `3.0682` n `65` status `ready` deltaP `14.058` edge `0.1975` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.0136` n `65` status `ready` deltaP `32.6759` edge `0.0595` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9834` n `50` status `ready` deltaP `33.4512` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->metal_4h` score `2.6158` n `65` status `ready` deltaP `22.5845` edge `0.109` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.5573` n `55` status `ready` deltaP `11.5406` edge `0.1812` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0842` n `65` status `ready` deltaP `25.6172` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0828` n `55` status `ready` deltaP `7.1557` edge `0.2005` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.611` n `65` status `ready` deltaP `5.6172` edge `0.1487` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.3349` n `50` status `ready` deltaP `6.9948` edge `0.3107` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
