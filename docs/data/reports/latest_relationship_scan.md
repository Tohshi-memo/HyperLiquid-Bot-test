# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T00:37:14.042235+00:00`
- Price records: `672`
- Market context records: `1895`
- Flow alert records: `7354`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.2751` n `199` status `ready` deltaP `23.1186` edge `0.5666` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8445` n `199` status `ready` deltaP `27.8672` edge `0.5092` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3385` n `199` status `ready` deltaP `18.1104` edge `0.4432` maxDD `-9.8581`
- `market_context_high->metal_24h` score `2.6306` n `183` status `ready` deltaP `17.808` edge `0.3431` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3322` n `199` status `ready` deltaP `14.4296` edge `0.2076` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6572` n `183` status `ready` deltaP `12.8756` edge `0.5843` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.5708` n `183` status `ready` deltaP `9.9955` edge `0.1871` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6573` n `199` status `ready` deltaP `7.3933` edge `0.1041` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4224` n `199` status `ready` deltaP `6.6553` edge `0.1022` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.4099` n `199` status `ready` deltaP `9.7882` edge `0.0778` maxDD `-3.7119`
- `market_context_high->fx_24h` score `0.3258` n `183` status `ready` deltaP `15.699` edge `0.0274` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0448` n `199` status `ready` deltaP `5.2862` edge `0.0404` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.1547` n `183` status `ready` deltaP `8.8883` edge `0.4177` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-0.3726` n `183` status `ready` deltaP `17.8848` edge `0.7083` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4775` n `199` status `ready` deltaP `6.8802` edge `0.0265` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.4797` n `199` status `ready` deltaP `3.4371` edge `0.0323` maxDD `-3.6151`
- `market_context_high->index_1h` score `-0.6349` n `199` status `ready` deltaP `-0.1557` edge `0.0113` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6799` n `199` status `ready` deltaP `-3.6515` edge `0.0004` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.7384` n `199` status `ready` deltaP `11.9331` edge `0.1281` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.9403` n `199` status `ready` deltaP `-4.4291` edge `-0.0022` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
