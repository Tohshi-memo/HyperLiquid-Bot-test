# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T10:52:28.223149+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4285`

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

- `news_risk_high->index_1h` score `-0.3969` n `127` status `ready` deltaP `3.5374` edge `0.0012` maxDD `-1.0529`
- `news_risk_high->crypto_alt_4h` score `-0.5031` n `127` status `ready` deltaP `4.3559` edge `0.1701` maxDD `-14.0916`
- `news_risk_high->index_4h` score `-0.6265` n `127` status `ready` deltaP `6.0327` edge `0.012` maxDD `-2.6034`
- `news_risk_high->crypto_alt_1h` score `-0.6875` n `127` status `ready` deltaP `0.7261` edge `0.0298` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.8105` n `127` status `ready` deltaP `-4.6242` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_24h` score `-1.0289` n `127` status `ready` deltaP `-6.4245` edge `0.1069` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `-1.0293` n `127` status `ready` deltaP `-5.2213` edge `-0.0079` maxDD `-1.1398`
- `news_risk_high->metal_1h` score `-1.124` n `127` status `ready` deltaP `-5.7947` edge `-0.0163` maxDD `-2.1337`
- `news_risk_high->equity_24h` score `-1.6298` n `127` status `ready` deltaP `18.2778` edge `0.9093` maxDD `-86.0244`
- `news_risk_high->fx_24h` score `-1.6731` n `127` status `ready` deltaP `-18.9303` edge `-0.0143` maxDD `-0.9201`
- `news_risk_high->equity_1h` score `-1.8467` n `127` status `ready` deltaP `-3.5822` edge `0.0064` maxDD `-12.5424`
- `news_risk_high->crypto_major_1h` score `-2.0348` n `127` status `ready` deltaP `-4.5252` edge `-0.0084` maxDD `-6.1465`
- `news_risk_high->crypto_major_4h` score `-2.4865` n `127` status `ready` deltaP `-4.7868` edge `0.0416` maxDD `-12.0183`
- `news_risk_high->commodity_1h` score `-2.9012` n `127` status `ready` deltaP `-14.7166` edge `-0.007` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.7912` n `127` status `ready` deltaP `-9.0815` edge `-0.0607` maxDD `-5.5752`
- `news_risk_high->commodity_4h` score `-4.5141` n `127` status `ready` deltaP `-19.6718` edge `-0.0096` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-5.0977` n `127` status `ready` deltaP `6.4901` edge `0.0653` maxDD `-34.3366`
- `news_risk_high->metal_24h` score `-5.9084` n `127` status `ready` deltaP `-9.1886` edge `-0.2415` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.4923` n `127` status `ready` deltaP `-22.3429` edge `0.0295` maxDD `-41.7256`
- `news_risk_high->crypto_major_24h` score `-11.5483` n `127` status `ready` deltaP `-19.4997` edge `0.0519` maxDD `-53.4077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
