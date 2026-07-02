# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T12:52:29.014036+00:00`
- Price records: `672`
- Market context records: `5456`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11440`

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

- `market_context_high->crypto_major_24h` score `3.7404` n `193` status `ready` deltaP `17.1489` edge `0.6514` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.5354` n `197` status `ready` deltaP `14.8252` edge `0.3417` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.1473` n `197` status `ready` deltaP `11.9258` edge `0.2633` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.9477` n `197` status `ready` deltaP `9.8985` edge `0.2604` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.4377` n `193` status `ready` deltaP `8.7858` edge `0.4858` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.3635` n `199` status `ready` deltaP `7.8634` edge `0.0744` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1151` n `199` status `ready` deltaP `6.4845` edge `0.0157` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0796` n `193` status `ready` deltaP `10.0281` edge `0.0313` maxDD `-0.9881`
- `market_context_high->metal_1h` score `-0.2725` n `199` status `ready` deltaP `3.9614` edge `0.0184` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4221` n `199` status `ready` deltaP `0.6575` edge `0.0566` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.5405` n `199` status `ready` deltaP `0.5612` edge `0.0001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.5442` n `199` status `ready` deltaP `1.8445` edge `0.0669` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.9074` n `197` status `ready` deltaP `6.8559` edge `0.0396` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0561` n `197` status `ready` deltaP `1.5158` edge `0.0044` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3541` n `199` status `ready` deltaP `-1.9724` edge `-0.0049` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7154` n `193` status `ready` deltaP `13.1827` edge `0.0688` maxDD `-16.1291`
- `market_context_high->metal_4h` score `-2.6002` n `197` status `ready` deltaP `-7.8146` edge `-0.0288` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2332` n `197` status `ready` deltaP `-5.9288` edge `-0.0418` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-7.0538` n `193` status `ready` deltaP `8.354` edge `0.2262` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0982` n `193` status `ready` deltaP `-3.3543` edge `-0.1499` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
