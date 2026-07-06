# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T02:37:26.604270+00:00`
- Price records: `672`
- Market context records: `5836`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.6324` n `267` status `ready` deltaP `7.6465` edge `0.1475` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.3159` n `267` status `ready` deltaP `1.2363` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4133` n `267` status `ready` deltaP `4.1631` edge `0.0385` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5313` n `267` status `ready` deltaP `-0.8635` edge `-0.0021` maxDD `-2.1545`
- `market_context_high->index_1h` score `-0.5438` n `267` status `ready` deltaP `1.3877` edge `0.0058` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.5689` n `239` status `ready` deltaP `15.7776` edge `0.3553` maxDD `-31.6316`
- `market_context_high->metal_1h` score `-0.6246` n `267` status `ready` deltaP `2.2113` edge `0.0003` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-1.0088` n `267` status `ready` deltaP `2.5858` edge `0.0308` maxDD `-6.2348`
- `market_context_high->index_4h` score `-1.1743` n `267` status `ready` deltaP `0.5961` edge `0.0142` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.1796` n `267` status `ready` deltaP `1.0877` edge `0.0279` maxDD `-6.6758`
- `market_context_high->fx_4h` score `-1.644` n `267` status `ready` deltaP `-2.169` edge `-0.0014` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.6451` n `239` status `ready` deltaP `7.4834` edge `0.021` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.2052` n `267` status `ready` deltaP `-5.1744` edge `-0.0451` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.5489` n `267` status `ready` deltaP `-0.8222` edge `-0.0146` maxDD `-8.0531`
- `market_context_high->index_24h` score `-2.8985` n `239` status `ready` deltaP `2.9194` edge `0.0234` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.1374` n `267` status `ready` deltaP `6.2837` edge `0.1339` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.9012` n `267` status `ready` deltaP `3.8275` edge `0.0669` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.0756` n `239` status `ready` deltaP `0.1402` edge `-0.2056` maxDD `-9.1308`
- `market_context_high->commodity_24h` score `-8.7095` n `239` status `ready` deltaP `-10.8969` edge `-0.0572` maxDD `-30.3426`
- `market_context_high->crypto_alt_24h` score `-12.8122` n `239` status `ready` deltaP `-12.046` edge `-0.5316` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
