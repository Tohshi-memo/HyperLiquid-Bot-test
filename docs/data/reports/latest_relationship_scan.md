# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T07:22:22.614276+00:00`
- Price records: `672`
- Market context records: `7115`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11664`

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

- `market_context_high->fx_4h` score `0.3687` n `146` status `ready` deltaP `15.461` edge `0.0142` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.124` n `146` status `ready` deltaP `-0.4307` edge `0.0484` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1261` n `146` status `ready` deltaP `3.9373` edge `0.0027` maxDD `-0.276`
- `market_context_high->index_1h` score `-0.5264` n `146` status `ready` deltaP `0.1456` edge `-0.0065` maxDD `-2.2895`
- `market_context_high->crypto_alt_1h` score `-0.5592` n `146` status `ready` deltaP `1.2202` edge `0.0317` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5796` n `146` status `ready` deltaP `3.4247` edge `0.0381` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8405` n `146` status `ready` deltaP `-3.9783` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3914` n `146` status `ready` deltaP `-4.7319` edge `-0.0433` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5208` n `146` status `ready` deltaP `-6.6402` edge `-0.0059` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5479` n `146` status `ready` deltaP `-6.8326` edge `0.0073` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1216` n `146` status `ready` deltaP `2.5633` edge `-0.0468` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0431` n `146` status `ready` deltaP `4.0365` edge `0.0114` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7016` n `146` status `ready` deltaP `-9.5082` edge `-0.1142` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0976` n `146` status `ready` deltaP `-3.339` edge `-0.0493` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4358` n `146` status `ready` deltaP `-9.1067` edge `-0.0121` maxDD `-5.414`
- `market_context_high->fx_24h` score `-4.6531` n `146` status `ready` deltaP `-12.3668` edge `-0.0226` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.712` n `146` status `ready` deltaP `0.3111` edge `-0.0162` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.356` n `146` status `ready` deltaP `-27.2831` edge `-0.0831` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7196` n `146` status `ready` deltaP `-2.4996` edge `-0.2396` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7516` n `146` status `ready` deltaP `-27.0239` edge `-0.1588` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
