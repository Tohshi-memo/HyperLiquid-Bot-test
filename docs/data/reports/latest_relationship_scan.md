# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T04:37:25.837476+00:00`
- Price records: `672`
- Market context records: `5524`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `market_context_high->equity_24h` score `3.7129` n `190` status `ready` deltaP `13.8761` edge `0.7248` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.676` n `190` status `ready` deltaP `16.2189` edge `0.5689` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.6545` n `193` status `ready` deltaP `13.8838` edge `0.3579` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.0061` n `193` status `ready` deltaP `9.189` edge `0.27` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.866` n `193` status `ready` deltaP `10.3153` edge `0.2506` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.3982` n `190` status `ready` deltaP `12.9312` edge `0.0397` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2018` n `193` status `ready` deltaP `7.2361` edge `0.0651` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0142` n `193` status `ready` deltaP `5.1984` edge `0.0135` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3658` n `193` status `ready` deltaP `0.3281` edge `-0.0002` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3731` n `193` status `ready` deltaP `0.9843` edge `0.0585` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4799` n `193` status `ready` deltaP `2.5736` edge `0.0674` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6818` n `193` status `ready` deltaP `0.6159` edge `0.0066` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9708` n `193` status `ready` deltaP `1.9943` edge `0.0039` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.1413` n `193` status `ready` deltaP `4.9223` edge `0.033` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6537` n `193` status `ready` deltaP `-4.7726` edge `-0.0112` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8416` n `190` status `ready` deltaP `14.0972` edge `0.0686` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.032` n `193` status `ready` deltaP `-12.0853` edge `-0.0557` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.6509` n `193` status `ready` deltaP `-9.5531` edge `-0.0566` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.079` n `190` status `ready` deltaP `7.2442` edge `0.2315` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3087` n `190` status `ready` deltaP `-4.2379` edge `-0.171` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
