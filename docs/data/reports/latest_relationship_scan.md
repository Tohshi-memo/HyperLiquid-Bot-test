# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T02:37:26.531582+00:00`
- Price records: `672`
- Market context records: `7626`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.5454` n `145` status `ready` deltaP `16.9771` edge `0.4473` maxDD `-34.5784`
- `market_context_high->index_1h` score `0.075` n `146` status `ready` deltaP `6.9625` edge `0.0111` maxDD `-0.8324`
- `market_context_high->unknown_24h` score `0.0437` n `146` status `ready` deltaP `9.9696` edge `0.0552` maxDD `-4.775`
- `market_context_high->commodity_24h` score `-0.0726` n `145` status `ready` deltaP `13.065` edge `0.0652` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.1292` n `146` status `ready` deltaP `8.3053` edge `0.0241` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1812` n `146` status `ready` deltaP `2.5039` edge `0.0233` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.3163` n `146` status `ready` deltaP `2.7294` edge `-0.0017` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3515` n `145` status `ready` deltaP `9.2803` edge `0.0176` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.4415` n `146` status `ready` deltaP `4.0531` edge `0.0107` maxDD `-2.2943`
- `market_context_high->equity_1h` score `-0.4541` n `146` status `ready` deltaP `5.9773` edge `0.0533` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6311` n `146` status `ready` deltaP `9.0633` edge `0.0288` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.2715` edge `-0.0014` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6699` n `146` status `ready` deltaP `0.7895` edge `0.0134` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.8787` n `146` status `ready` deltaP `3.8068` edge `0.0609` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1375` n `146` status `ready` deltaP `8.6744` edge `0.0641` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4773` n `146` status `ready` deltaP `2.214` edge `0.2102` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.529` n `146` status `ready` deltaP `-0.9843` edge `-0.0585` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6599` n `146` status `ready` deltaP `-1.6706` edge `0.044` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.0149` n `146` status `ready` deltaP `-3.2772` edge `0.0892` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5728` n `146` status `ready` deltaP `-6.3529` edge `-0.0036` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
