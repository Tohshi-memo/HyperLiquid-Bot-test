# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T23:52:25.761978+00:00`
- Price records: `672`
- Market context records: `5505`
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

- `market_context_high->crypto_major_24h` score `3.012` n `190` status `ready` deltaP `16.2189` edge `0.5969` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4861` n `193` status `ready` deltaP `14.4936` edge `0.3398` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.4405` n `190` status `ready` deltaP `10.7511` edge `0.6396` maxDD `-31.6316`
- `market_context_high->equity_4h` score `2.3574` n `193` status `ready` deltaP `11.6872` edge `0.2824` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.0123` n `193` status `ready` deltaP `10.256` edge `0.2634` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5615` n `193` status `ready` deltaP `9.0325` edge `0.0831` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3814` n `190` status `ready` deltaP `12.9312` edge `0.0383` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1512` n `193` status `ready` deltaP `6.6954` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2532` n `193` status `ready` deltaP `1.4334` edge `0.0655` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3455` n `193` status `ready` deltaP `0.6275` edge `0.0004` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.3792` n `193` status `ready` deltaP `3.0227` edge `0.0728` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5391` n `193` status `ready` deltaP `1.5141` edge `0.0125` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7665` n `193` status `ready` deltaP `4.1285` edge `0.0067` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.9052` n `193` status `ready` deltaP `6.5991` edge `0.0415` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.4836` n `193` status `ready` deltaP `-2.9762` edge `-0.009` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8053` n `190` status `ready` deltaP `14.2708` edge `0.0721` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8835` n `193` status `ready` deltaP `-10.7134` edge `-0.0458` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5091` n `193` status `ready` deltaP `-8.486` edge `-0.0519` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1906` n `190` status `ready` deltaP `7.2442` edge `0.2222` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2838` n `190` status `ready` deltaP `-4.2379` edge `-0.1678` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
