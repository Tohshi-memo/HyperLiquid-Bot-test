# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T14:37:18.020053+00:00`
- Price records: `672`
- Market context records: `1126`
- Flow alert records: `5146`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8733`

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

- `market_context_high->crypto_major_24h` score `19.1751` n `150` status `ready` deltaP `41.2014` edge `1.3696` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `8.953` n `150` status `ready` deltaP `17.5625` edge `0.7524` maxDD `-9.5387`
- `market_context_high->equity_24h` score `7.0206` n `150` status `ready` deltaP `17.0416` edge `0.5211` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5571` n `150` status `ready` deltaP `-1.8889` edge `0.6424` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.4894` n `150` status `ready` deltaP `15.6527` edge `0.3839` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.6294` n `168` status `ready` deltaP `9.4222` edge `0.1393` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.7128` n `168` status `ready` deltaP `6.7653` edge `0.0826` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4115` n `168` status `ready` deltaP `6.8969` edge `0.02` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3088` n `168` status `ready` deltaP `2.8799` edge `0.0443` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1484` n `168` status `ready` deltaP `8.4652` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0573` n `168` status `ready` deltaP `7.1322` edge `0.0338` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `-0.0627` n `168` status `ready` deltaP `7.5421` edge `0.1338` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.27` n `168` status `ready` deltaP `6.651` edge `-0.0058` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2802` n `168` status `ready` deltaP `2.9441` edge `0.0413` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.7123` n `168` status `ready` deltaP `-1.775` edge `0.0013` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.7215` n `168` status `ready` deltaP `0.9364` edge `0.0009` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1289` n `168` status `ready` deltaP `4.9289` edge `0.1189` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.5334` n `168` status `ready` deltaP `5.9378` edge `-0.0553` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.0809` n `168` status `ready` deltaP `-10.9683` edge `-0.0051` maxDD `-13.0076`
- `market_context_high->unknown_24h` score `-3.3882` n `150` status `ready` deltaP `1.8472` edge `-0.0217` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
