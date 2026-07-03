# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T23:52:28.397139+00:00`
- Price records: `672`
- Market context records: `5608`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.3619` n `174` status `ready` deltaP `15.0084` edge `0.688` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4768` n `220` status `ready` deltaP `13.6225` edge `0.2615` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.2353` n `174` status `ready` deltaP `21.438` edge `0.0574` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8566` n `220` status `ready` deltaP `8.9053` edge `0.1761` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4271` n `220` status `ready` deltaP `5.8731` edge `0.1603` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3376` n `232` status `ready` deltaP `5.7996` edge `0.0339` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3447` n `232` status `ready` deltaP `0.3949` edge `0.0008` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.5125` n `232` status `ready` deltaP `0.1678` edge `0.0007` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6213` n `232` status `ready` deltaP `1.0169` edge `0.0376` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6359` n `232` status `ready` deltaP `4.029` edge `0.0447` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.8829` n `232` status `ready` deltaP `1.0892` edge `0.006` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1795` n `232` status `ready` deltaP `-2.2868` edge `-0.0065` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2379` n `220` status `ready` deltaP `1.0394` edge `0.0073` maxDD `-1.168`
- `market_context_high->crypto_major_24h` score `-1.485` n `174` status `ready` deltaP `9.8061` edge `0.2649` maxDD `-29.6555`
- `market_context_high->index_4h` score `-1.6396` n `220` status `ready` deltaP `1.7988` edge `0.0123` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3855` n `174` status `ready` deltaP `10.0874` edge `0.0256` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8539` n `220` status `ready` deltaP `-10.8952` edge `-0.0549` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2216` n `220` status `ready` deltaP `-6.1724` edge `-0.0431` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2133` n `174` status `ready` deltaP `-10.0635` edge `-0.2498` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.4999` n `174` status `ready` deltaP `-0.4071` edge `-0.0859` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
