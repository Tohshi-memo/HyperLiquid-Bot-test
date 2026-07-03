# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T02:22:31.429403+00:00`
- Price records: `672`
- Market context records: `5515`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->equity_24h` score `3.0059` n `190` status `ready` deltaP `12.3136` edge `0.6763` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.634` n `190` status `ready` deltaP `16.2189` edge `0.5654` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3821` n `193` status `ready` deltaP `13.8838` edge `0.3352` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9236` n `193` status `ready` deltaP `10.3153` edge `0.2554` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8141` n `193` status `ready` deltaP `9.189` edge `0.254` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.3922` n `190` status `ready` deltaP `12.9312` edge `0.0392` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2449` n `193` status `ready` deltaP `7.6852` edge `0.0657` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0277` n `193` status `ready` deltaP `5.6475` edge `0.014` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3478` n `193` status `ready` deltaP `0.6275` edge `0.0001` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.535` n `193` status `ready` deltaP `0.3855` edge `0.049` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6586` n `193` status `ready` deltaP `1.9748` edge `0.0565` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7189` n `193` status `ready` deltaP `0.3165` edge `0.0055` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8796` n `193` status `ready` deltaP `2.909` edge `0.0054` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0893` n `193` status `ready` deltaP `5.2272` edge `0.0353` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5746` n `193` status `ready` deltaP `-3.8744` edge `-0.0106` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8326` n `190` status `ready` deltaP `14.2708` edge `0.0686` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0352` n `193` status `ready` deltaP `-12.0853` edge `-0.0561` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5721` n `193` status `ready` deltaP `-8.9433` edge `-0.0541` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.3094` n `190` status `ready` deltaP `7.2442` edge `0.2123` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3243` n `190` status `ready` deltaP `-4.2379` edge `-0.173` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
