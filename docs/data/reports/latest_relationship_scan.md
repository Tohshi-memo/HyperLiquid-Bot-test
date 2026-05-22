# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T05:07:19.081493+00:00`
- Price records: `672`
- Market context records: `1495`
- Flow alert records: `6215`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8811`

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

- `market_context_high->metal_24h` score `12.3709` n `172` status `ready` deltaP `20.4982` edge `1.0068` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.4852` n `172` status `ready` deltaP `28.985` edge `0.9655` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.3712` n `172` status `ready` deltaP `27.3538` edge `0.7951` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9002` n `172` status `ready` deltaP `20.3327` edge `0.2981` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.2457` n `172` status `ready` deltaP `13.6144` edge `0.4124` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2853` n `199` status `ready` deltaP `7.0053` edge `0.1434` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9883` n `172` status `ready` deltaP `19.8401` edge `0.055` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1747` n `199` status `ready` deltaP `1.7038` edge `0.0341` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2505` n `199` status `ready` deltaP `2.4953` edge `0.009` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.2592` n `199` status `ready` deltaP `10.4937` edge `0.2404` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.4726` n `199` status `ready` deltaP `1.737` edge `0.0514` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.513` n `199` status `ready` deltaP `0.0692` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.687` n `199` status `ready` deltaP `6.276` edge `0.1718` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7796` n `199` status `ready` deltaP `5.2546` edge `-0.0014` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.9307` n `199` status `ready` deltaP `-1.8538` edge `0.0437` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.9648` n `199` status `ready` deltaP `-3.2548` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.0879` n `199` status `ready` deltaP `-0.0481` edge `0.0018` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.2073` n `199` status `ready` deltaP `11.3517` edge `0.0929` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.5068` n `199` status `ready` deltaP `-0.8824` edge `0.016` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.3312` n `199` status `ready` deltaP `-14.2879` edge `-0.0884` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
