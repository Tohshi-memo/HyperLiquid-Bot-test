# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T05:52:31.013412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10952`

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

- `market_context_high->commodity_4h` score `1.3299` n `167` status `ready` deltaP `15.138` edge `0.0772` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.0238` n `136` status `ready` deltaP `20.578` edge `0.0289` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8423` n `169` status `ready` deltaP `11.0681` edge `0.0307` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.1415` n `167` status `ready` deltaP `9.0851` edge `0.0112` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.079` n `169` status `ready` deltaP `5.0154` edge `0.0016` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6201` n `136` status `ready` deltaP `1.7054` edge `0.0901` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7703` n `169` status `ready` deltaP `-2.1277` edge `-0.0023` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8288` n `169` status `ready` deltaP `-4.9578` edge `-0.0096` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.0561` n `167` status `ready` deltaP `-0.2784` edge `-0.0079` maxDD `-1.26`
- `market_context_high->equity_1h` score `-1.1921` n `169` status `ready` deltaP `-1.4571` edge `-0.0026` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.2059` n `136` status `ready` deltaP `-2.3897` edge `0.0436` maxDD `-2.9193`
- `market_context_high->crypto_alt_1h` score `-1.4881` n `169` status `ready` deltaP `-8.0803` edge `-0.0348` maxDD `-5.5029`
- `market_context_high->equity_24h` score `-1.7161` n `136` status `ready` deltaP `-2.0833` edge `0.1852` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-1.9248` n `167` status `ready` deltaP `-5.9077` edge `-0.031` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0258` n `167` status `ready` deltaP `-9.8921` edge `-0.11` maxDD `-7.9584`
- `market_context_high->crypto_major_1h` score `-3.4904` n `169` status `ready` deltaP `-9.3425` edge `-0.0552` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8413` n `167` status `ready` deltaP `-10.9373` edge `-0.1438` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3774` n `136` status `ready` deltaP `-11.8771` edge `-0.1413` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8148` n `136` status `ready` deltaP `-2.4918` edge `-0.1352` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5287` n `169` status `ready` deltaP `-4.5876` edge `-0.5511` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
