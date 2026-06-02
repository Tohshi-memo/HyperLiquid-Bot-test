# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T20:37:27.013253+00:00`
- Price records: `672`
- Market context records: `2697`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `10.0939` n `111` status `ready` deltaP `16.3523` edge `1.0815` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6719` n `111` status `ready` deltaP `17.652` edge `0.6378` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.876` n `141` status `ready` deltaP `5.876` edge `0.1388` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2177` n `141` status `ready` deltaP `11.5897` edge `0.0348` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1427` n `143` status `ready` deltaP `2.8988` edge `0.0416` maxDD `-3.1587`
- `market_context_high->index_1h` score `-0.1518` n `143` status `ready` deltaP `3.2003` edge `0.0086` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4291` n `143` status `ready` deltaP `1.9985` edge `0.007` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4668` n `143` status `ready` deltaP `0.2513` edge `0.0038` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.5026` n `141` status `ready` deltaP `16.4343` edge `0.2813` maxDD `-28.6198`
- `market_context_high->crypto_major_24h` score `-0.5281` n `111` status `ready` deltaP `5.9967` edge `0.6486` maxDD `-44.169`
- `market_context_high->crypto_alt_1h` score `-0.5284` n `143` status `ready` deltaP `6.4445` edge `0.0653` maxDD `-10.747`
- `market_context_high->fx_24h` score `-0.5378` n `111` status `ready` deltaP `7.0008` edge `-0.0043` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.7454` n `141` status `ready` deltaP `-0.507` edge `0.0108` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-0.7458` n `143` status `ready` deltaP `-1.25` edge `-0.0027` maxDD `-3.0996`
- `market_context_high->commodity_24h` score `-0.8478` n `111` status `ready` deltaP `6.7474` edge `0.1557` maxDD `-12.4171`
- `market_context_high->index_24h` score `-0.9915` n `111` status `ready` deltaP `3.3221` edge `-0.0067` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `-1.0009` n `143` status `ready` deltaP `3.3479` edge `0.0363` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0193` n `141` status `ready` deltaP `4.4445` edge `0.0317` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2391` n `143` status `ready` deltaP `-4.4857` edge `0.0105` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-2.053` n `141` status `ready` deltaP `-1.5201` edge `-0.0205` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
