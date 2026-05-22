# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T03:52:13.031110+00:00`
- Price records: `672`
- Market context records: `1490`
- Flow alert records: `6199`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->crypto_alt_24h` score `11.8356` n `172` status `ready` deltaP `28.985` edge `0.9947` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.7705` n `172` status `ready` deltaP `18.4593` edge `0.9912` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `10.7936` n `172` status `ready` deltaP `27.3538` edge `0.8303` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.983` n `172` status `ready` deltaP `20.3327` edge `0.305` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5685` n `172` status `ready` deltaP `13.6144` edge `0.4393` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4546` n `204` status `ready` deltaP `7.5473` edge `0.1539` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.7964` n `172` status `ready` deltaP `17.8012` edge `0.0526` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.0286` n `204` status `ready` deltaP `11.3313` edge `0.2588` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0419` n `204` status `ready` deltaP `2.5537` edge `0.0395` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1705` n `204` status `ready` deltaP `3.0293` edge `0.0121` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5436` n `204` status `ready` deltaP `-0.4755` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5464` n `204` status `ready` deltaP `1.3092` edge `0.0481` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.6015` n `204` status `ready` deltaP `7.2244` edge `0.1726` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7345` n `204` status `ready` deltaP `5.9117` edge `0.0` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.7953` n `204` status `ready` deltaP `-1.0162` edge `0.0494` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.9892` n `204` status `ready` deltaP `-3.7243` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.0903` n `204` status `ready` deltaP `-0.1086` edge `0.002` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.4085` n `204` status `ready` deltaP `10.1417` edge `0.0842` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.6037` n `204` status `ready` deltaP `-1.3737` edge `0.0112` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.2117` n `204` status `ready` deltaP `-13.3997` edge `-0.079` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
