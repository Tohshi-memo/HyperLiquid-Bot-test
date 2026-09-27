# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T07:07:30.153522+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `news_risk_high->unknown_24h` score `1708.9044` n `118` status `ready` deltaP `1.2153` edge `142.4006` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.8286` n `48` status `ready` deltaP `10.6413` edge `8.5861` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.6725` n `44` status `ready` deltaP `30.1926` edge `4.2232` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.7982` n `44` status `ready` deltaP `14.9148` edge `2.3384` maxDD `-2.7051`
- `market_context_high->equity_24h` score `28.0636` n `44` status `ready` deltaP `36.0954` edge `2.1294` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9209` n `44` status `ready` deltaP `33.4912` edge `0.4456` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9059` n `44` status `ready` deltaP `34.5644` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.1301` n `44` status `ready` deltaP `34.9362` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7169` n `44` status `ready` deltaP `15.3825` edge `0.1615` maxDD `-1.3444`
- `market_context_high->equity_1h` score `0.9791` n `48` status `ready` deltaP `11.7266` edge `0.0437` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.9382` n `44` status `ready` deltaP `7.4834` edge `0.0909` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `0.8162` n `44` status `ready` deltaP `6.6103` edge `0.1144` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.8039` n `48` status `ready` deltaP `7.7221` edge `0.1013` maxDD `-4.8632`
- `news_risk_high->index_24h` score `0.6001` n `118` status `ready` deltaP `13.73` edge `0.028` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.5714` n `48` status `ready` deltaP `9.4935` edge `0.008` maxDD `-0.2275`
- `market_context_high->crypto_alt_1h` score `0.5651` n `48` status `ready` deltaP `7.1108` edge `0.0886` maxDD `-5.7799`
- `news_risk_high->metal_24h` score `0.5531` n `118` status `ready` deltaP `14.9188` edge `0.1239` maxDD `-6.8481`
- `market_context_high->fx_1h` score `0.3755` n `48` status `ready` deltaP `11.4895` edge `0.0072` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1342` n `48` status `ready` deltaP `4.9401` edge `0.0101` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.148` n `140` status `ready` deltaP `2.0531` edge `0.003` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
