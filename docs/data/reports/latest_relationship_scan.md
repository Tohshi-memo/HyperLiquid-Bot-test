# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T05:52:25.404357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `32.9432` n `132` status `ready` deltaP `-17.5239` edge `3.1075` maxDD `-9.6329`
- `market_context_high->commodity_1h` score `0.6633` n `180` status `ready` deltaP `9.3114` edge `0.0275` maxDD `-0.7439`
- `market_context_high->commodity_4h` score `0.643` n `169` status `ready` deltaP `10.3267` edge `0.0562` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.5472` n `132` status `ready` deltaP `17.883` edge `0.0317` maxDD `-1.4613`
- `market_context_high->commodity_24h` score `0.5234` n `132` status `ready` deltaP `12.4594` edge `0.1691` maxDD `-9.8043`
- `market_context_high->fx_4h` score `-0.2437` n `169` status `ready` deltaP `3.7683` edge `0.0041` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2742` n `180` status `ready` deltaP `1.6866` edge `-0.0015` maxDD `-0.5914`
- `market_context_high->index_1h` score `-0.8545` n `180` status `ready` deltaP `-7.0758` edge `-0.0047` maxDD `-0.948`
- `market_context_high->metal_1h` score `-0.9815` n `180` status `ready` deltaP `-7.2488` edge `-0.0139` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.4153` n `169` status `ready` deltaP `-3.0622` edge `-0.0081` maxDD `-1.4875`
- `market_context_high->equity_1h` score `-1.4942` n `180` status `ready` deltaP `-6.8662` edge `-0.0181` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.4479` n `132` status `ready` deltaP `0.367` edge `-0.074` maxDD `-2.9283`
- `market_context_high->crypto_alt_1h` score `-2.6285` n `180` status `ready` deltaP `-9.1084` edge `-0.0398` maxDD `-6.4812`
- `market_context_high->crypto_major_1h` score `-3.4527` n `180` status `ready` deltaP `-7.8011` edge `-0.0453` maxDD `-11.9002`
- `market_context_high->metal_4h` score `-3.4885` n `169` status `ready` deltaP `-10.0979` edge `-0.047` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.9862` n `169` status `ready` deltaP `-12.5467` edge `-0.1165` maxDD `-15.8728`
- `market_context_high->index_24h` score `-4.2684` n `132` status `ready` deltaP `-13.93` edge `-0.0533` maxDD `-6.7627`
- `market_context_high->crypto_alt_4h` score `-6.7029` n `169` status `ready` deltaP `-12.8511` edge `-0.1381` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-7.1284` n `132` status `ready` deltaP `-15.5343` edge `-0.2332` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.0552` n `132` status `ready` deltaP `-11.4265` edge `-0.1986` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
