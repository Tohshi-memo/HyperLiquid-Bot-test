# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T02:52:29.355910+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4034.7477` n `51` status `ready` deltaP `22.5388` edge `336.1208` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.1159` n `40` status `ready` deltaP `51.4583` edge `0.873` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.199` n `40` status `ready` deltaP `51.3194` edge `0.6039` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `3.4216` n `51` status `ready` deltaP `8.0404` edge `0.3079` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.4079` n `51` status `ready` deltaP `13.6179` edge `0.0646` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.7174` n `43` status `ready` deltaP `9.586` edge `0.1127` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.5115` n `51` status `ready` deltaP `11.0683` edge `0.0269` maxDD `-0.8085`
- `market_context_high->fx_4h` score `0.4359` n `43` status `ready` deltaP `17.8177` edge `0.0167` maxDD `-1.3685`
- `market_context_high->crypto_alt_4h` score `0.391` n `43` status `ready` deltaP `6.1933` edge `0.0994` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.3673` n `47` status `ready` deltaP `7.5646` edge `0.0341` maxDD `-1.3282`
- `news_risk_high->equity_1h` score `0.2325` n `51` status `ready` deltaP `6.1436` edge `0.0607` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.0001` n `47` status `ready` deltaP `7.1155` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->metal_1h` score `-0.0055` n `51` status `ready` deltaP `3.405` edge `0.0086` maxDD `-0.5599`
- `news_risk_high->index_1h` score `-0.0694` n `51` status `ready` deltaP `2.5068` edge `0.0067` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0768` n `51` status `ready` deltaP `2.7768` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.1667` n `51` status `ready` deltaP `7.4666` edge `0.0246` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.1744` n `51` status `ready` deltaP `6.0996` edge `0.009` maxDD `-3.762`
- `news_risk_high->crypto_alt_1h` score `-0.2544` n `51` status `ready` deltaP `3.9891` edge `0.009` maxDD `-3.1233`
- `news_risk_high->commodity_1h` score `-0.4019` n `51` status `ready` deltaP `3.2259` edge `-0.0199` maxDD `-1.9168`
- `market_context_high->fx_24h` score `-0.7103` n `40` status `ready` deltaP `0.6597` edge `0.0344` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
