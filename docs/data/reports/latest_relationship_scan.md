# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T10:37:24.299941+00:00`
- Price records: `672`
- Market context records: `7130`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11670`

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

- `market_context_high->fx_4h` score `0.502` n `139` status `ready` deltaP `17.8584` edge `0.0153` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0916` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4038` n `151` status `ready` deltaP `-2.6986` edge `0.0402` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5923` n `151` status `ready` deltaP `0.3311` edge `0.0249` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6268` n `151` status `ready` deltaP `3.6424` edge `0.0364` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7575` n `151` status `ready` deltaP `-2.5994` edge `-0.0177` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7948` n `151` status `ready` deltaP `0.7852` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3844` n `151` status `ready` deltaP `-5.0254` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-2.1286` n `139` status `ready` deltaP `-5.2115` edge `0.0194` maxDD `-4.6297`
- `market_context_high->commodity_4h` score `-2.33` n `139` status `ready` deltaP `-6.8904` edge `-0.0447` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.1818` n `139` status `ready` deltaP `2.2746` edge `0.0054` maxDD `-24.6128`
- `market_context_high->equity_1h` score `-3.4172` n `151` status `ready` deltaP `0.9577` edge `-0.0454` maxDD `-14.9936`
- `market_context_high->commodity_24h` score `-4.1818` n `138` status `ready` deltaP `-11.8508` edge `-0.1386` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.2414` n `139` status `ready` deltaP `-4.5962` edge `-0.0529` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4612` n `139` status `ready` deltaP `-9.4238` edge `-0.0132` maxDD `-5.3259`
- `market_context_high->fx_24h` score `-4.8327` n `138` status `ready` deltaP `-14.3418` edge `-0.0244` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.9836` n `139` status `ready` deltaP `-1.1516` edge `-0.0268` maxDD `-22.4658`
- `market_context_high->unknown_24h` score `-9.8627` n `138` status `ready` deltaP `-30.7368` edge `-0.1023` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8723` n `139` status `ready` deltaP `-1.5902` edge `-0.2577` maxDD `-64.0182`
- `market_context_high->metal_24h` score `-14.5797` n `138` status `ready` deltaP `-28.8043` edge `-0.1768` maxDD `-41.3581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
