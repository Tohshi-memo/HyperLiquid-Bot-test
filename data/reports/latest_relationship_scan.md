# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T19:52:30.310490+00:00`
- Price records: `672`
- Market context records: `7596`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.7506` n `143` status `ready` deltaP `18.0381` edge `0.5606` maxDD `-41.7701`
- `market_context_high->unknown_24h` score `0.5604` n `144` status `ready` deltaP `13.0209` edge `0.1211` maxDD `-5.5516`
- `market_context_high->commodity_24h` score `0.4889` n `143` status `ready` deltaP `16.1388` edge `0.0915` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0947` n `148` status `ready` deltaP `7.2073` edge `0.012` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.0768` n `148` status `ready` deltaP `7.5006` edge `0.0196` maxDD `-2.4139`
- `market_context_high->crypto_major_1h` score `-0.1847` n `148` status `ready` deltaP `7.659` edge `0.0213` maxDD `-4.0162`
- `market_context_high->commodity_1h` score `-0.2097` n `148` status `ready` deltaP `4.4294` edge `0.0008` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.2529` n `148` status `ready` deltaP `1.8005` edge `0.0188` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.2646` n `143` status `ready` deltaP `9.9169` edge `0.0206` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4321` n `148` status `ready` deltaP `6.6817` edge `0.0563` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.6144` n `148` status `ready` deltaP `9.4202` edge `0.0302` maxDD `-3.4082`
- `market_context_high->fx_1h` score `-0.6316` n `148` status `ready` deltaP `-0.1501` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6437` n `148` status `ready` deltaP `1.1895` edge `0.0141` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9881` n `148` status `ready` deltaP `-0.6029` edge `-0.0603` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.0635` n `148` status `ready` deltaP `2.7027` edge `0.0513` maxDD `-9.7866`
- `market_context_high->crypto_major_4h` score `-1.2001` n `148` status `ready` deltaP `8.3265` edge `0.0637` maxDD `-14.8454`
- `market_context_high->equity_4h` score `-1.4963` n `148` status `ready` deltaP `3.2751` edge `0.2113` maxDD `-20.9976`
- `market_context_high->metal_4h` score `-1.6665` n `148` status `ready` deltaP `-1.6809` edge `0.0446` maxDD `-4.7638`
- `market_context_high->metal_24h` score `-1.9503` n `144` status `ready` deltaP `-1.5625` edge `0.1157` maxDD `-9.0925`
- `market_context_high->fx_4h` score `-2.498` n `148` status `ready` deltaP `-5.3848` edge `-0.0038` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
