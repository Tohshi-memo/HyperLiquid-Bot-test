# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T03:52:20.321056+00:00`
- Price records: `672`
- Market context records: `2727`
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

- `market_context_high->crypto_alt_24h` score `11.3875` n `111` status `ready` deltaP `16.3523` edge `1.1893` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6664` n `111` status `ready` deltaP `17.4784` edge `0.6385` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.1893` n `111` status `ready` deltaP `6.5175` edge `0.8653` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.1045` n `143` status `ready` deltaP `7.3161` edge `0.1486` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0743` n `143` status `ready` deltaP `9.9416` edge `0.0274` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1581` n `143` status `ready` deltaP `3.2003` edge `0.0078` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1675` n `143` status `ready` deltaP `2.8988` edge `0.0398` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4245` n `143` status `ready` deltaP `16.5157` edge `0.2886` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5075` n `143` status `ready` deltaP `-0.1978` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.514` n `143` status `ready` deltaP `1.25` edge `0.0011` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5346` n `143` status `ready` deltaP `6.1451` edge `0.0665` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7785` n `143` status `ready` deltaP `-1.6991` edge `-0.0039` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9073` n `143` status `ready` deltaP `3.6473` edge `0.0463` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0165` n `143` status `ready` deltaP `-2.421` edge `0.0093` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.0198` n `111` status `ready` deltaP `1.9661` edge `-0.0109` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.2244` n `143` status `ready` deltaP `-4.2355` edge `0.0095` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3252` n `143` status `ready` deltaP `1.8186` edge `0.01` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6051` n `111` status `ready` deltaP `2.5807` edge `0.0864` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0647` n `143` status `ready` deltaP `-0.9444` edge `-0.0278` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3313` n `143` status `ready` deltaP `-1.8815` edge `-0.0313` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
