# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T23:52:24.755804+00:00`
- Price records: `672`
- Market context records: `6442`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.5765` n `32` status `ready` deltaP `29.5139` edge `0.7827` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.97` n `145` status `ready` deltaP `21.1698` edge `0.9364` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3661` n `32` status `ready` deltaP `52.9514` edge `0.1775` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9975` n `32` status `ready` deltaP `34.375` edge `0.1245` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2043` n `32` status `ready` deltaP `11.1111` edge `0.4147` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4206` n `32` status `ready` deltaP `29.1916` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.517` n `32` status `ready` deltaP `13.9783` edge `0.148` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.229` n `186` status `ready` deltaP `-5.5325` edge `0.2294` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.9043` n `32` status `ready` deltaP `10.1235` edge `0.0946` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0324` n `186` status `ready` deltaP `7.0548` edge `0.0233` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2033` n `32` status `ready` deltaP `6.5307` edge `-0.026` maxDD `-0.7581`
- `market_context_high->metal_4h` score `-0.2317` n `186` status `ready` deltaP `7.3662` edge `0.0404` maxDD `-2.7056`
- `news_risk_high->metal_1h` score `-0.5394` n `32` status `ready` deltaP `0.7485` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.5508` n `186` status `ready` deltaP `-14.7653` edge `0.2931` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-0.5862` n `186` status `ready` deltaP `0.2109` edge `0.0012` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6046` n `186` status `ready` deltaP `-0.8708` edge `-0.0034` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.6217` n `186` status `ready` deltaP `6.4762` edge `0.047` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.6825` n `32` status `ready` deltaP `1.3889` edge `-0.0096` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.6866` n `145` status `ready` deltaP `11.7935` edge `0.0902` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
