# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T10:52:20.283162+00:00`
- Price records: `672`
- Market context records: `2655`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.9963` n `122` status `ready` deltaP `17.3526` edge `0.5835` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `7.2439` n `122` status `ready` deltaP `11.8226` edge `0.8742` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `5.3314` n `122` status `ready` deltaP `25.4074` edge `0.5428` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.0277` n `122` status `ready` deltaP `16.221` edge `0.4085` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9104` n `122` status `ready` deltaP `10.2559` edge `0.1958` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0131` n `133` status `ready` deltaP `9.0991` edge `0.1425` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.6292` n `122` status `ready` deltaP `10.0069` edge `0.0838` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.4852` n `133` status `ready` deltaP `6.8468` edge `0.1142` maxDD `-4.2199`
- `market_context_high->metal_4h` score `0.0603` n `122` status `ready` deltaP `7.1472` edge `0.039` maxDD `-2.5301`
- `market_context_high->index_4h` score `0.02` n `122` status `ready` deltaP `7.8169` edge `0.0337` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1166` n `133` status `ready` deltaP `3.8528` edge `0.014` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1575` n `133` status `ready` deltaP `2.3423` edge `0.0292` maxDD `-1.9684`
- `market_context_high->fx_24h` score `-0.4866` n `122` status `ready` deltaP `7.0184` edge `-0.0001` maxDD `-0.6461`
- `market_context_high->commodity_1h` score `-0.5103` n `133` status `ready` deltaP `2.9276` edge `0.0029` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5571` n `133` status `ready` deltaP `-1.2809` edge `0.0015` maxDD `-1.8175`
- `market_context_high->fx_1h` score `-0.6132` n `133` status `ready` deltaP `-1.4205` edge `0.003` maxDD `-0.2373`
- `market_context_high->fx_4h` score `-0.7983` n `122` status `ready` deltaP `-1.7718` edge `0.0113` maxDD `-0.6141`
- `market_context_high->equity_1h` score `-1.086` n `133` status `ready` deltaP `-3.1864` edge `0.0146` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.1655` n `122` status `ready` deltaP `4.2133` edge `0.0145` maxDD `-10.0279`
- `market_context_high->equity_24h` score `-1.4027` n `122` status `ready` deltaP `7.2092` edge `-0.0672` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
