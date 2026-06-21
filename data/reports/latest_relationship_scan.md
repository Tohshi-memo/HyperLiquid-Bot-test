# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T00:07:29.097938+00:00`
- Price records: `672`
- Market context records: `4260`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10816`

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

- `risk_on_high->unknown_4h` score `131.4492` n `44` status `ready` deltaP `-2.8132` edge `11.1547` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.4492` n `44` status `ready` deltaP `-2.8132` edge `11.1547` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.9106` n `232` status `ready` deltaP `1.8352` edge `2.4716` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.9851` n `220` status `ready` deltaP `-1.9041` edge `1.2211` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.3501` n `200` status `ready` deltaP `-9.6042` edge `1.0799` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.8933` n `44` status `ready` deltaP `31.8736` edge `-0.05` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8933` n `44` status `ready` deltaP `31.8736` edge `-0.05` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.6024` n `44` status `ready` deltaP `13.7334` edge `0.0252` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.6024` n `44` status `ready` deltaP `13.7334` edge `0.0252` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.362` n `44` status `ready` deltaP `7.4442` edge `0.0035` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.362` n `44` status `ready` deltaP `7.4442` edge `0.0035` maxDD `-0.1704`
- `risk_on_high->commodity_24h` score `0.1271` n `40` status `ready` deltaP `-1.3889` edge `0.248` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.1271` n `40` status `ready` deltaP `-1.3889` edge `0.248` maxDD `-12.9187`
- `risk_on_high->crypto_major_1h` score `0.0014` n `44` status `ready` deltaP `6.8999` edge `0.0084` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0014` n `44` status `ready` deltaP `6.8999` edge `0.0084` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0021` n `44` status `ready` deltaP `8.1763` edge `0.0043` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0021` n `44` status `ready` deltaP `8.1763` edge `0.0043` maxDD `-0.3925`
- `risk_on_high->metal_24h` score `-0.0787` n `40` status `ready` deltaP `-25.5556` edge `0.2217` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `-0.0787` n `40` status `ready` deltaP `-25.5556` edge `0.2217` maxDD `-1.9133`
- `risk_on_high->equity_1h` score `-0.1568` n `44` status `ready` deltaP `6.3283` edge `-0.0163` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
