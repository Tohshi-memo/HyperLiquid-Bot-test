# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T23:44:01.461995+00:00`
- Price records: `672`
- Market context records: `5504`
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

- `market_context_high->crypto_major_24h` score `3.0576` n `190` status `ready` deltaP `16.2189` edge `0.6007` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.5079` n `193` status `ready` deltaP `14.646` edge `0.3406` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.4116` n `193` status `ready` deltaP `11.8397` edge `0.2859` maxDD `-7.4425`
- `market_context_high->equity_24h` score `2.4057` n `190` status `ready` deltaP `10.7511` edge `0.6367` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `2.0377` n `193` status `ready` deltaP `10.4085` edge `0.2645` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5807` n `193` status `ready` deltaP `9.1822` edge `0.0837` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.379` n `190` status `ready` deltaP `12.9312` edge `0.0381` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1655` n `193` status `ready` deltaP `6.8451` edge `0.0175` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.252` n `193` status `ready` deltaP `1.4334` edge `0.0656` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3455` n `193` status `ready` deltaP `0.6275` edge `0.0004` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.3588` n `193` status `ready` deltaP `3.1724` edge `0.0735` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5391` n `193` status `ready` deltaP `1.5141` edge `0.0125` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7665` n `193` status `ready` deltaP `4.1285` edge `0.0067` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.8834` n `193` status `ready` deltaP `6.7516` edge `0.0423` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.4967` n `193` status `ready` deltaP `-3.1259` edge `-0.0091` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8006` n `190` status `ready` deltaP `14.2708` edge `0.0727` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8685` n `193` status `ready` deltaP `-10.5609` edge `-0.0449` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5067` n `193` status `ready` deltaP `-8.486` edge `-0.0517` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.169` n `190` status `ready` deltaP `7.2442` edge `0.224` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2806` n `190` status `ready` deltaP `-4.2379` edge `-0.1674` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
