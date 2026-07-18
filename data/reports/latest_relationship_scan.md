# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T01:22:29.969825+00:00`
- Price records: `672`
- Market context records: `7089`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7419` n `166` status `ready` deltaP `17.6884` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1588` n `166` status `ready` deltaP `4.363` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.303` n `166` status `ready` deltaP `-0.1641` edge `0.0317` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.4441` n `166` status `ready` deltaP `1.4717` edge `-0.0048` maxDD `-2.2895`
- `market_context_high->crypto_alt_1h` score `-0.5908` n `166` status `ready` deltaP `1.2156` edge `0.0291` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.6093` n `166` status `ready` deltaP `3.4684` edge `0.034` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8967` n `166` status `ready` deltaP `-4.9545` edge `-0.0203` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4363` n `166` status `ready` deltaP `-5.7608` edge `-0.0045` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5111` n `166` status `ready` deltaP `-6.5989` edge `-0.0462` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.8113` n `166` status `ready` deltaP `-8.6064` edge `-0.0114` maxDD `-4.742`
- `market_context_high->equity_1h` score `-1.9929` n `166` status `ready` deltaP `3.4323` edge `-0.0361` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2116` n `166` status `ready` deltaP `3.5355` edge `-0.0372` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.7469` n `166` status `ready` deltaP `-4.6394` edge `-0.0671` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-2.9921` n `166` status `ready` deltaP `4.0718` edge `0.0177` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1619` n `166` status `ready` deltaP `-1.6107` edge `-0.0161` maxDD `-22.2831`
- `market_context_high->metal_4h` score `-3.9902` n `166` status `ready` deltaP `-4.0038` edge `-0.0075` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.9982` n `166` status `ready` deltaP `-5.0953` edge `-0.0165` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.1989` n `166` status `ready` deltaP `2.4904` edge `-0.1807` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.7227` n `166` status `ready` deltaP `-22.2766` edge `-0.0637` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.3133` n `166` status `ready` deltaP `-23.8475` edge `-0.1224` maxDD `-43.9111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
