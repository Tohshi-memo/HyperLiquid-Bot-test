# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T23:37:16.760013+00:00`
- Price records: `672`
- Market context records: `1890`
- Flow alert records: `7341`
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

- `market_context_high->crypto_alt_4h` score `7.1703` n `199` status `ready` deltaP `22.8137` edge `0.5599` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7999` n `199` status `ready` deltaP `27.7148` edge `0.5065` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3385` n `199` status `ready` deltaP `18.1104` edge `0.4432` maxDD `-9.8581`
- `market_context_high->metal_24h` score `2.8857` n `183` status `ready` deltaP `17.9816` edge `0.3632` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.325` n `199` status `ready` deltaP `14.4296` edge `0.207` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.7103` n `183` status `ready` deltaP `10.6899` edge `0.1941` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.6548` n `183` status `ready` deltaP `12.8756` edge `0.5841` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5794` n `199` status `ready` deltaP `6.9442` edge `0.1006` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4135` n `199` status `ready` deltaP `9.7882` edge `0.0781` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.342` n `199` status `ready` deltaP `6.2062` edge `0.0985` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2782` n `183` status `ready` deltaP `15.1782` edge `0.0269` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.0511` n `183` status `ready` deltaP `9.5828` edge `0.4217` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.0916` n `199` status `ready` deltaP `4.9868` edge `0.0385` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.3546` n `183` status `ready` deltaP `17.8848` edge `0.7098` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4829` n `199` status `ready` deltaP `6.8802` edge `0.0258` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5468` n `199` status `ready` deltaP `2.988` edge `0.0297` maxDD `-3.6151`
- `market_context_high->index_1h` score `-0.6517` n `199` status `ready` deltaP `-0.3054` edge `0.0109` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6712` n `199` status `ready` deltaP `11.9331` edge `0.1337` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.7165` n `199` status `ready` deltaP `-4.2503` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9798` n `199` status `ready` deltaP `-5.0389` edge `-0.0032` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
