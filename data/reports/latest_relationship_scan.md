# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T11:37:22.628928+00:00`
- Price records: `672`
- Market context records: `2658`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->unknown_24h` score `7.9986` n `119` status `ready` deltaP `17.3815` edge `0.5835` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `7.6852` n `119` status `ready` deltaP `13.1988` edge `0.9018` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `4.9521` n `121` status `ready` deltaP `24.4759` edge `0.5174` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5456` n `121` status `ready` deltaP `14.575` edge `0.3793` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.7329` n `121` status `ready` deltaP `8.7419` edge `0.1911` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0707` n `133` status `ready` deltaP `9.0991` edge `0.1473` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6355` n `133` status `ready` deltaP `8.0512` edge `0.1187` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.4299` n `119` status `ready` deltaP `9.5399` edge `0.0703` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `0.0745` n `133` status `ready` deltaP `3.5467` edge `0.0405` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.0535` n `121` status `ready` deltaP `7.4985` edge `0.0297` maxDD `-2.3986`
- `market_context_high->metal_4h` score `-0.1329` n `121` status `ready` deltaP `5.5722` edge `0.0334` maxDD `-2.5301`
- `market_context_high->index_1h` score `-0.2983` n `133` status `ready` deltaP `2.0463` edge `0.0109` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3267` n `133` status `ready` deltaP `4.132` edge `0.0059` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.3842` n `119` status `ready` deltaP `8.1714` edge `0.0007` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.5141` n `133` status `ready` deltaP `-0.0765` edge `0.004` maxDD `-1.8854`
- `market_context_high->fx_1h` score `-0.6132` n `133` status `ready` deltaP `-1.4205` edge `0.003` maxDD `-0.2373`
- `market_context_high->fx_4h` score `-0.6998` n `121` status `ready` deltaP `-0.6778` edge `0.0116` maxDD `-0.565`
- `market_context_high->commodity_4h` score `-1.0885` n `121` status `ready` deltaP `4.6739` edge `0.0213` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2159` n `133` status `ready` deltaP `-4.3908` edge `0.0118` maxDD `-2.7085`
- `market_context_high->equity_24h` score `-1.4953` n `119` status `ready` deltaP `6.6512` edge `-0.0712` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
