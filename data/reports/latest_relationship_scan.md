# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T17:07:26.959959+00:00`
- Price records: `672`
- Market context records: `2682`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.2021` n `111` status `ready` deltaP `16.0051` edge `1.0095` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7644` n `111` status `ready` deltaP `17.9993` edge `0.6432` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `1.9987` n `132` status `ready` deltaP `19.4337` edge `0.3467` maxDD `-18.7758`
- `market_context_high->unknown_4h` score `1.3938` n `132` status `ready` deltaP `7.428` edge `0.1716` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.1036` n `132` status `ready` deltaP `10.1303` edge `0.0299` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1633` n `141` status `ready` deltaP `2.8454` edge `0.0095` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1903` n `141` status `ready` deltaP `2.8135` edge `0.0382` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.3002` n `111` status `ready` deltaP `9.4313` edge `-0.0007` maxDD `-0.6418`
- `market_context_high->crypto_major_4h` score `-0.3534` n `132` status `ready` deltaP `7.5943` edge `0.189` maxDD `-18.4617`
- `market_context_high->commodity_1h` score `-0.405` n `141` status `ready` deltaP `2.2221` edge `0.0086` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4667` n `141` status `ready` deltaP `0.2368` edge `0.0039` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.4824` n `141` status `ready` deltaP `6.848` edge `0.0685` maxDD `-10.747`
- `market_context_high->commodity_24h` score `-0.535` n `111` status `ready` deltaP `7.9627` edge `0.1877` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.575` n `132` status `ready` deltaP `0.7437` edge `0.0125` maxDD `-0.5631`
- `market_context_high->index_24h` score `-0.6005` n `111` status `ready` deltaP `5.4054` edge `0.012` maxDD `-2.5127`
- `market_context_high->metal_1h` score `-0.7966` n `141` status `ready` deltaP `-2.0332` edge `-0.0057` maxDD `-2.9635`
- `market_context_high->crypto_major_1h` score `-0.9695` n `141` status `ready` deltaP `3.7117` edge `0.0379` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1692` n `141` status `ready` deltaP `-4.1512` edge `0.0141` maxDD `-2.7085`
- `market_context_high->crypto_major_24h` score `-1.2028` n `111` status `ready` deltaP `5.9967` edge `0.5621` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.2371` n `132` status `ready` deltaP `3.3167` edge `0.0113` maxDD `-10.0279`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
