# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T07:37:23.051455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10778`

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

- `risk_on_high->unknown_4h` score `19.2295` n `135` status `ready` deltaP `8.1132` edge `1.6102` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.2295` n `135` status `ready` deltaP `8.1132` edge `1.6102` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `8.2492` n `227` status `ready` deltaP `7.8684` edge `0.708` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3271` n `37` status `ready` deltaP `25.1783` edge `0.4697` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3014` n `37` status `ready` deltaP `24.6528` edge `0.1941` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.7446` n `37` status `ready` deltaP `17.1803` edge `0.2388` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1396` n `37` status `ready` deltaP `21.4074` edge `0.0577` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8655` n `37` status `ready` deltaP `10.9715` edge `0.1024` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6398` n `37` status `ready` deltaP `13.6835` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.2697` n `37` status `ready` deltaP `6.9146` edge `0.078` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1712` n `37` status `ready` deltaP `13.9667` edge `0.0238` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.8986` n `37` status `ready` deltaP `8.5775` edge `0.0442` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6819` n `37` status `ready` deltaP `6.7032` edge `0.045` maxDD `-1.296`
- `news_risk_high->crypto_major_24h` score `0.3292` n `37` status `ready` deltaP `13.2789` edge `0.2313` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.2728` n `37` status `ready` deltaP `12.8378` edge `0.0387` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0991` n `147` status `ready` deltaP `12.3671` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0991` n `147` status `ready` deltaP `12.3671` edge `0.0015` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0231` n `37` status `ready` deltaP `5.7251` edge `0.0035` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1046` n `147` status `ready` deltaP `5.1285` edge `-0.0029` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
