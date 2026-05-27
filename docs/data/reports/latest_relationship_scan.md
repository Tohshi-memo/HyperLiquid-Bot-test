# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T06:37:14.657798+00:00`
- Price records: `672`
- Market context records: `2017`
- Flow alert records: `7698`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9085`

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

- `market_context_high->crypto_major_4h` score `8.917` n `206` status `ready` deltaP `30.8519` edge `0.5904` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4019` n `206` status `ready` deltaP `24.6492` edge `0.6503` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9148` n `206` status `ready` deltaP `18.8122` edge `0.4424` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8803` n `206` status `ready` deltaP `16.5863` edge `0.2389` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.4997` n `206` status `ready` deltaP `12.2086` edge `0.1422` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.2954` n `206` status `ready` deltaP `12.1211` edge `0.0955` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.1982` n `206` status `ready` deltaP `9.8134` edge `0.1458` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.3255` n `188` status `ready` deltaP `15.9101` edge `0.4531` maxDD `-35.8966`
- `market_context_high->equity_1h` score `0.1882` n `206` status `ready` deltaP `6.738` edge `0.0496` maxDD `-2.6402`
- `market_context_high->metal_24h` score `0.179` n `188` status `ready` deltaP `12.4526` edge `0.1745` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.1385` n `188` status `ready` deltaP `14.7734` edge `0.4029` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `0.0775` n `206` status `ready` deltaP `3.9475` edge `0.0521` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.1565` n `188` status `ready` deltaP `3.0749` edge `0.0893` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.2364` n `188` status `ready` deltaP `12.9336` edge `0.0256` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3716` n `206` status `ready` deltaP `1.811` edge `0.016` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8447` n `206` status `ready` deltaP `-1.2339` edge `0.0006` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-1.0001` n `206` status `ready` deltaP `2.9853` edge `0.0155` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.5187` n `206` status `ready` deltaP `-5.6122` edge `-0.001` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.5879` n `206` status `ready` deltaP `7.101` edge `0.0826` maxDD `-11.9812`
- `market_context_high->commodity_1h` score `-1.8327` n `206` status `ready` deltaP `2.9896` edge `0.0009` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
