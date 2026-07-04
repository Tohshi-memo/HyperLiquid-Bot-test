# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T11:22:31.781783+00:00`
- Price records: `672`
- Market context records: `5657`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.3431` n `188` status `ready` deltaP `15.2482` edge `0.6015` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.891` n `237` status `ready` deltaP `11.3094` edge `0.2281` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.5305` n `237` status `ready` deltaP `7.9912` edge `0.1548` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.3517` n `188` status `ready` deltaP `17.8671` edge `0.0549` maxDD `-2.2431`
- `market_context_high->crypto_alt_4h` score `0.1015` n `237` status `ready` deltaP `7.1364` edge `0.1458` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2852` n `248` status `ready` deltaP `1.5091` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.399` n `248` status `ready` deltaP `5.2564` edge `0.0324` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5462` n `248` status `ready` deltaP `-0.3453` edge `-0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6653` n `248` status `ready` deltaP `1.2918` edge `0.0321` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8643` n `248` status `ready` deltaP `2.5232` edge `0.0357` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8887` n `248` status `ready` deltaP `0.8982` edge `-0.0035` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.912` n `248` status `ready` deltaP `0.8306` edge `0.0053` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2432` n `237` status `ready` deltaP `2.5902` edge `0.0067` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0355` n `237` status `ready` deltaP `-1.689` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3742` n `188` status `ready` deltaP `8.699` edge `0.0363` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0694` n `237` status `ready` deltaP `-14.9789` edge `-0.0553` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.802` n `237` status `ready` deltaP `-2.1875` edge `-0.0347` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6563` n `188` status `ready` deltaP `3.9599` edge `0.0396` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4406` n `188` status `ready` deltaP `-13.9701` edge `-0.2529` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.6496` n `188` status `ready` deltaP `-13.8963` edge `-0.1006` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
