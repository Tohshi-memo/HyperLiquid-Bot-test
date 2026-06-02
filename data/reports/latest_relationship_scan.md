# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T14:07:25.638922+00:00`
- Price records: `672`
- Market context records: `2669`
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

- `market_context_high->crypto_alt_24h` score `9.2009` n `111` status `ready` deltaP `16.0051` edge `1.0094` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5378` n `111` status `ready` deltaP `17.1312` edge `0.6301` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.8326` n `123` status `ready` deltaP `24.0346` edge `0.5076` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.6908` n `123` status `ready` deltaP `11.5854` edge `0.328` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.3174` n `123` status `ready` deltaP `7.4187` edge `0.1653` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7077` n `132` status `ready` deltaP `8.9412` edge `0.1181` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `-0.0063` n `132` status `ready` deltaP `5.6115` edge `0.0812` maxDD `-4.2199`
- `market_context_high->fx_24h` score `-0.0946` n `111` status `ready` deltaP `11.3411` edge `0.0037` maxDD `-0.6418`
- `market_context_high->index_24h` score `-0.1326` n `111` status `ready` deltaP `7.4888` edge `0.0371` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1728` n `123` status `ready` deltaP `7.4695` edge `0.0122` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.2328` n `132` status `ready` deltaP `2.1503` edge `0.0242` maxDD `-1.9684`
- `market_context_high->index_1h` score `-0.2535` n `132` status `ready` deltaP `1.8599` edge `0.0045` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.365` n `132` status `ready` deltaP `3.3206` edge `0.0064` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.4826` n `123` status `ready` deltaP `1.7785` edge `0.0133` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.4898` n `111` status `ready` deltaP `7.9627` edge `0.1935` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5441` n `132` status `ready` deltaP `-0.7303` edge `0.0039` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6442` n `132` status `ready` deltaP `-1.0661` edge `-0.0007` maxDD `-2.3164`
- `market_context_high->metal_4h` score `-0.8142` n `123` status `ready` deltaP `0.7622` edge `0.0034` maxDD `-4.3625`
- `market_context_high->commodity_4h` score `-1.2569` n `123` status `ready` deltaP `3.252` edge `0.0092` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.3299` n `111` status `ready` deltaP `5.9967` edge `0.5458` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
