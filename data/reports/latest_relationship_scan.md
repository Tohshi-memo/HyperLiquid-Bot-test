# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T23:22:13.835679+00:00`
- Price records: `672`
- Market context records: `1889`
- Flow alert records: `7338`
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

- `market_context_high->crypto_alt_4h` score `7.1655` n `199` status `ready` deltaP `22.8137` edge `0.5595` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8035` n `199` status `ready` deltaP `27.7148` edge `0.5068` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3373` n `199` status `ready` deltaP `18.1104` edge `0.4431` maxDD `-9.8581`
- `market_context_high->metal_24h` score `2.9433` n `183` status `ready` deltaP `17.9816` edge `0.368` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3358` n `199` status `ready` deltaP `14.4296` edge `0.2079` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.7494` n `183` status `ready` deltaP `10.8635` edge `0.1962` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.6548` n `183` status `ready` deltaP `12.8756` edge `0.5841` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5818` n `199` status `ready` deltaP `6.9442` edge `0.1008` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4183` n `199` status `ready` deltaP `9.7882` edge `0.0785` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.348` n `199` status `ready` deltaP `6.2062` edge `0.099` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2619` n `183` status `ready` deltaP `15.0045` edge `0.0267` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.0132` n `183` status `ready` deltaP `9.7564` edge `0.4237` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.0892` n `199` status `ready` deltaP `4.9868` edge `0.0387` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.3378` n `183` status `ready` deltaP `17.8848` edge `0.7112` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.486` n `199` status `ready` deltaP `6.8802` edge `0.0254` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5648` n `199` status `ready` deltaP `2.8383` edge `0.0292` maxDD `-3.6151`
- `market_context_high->index_1h` score `-0.6505` n `199` status `ready` deltaP `-0.3054` edge `0.011` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6556` n `199` status `ready` deltaP `11.9331` edge `0.135` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.7259` n `199` status `ready` deltaP `-4.4` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9821` n `199` status `ready` deltaP `-5.0389` edge `-0.0035` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
