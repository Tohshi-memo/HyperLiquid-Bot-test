# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T07:52:29.483447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4826`

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

- `market_context_high->unknown_1h` score `366.1546` n `50` status `ready` deltaP `11.024` edge `30.4443` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.791` n `50` status `ready` deltaP `12.0427` edge `24.4023` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.2006` n `50` status `ready` deltaP `25.3889` edge `1.0178` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.895` n `70` status `ready` deltaP `33.7351` edge `0.7315` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.6799` n `50` status `ready` deltaP `33.0417` edge `0.728` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.4713` n `78` status `ready` deltaP `36.5697` edge `0.5658` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6078` n `78` status `ready` deltaP `30.2845` edge `0.5665` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3619` n `50` status `ready` deltaP `17.3902` edge `0.5679` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.0683` n `50` status `ready` deltaP `16.9512` edge `0.5216` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.1892` n `70` status `ready` deltaP `33.0407` edge `0.1447` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9392` n `78` status `ready` deltaP `30.4096` edge `0.1868` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3081` n `50` status `ready` deltaP `15.1018` edge `0.2413` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0025` n `50` status `ready` deltaP `13.5509` edge `0.2049` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8933` n `50` status `ready` deltaP `32.3841` edge `0.0387` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.6986` n `78` status `ready` deltaP `13.6535` edge `0.1694` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2487` n `78` status `ready` deltaP `19.9304` edge `0.0961` maxDD `-0.993`
- `news_risk_high->index_4h` score `1.9109` n `78` status `ready` deltaP `23.2372` edge `0.0472` maxDD `-0.4296`
- `news_risk_high->crypto_alt_1h` score `1.6763` n `78` status `ready` deltaP `6.7941` edge `0.1463` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4364` n `50` status `ready` deltaP `20.1916` edge `0.0115` maxDD `-0.113`
- `market_context_high->fx_24h` score `1.3122` n `50` status `ready` deltaP `25.3681` edge `0.1009` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
