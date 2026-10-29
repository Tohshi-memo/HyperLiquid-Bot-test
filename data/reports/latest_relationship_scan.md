# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T19:37:28.961005+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1617.6019` n `134` status `ready` deltaP `-1.7491` edge `134.8548` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `63.2864` n `134` status `ready` deltaP `5.9041` edge `5.2478` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.1946` n `134` status `ready` deltaP `27.1041` edge `0.0205` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3034` n `134` status `ready` deltaP `10.0054` edge `0.0101` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1011` n `134` status `ready` deltaP `11.9562` edge `0.0506` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0933` n `134` status `ready` deltaP `13.2395` edge `0.0133` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0933` n `134` status `ready` deltaP `3.7291` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3547` n `134` status `ready` deltaP `1.1954` edge `0.0139` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.4281` n `134` status `ready` deltaP `5.3691` edge `0.0313` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4421` n `134` status `ready` deltaP `1.7875` edge `0.0388` maxDD `-2.3383`
- `market_context_high->fx_4h` score `-0.4942` n `134` status `ready` deltaP `-0.0159` edge `-0.0034` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.9984` n `134` status `ready` deltaP `-3.7425` edge `-0.0024` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.0132` n `134` status `ready` deltaP `5.3612` edge `0.0129` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.1542` n `134` status `ready` deltaP `2.1003` edge `0.0245` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5588` n `134` status `ready` deltaP `-2.7917` edge `-0.0228` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6811` n `134` status `ready` deltaP `3.9257` edge `0.023` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.448` n `134` status `ready` deltaP `-7.1965` edge `-0.024` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7602` n `134` status `ready` deltaP `4.6551` edge `-0.0554` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-2.8333` n `134` status `ready` deltaP `9.5409` edge `-0.024` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.4743` n `134` status `ready` deltaP `1.078` edge `-0.0218` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
