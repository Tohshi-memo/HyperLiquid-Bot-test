# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T18:52:25.347109+00:00`
- Price records: `672`
- Market context records: `3207`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10906`

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

- `market_context_high->crypto_alt_24h` score `17.1719` n `97` status `ready` deltaP `11.9398` edge `2.349` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.6739` n `97` status `ready` deltaP `47.4924` edge `0.8657` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.0258` n `97` status `ready` deltaP `28.0784` edge `0.8408` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6692` n `97` status `ready` deltaP `11.8109` edge `1.3615` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3947` n `125` status `ready` deltaP `22.3037` edge `0.18` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.5708` n `97` status `ready` deltaP `11.2614` edge `-0.0024` maxDD `-0.6756`
- `market_context_high->unknown_4h` score `0.4935` n `125` status `ready` deltaP `10.9122` edge `0.1906` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3626` n `135` status `ready` deltaP `5.9969` edge `0.0325` maxDD `-1.7142`
- `market_context_high->unknown_24h` score `-0.5947` n `97` status `ready` deltaP `13.2338` edge `0.3208` maxDD `-36.1545`
- `market_context_high->crypto_alt_1h` score `-0.7766` n `135` status `ready` deltaP `5.5711` edge `0.1111` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.8174` n `135` status `ready` deltaP `5.6099` edge `0.0841` maxDD `-15.1032`
- `market_context_high->index_1h` score `-0.9108` n `135` status `ready` deltaP `3.0572` edge `0.01` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-1.0861` n `135` status `ready` deltaP `-9.8348` edge `-0.005` maxDD `-0.8278`
- `market_context_high->fx_4h` score `-1.1314` n `125` status `ready` deltaP `-7.6756` edge `-0.0054` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.4406` n `135` status `ready` deltaP `2.8998` edge `0.0092` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.515` n `125` status `ready` deltaP `15.1427` edge `0.0637` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.0267` n `135` status `ready` deltaP `-3.1836` edge `-0.0083` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6322` n `135` status `ready` deltaP `2.3963` edge `-0.1156` maxDD `-17.0266`
- `market_context_high->crypto_alt_4h` score `-3.2593` n `125` status `ready` deltaP `13.2037` edge `0.2986` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.4722` n `125` status `ready` deltaP `6.272` edge `0.1772` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
