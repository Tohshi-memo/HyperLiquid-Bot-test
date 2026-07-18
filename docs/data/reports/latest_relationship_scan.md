# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T09:52:26.531615+00:00`
- Price records: `672`
- Market context records: `7126`
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

- `market_context_high->fx_4h` score `0.4407` n `141` status `ready` deltaP `16.7391` edge `0.0149` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0595` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4134` n `151` status `ready` deltaP `-2.6986` edge `0.0394` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.7042` n `151` status `ready` deltaP `-1.2065` edge `0.0208` maxDD `-5.91`
- `market_context_high->index_1h` score `-0.755` n `151` status `ready` deltaP `1.2977` edge `-0.0051` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.8202` n `151` status `ready` deltaP `-3.6245` edge `-0.0189` maxDD `-1.9668`
- `market_context_high->crypto_major_1h` score `-1.0785` n `151` status `ready` deltaP `2.6173` edge `0.0334` maxDD `-7.5909`
- `market_context_high->unknown_4h` score `-1.4277` n `141` status `ready` deltaP `-5.6911` edge `0.0151` maxDD `-4.4825`
- `market_context_high->metal_1h` score `-1.4664` n `151` status `ready` deltaP `-6.0505` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->commodity_4h` score `-2.2765` n `141` status `ready` deltaP `-6.2067` edge `-0.0448` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.0994` n `141` status `ready` deltaP `3.4034` edge `0.0084` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.3637` n `151` status `ready` deltaP `1.4702` edge `-0.0451` maxDD `-14.934`
- `market_context_high->commodity_24h` score `-4.0107` n `141` status `ready` deltaP `-10.9412` edge `-0.1304` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.2057` n `141` status `ready` deltaP `-4.2856` edge `-0.052` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5133` n `141` status `ready` deltaP `-10.0328` edge `-0.0131` maxDD `-5.3568`
- `market_context_high->fx_24h` score `-4.7635` n `141` status `ready` deltaP `-13.5823` edge `-0.0237` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.7975` n `141` status `ready` deltaP `-0.0833` edge `-0.0207` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.6006` n `141` status `ready` deltaP `-28.8712` edge `-0.0929` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8478` n `141` status `ready` deltaP `-2.1514` edge `-0.2526` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.6879` n `141` status `ready` deltaP `-28.4686` edge `-0.1713` maxDD `-41.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
