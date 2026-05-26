# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T23:07:20.221484+00:00`
- Price records: `672`
- Market context records: `1985`
- Flow alert records: `7605`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7584`

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

- `market_context_high->crypto_alt_4h` score `7.4602` n `233` status `ready` deltaP `22.7481` edge `0.5845` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0712` n `233` status `ready` deltaP `26.7069` edge `0.525` maxDD `-4.4354`
- `market_context_high->unknown_4h` score `2.7002` n `233` status `ready` deltaP `14.0401` edge `0.3245` maxDD `-9.447`
- `market_context_high->equity_4h` score `2.188` n `233` status `ready` deltaP `13.7823` edge `0.1999` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.9368` n `198` status `ready` deltaP `16.665` edge `0.2929` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.8158` n `198` status `ready` deltaP `16.6891` edge `0.5721` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.2808` n `198` status `ready` deltaP `15.3711` edge `0.4941` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.0687` n `233` status `ready` deltaP `9.9561` edge `0.1213` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8195` n `233` status `ready` deltaP `8.3794` edge `0.1238` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.52` n `198` status `ready` deltaP `19.8924` edge `0.7693` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.4856` n `198` status `ready` deltaP `4.0958` edge `0.136` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1178` n `233` status `ready` deltaP `7.0678` edge `0.0673` maxDD `-3.7016`
- `market_context_high->fx_24h` score `-0.0721` n `198` status `ready` deltaP `10.8343` edge `0.0211` maxDD `-1.2801`
- `market_context_high->equity_1h` score `-0.2003` n `233` status `ready` deltaP `4.0484` edge `0.0357` maxDD `-2.6836`
- `market_context_high->fx_1h` score `-0.6727` n `233` status `ready` deltaP `-3.4084` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6975` n `233` status `ready` deltaP `-0.4433` edge `0.008` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.1932` n `233` status `ready` deltaP `-9.0116` edge `-0.0041` maxDD `-1.1041`
- `market_context_high->metal_1h` score `-1.4081` n `233` status `ready` deltaP `2.1511` edge `0.0019` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4433` n `233` status `ready` deltaP `1.0434` edge `-0.0322` maxDD `-3.6022`
- `market_context_high->commodity_1h` score `-1.9031` n `233` status `ready` deltaP `1.6518` edge `0.0008` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
