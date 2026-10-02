# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T05:07:34.617033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4880`

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

- `market_context_high->unknown_1h` score `340.794` n `50` status `ready` deltaP `9.3772` edge `28.3419` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.1015` n `50` status `ready` deltaP `8.9939` edge `23.9485` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.594` n `66` status `ready` deltaP `39.1572` edge `1.0594` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0711` n `50` status `ready` deltaP `36.1667` edge `0.8231` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.1907` n `50` status `ready` deltaP `16.1875` edge `0.7456` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `7.348` n `66` status `ready` deltaP `29.5613` edge `0.4966` maxDD `-3.5074`
- `market_context_high->crypto_major_4h` score `6.8677` n `50` status `ready` deltaP `17.5427` edge `0.5257` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7717` n `50` status `ready` deltaP `15.5793` edge `0.4231` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.5226` n `87` status `ready` deltaP `13.3954` edge `0.3386` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.2281` n `50` status `ready` deltaP `15.7431` edge `0.4951` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9021` n `50` status `ready` deltaP `32.689` edge `0.0374` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.7805` n `50` status `ready` deltaP `13.5509` edge `0.1864` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7635` n `50` status `ready` deltaP `13.1557` edge `0.2089` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.0009` n `87` status `ready` deltaP `21.2766` edge `0.0945` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.1747` n `66` status `ready` deltaP `20.2809` edge `0.1278` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9436` n `50` status `ready` deltaP `14.9653` edge `0.0783` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.9404` n `99` status `ready` deltaP `6.7517` edge `0.0896` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.755` n `66` status `ready` deltaP `5.4293` edge `0.188` maxDD `-2.192`
- `market_context_high->fx_24h` score `0.4829` n `50` status `ready` deltaP `14.4306` edge `0.0675` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
