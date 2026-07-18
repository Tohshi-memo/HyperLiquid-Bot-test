# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T10:22:25.460649+00:00`
- Price records: `672`
- Market context records: `7129`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.4709` n `139` status `ready` deltaP `17.2915` edge `0.0151` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0595` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4074` n `151` status `ready` deltaP `-2.6986` edge `0.0399` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6306` n `151` status `ready` deltaP `-0.1814` edge `0.0234` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6613` n `151` status `ready` deltaP `3.1298` edge `0.0354` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7614` n `151` status `ready` deltaP `-2.5994` edge `-0.0182` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.8394` n `151` status `ready` deltaP `0.2726` edge `-0.0053` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3844` n `151` status `ready` deltaP `-5.0254` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-2.1113` n `139` status `ready` deltaP `-5.2115` edge `0.019` maxDD `-4.4825`
- `market_context_high->commodity_4h` score `-2.3396` n `139` status `ready` deltaP `-6.8904` edge `-0.0455` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.1427` n `139` status `ready` deltaP `2.8415` edge `0.0066` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.4191` n `151` status `ready` deltaP `0.9577` edge `-0.0456` maxDD `-14.99`
- `market_context_high->commodity_24h` score `-4.1212` n `139` status `ready` deltaP `-11.5432` edge `-0.1356` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.2903` n `139` status `ready` deltaP `-5.1632` edge `-0.0532` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5103` n `139` status `ready` deltaP `-9.9908` edge `-0.0135` maxDD `-5.3268`
- `market_context_high->fx_24h` score `-4.8389` n `139` status `ready` deltaP `-14.4497` edge `-0.0242` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.8784` n `139` status `ready` deltaP `-0.5845` edge `-0.0241` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.7906` n `139` status `ready` deltaP `-30.106` edge `-0.1005` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8665` n `139` status `ready` deltaP `-1.5902` edge `-0.2579` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.6144` n `139` status `ready` deltaP `-28.6933` edge `-0.1749` maxDD `-41.4673`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
