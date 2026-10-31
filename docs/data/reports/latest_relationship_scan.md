# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T11:07:23.033898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7437`

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

- `market_context_high->unknown_24h` score `2059.2056` n `119` status `ready` deltaP `-6.4732` edge `171.6866` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `102.303` n `98` status `ready` deltaP `-5.3433` edge `8.5895` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `50.0567` n `119` status `ready` deltaP `1.5871` edge `4.1741` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.7418` n `38` status `ready` deltaP `46.1257` edge `1.1761` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.0375` n `119` status `ready` deltaP `25.2553` edge `0.9438` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.147` n `98` status `ready` deltaP `18.638` edge `0.4433` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.52` n `119` status `ready` deltaP `41.6521` edge `0.1173` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.9408` n `119` status `ready` deltaP `13.6819` edge `0.0162` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8948` n `98` status `ready` deltaP `7.9463` edge `0.1045` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.6071` n `119` status `ready` deltaP `17.5203` edge `0.0337` maxDD `-1.4805`
- `market_context_high->equity_1h` score `0.4025` n `119` status `ready` deltaP `5.2206` edge `0.0863` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3247` n `119` status `ready` deltaP `8.5241` edge `0.073` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.1055` n `119` status `ready` deltaP `2.6363` edge `0.1477` maxDD `-5.4737`
- `market_context_high->commodity_4h` score `0.0372` n `119` status `ready` deltaP `11.333` edge `0.0511` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.086` n `119` status `ready` deltaP `3.8155` edge `-0.001` maxDD `-0.1699`
- `market_context_high->metal_24h` score `-0.1187` n `119` status `ready` deltaP `9.4756` edge `0.1863` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.3645` n `119` status `ready` deltaP `0.8932` edge `0.0151` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3716` n `119` status `ready` deltaP `1.9522` edge `-0.0022` maxDD `-0.3428`
- `market_context_high->index_1h` score `-0.4562` n `119` status `ready` deltaP `2.4342` edge `0.0016` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8266` n `119` status `ready` deltaP `2.4241` edge `0.0554` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
