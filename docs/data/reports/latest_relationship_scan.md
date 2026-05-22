# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T23:07:17.300155+00:00`
- Price records: `672`
- Market context records: `1572`
- Flow alert records: `6439`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `13.155` n `182` status `ready` deltaP `26.5949` edge `1.019` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.319` n `182` status `ready` deltaP `26.9974` edge `0.9649` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.8085` n `182` status `ready` deltaP `26.7399` edge `0.7523` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0116` n `182` status `ready` deltaP `20.7799` edge `0.3044` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.6928` n `182` status `ready` deltaP `17.1932` edge `0.4258` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.783` n `199` status `ready` deltaP `7.53` edge `0.1245` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.2768` n `182` status `ready` deltaP `12.5362` edge `0.0444` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1912` n `199` status `ready` deltaP `13.2545` edge `0.2681` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0185` n `199` status `ready` deltaP `9.2796` edge `0.2114` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.33` n `199` status `ready` deltaP `0.8177` edge `0.0546` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.6331` n `199` status `ready` deltaP `0.3145` edge `0.026` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6685` n `199` status `ready` deltaP `0.7741` edge `0.0023` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7096` n `199` status `ready` deltaP `5.5969` edge `0.0053` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7243` n `199` status `ready` deltaP `-0.1978` edge `0.0006` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8856` n `199` status `ready` deltaP `-0.5935` edge `0.0261` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.2072` n `199` status `ready` deltaP `-2.6106` edge `0.0257` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.309` n `199` status `ready` deltaP `10.516` edge `0.09` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3791` n `199` status `ready` deltaP `-10.3973` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1115` n `199` status `ready` deltaP `-13.9379` edge `-0.0997` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
