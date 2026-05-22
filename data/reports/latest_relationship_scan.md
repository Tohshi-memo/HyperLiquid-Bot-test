# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T09:07:16.502638+00:00`
- Price records: `672`
- Market context records: `1512`
- Flow alert records: `6264`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `14.0856` n `159` status `ready` deltaP `23.3327` edge `1.1183` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1618` n `159` status `ready` deltaP `28.8424` edge `0.9395` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7951` n `159` status `ready` deltaP `28.0628` edge `0.8257` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6706` n `159` status `ready` deltaP `19.6672` edge `0.2834` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4385` n `159` status `ready` deltaP `12.8538` edge `0.3502` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0245` n `159` status `ready` deltaP `19.1071` edge `0.0629` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.9194` n `185` status `ready` deltaP `5.9418` edge `0.12` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.3345` n `193` status `ready` deltaP `1.9849` edge `0.0054` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3771` n `193` status `ready` deltaP `0.2692` edge `0.0268` maxDD `-2.8014`
- `market_context_high->crypto_alt_1h` score `-0.4775` n `193` status `ready` deltaP `0.7423` edge `0.0362` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.487` n `193` status `ready` deltaP `0.5236` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7636` n `193` status `ready` deltaP `-0.6391` edge `-0.0015` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7647` n `193` status `ready` deltaP `5.2558` edge `0.0005` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.788` n `185` status `ready` deltaP `8.9749` edge `0.1711` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8353` n `185` status `ready` deltaP `5.0247` edge `0.1303` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.9732` n `193` status `ready` deltaP `-0.5817` edge `0.0148` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.1648` n `185` status `ready` deltaP `10.9978` edge `0.0988` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.3186` n `185` status `ready` deltaP `-4.2873` edge `0.0276` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6537` n `185` status `ready` deltaP `-5.1624` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-1.7462` n `159` status `ready` deltaP `-2.4076` edge `0.1435` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
