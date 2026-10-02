# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T05:22:34.190224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4882`

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

- `market_context_high->unknown_1h` score `340.83` n `50` status `ready` deltaP `9.5269` edge `28.3439` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0739` n `50` status `ready` deltaP `8.9939` edge `23.9462` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.2423` n `65` status `ready` deltaP `39.1106` edge `1.0304` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0687` n `50` status `ready` deltaP `36.1667` edge `0.8229` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.2543` n `50` status `ready` deltaP `16.1875` edge `0.7509` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `7.6314` n `65` status `ready` deltaP `30.6463` edge `0.504` maxDD `-3.1219`
- `market_context_high->crypto_major_4h` score `6.8473` n `50` status `ready` deltaP `17.5427` edge `0.524` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7657` n `50` status `ready` deltaP `15.5793` edge `0.4226` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.5634` n `87` status `ready` deltaP `13.3954` edge `0.342` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.2113` n `50` status `ready` deltaP `15.5694` edge `0.4941` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9021` n `50` status `ready` deltaP `32.689` edge `0.0374` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.7769` n `50` status `ready` deltaP `13.5509` edge `0.1861` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7623` n `50` status `ready` deltaP `13.1557` edge `0.2088` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.9637` n `87` status `ready` deltaP `21.2766` edge `0.0914` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.2123` n `65` status `ready` deltaP `21.063` edge `0.1274` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9542` n `50` status `ready` deltaP `15.1389` edge `0.0785` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.9452` n `99` status `ready` deltaP `6.7517` edge `0.09` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.6791` n `65` status `ready` deltaP `4.5539` edge `0.1841` maxDD `-2.192`
- `market_context_high->fx_24h` score `0.4852` n `50` status `ready` deltaP `14.4306` edge `0.0678` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
