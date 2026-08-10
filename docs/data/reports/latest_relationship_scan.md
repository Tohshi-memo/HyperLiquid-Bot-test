# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T13:52:25.151356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `0.9704` n `169` status `ready` deltaP `12.6037` edge `0.0683` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7467` n `136` status `ready` deltaP `18.7634` edge `0.0179` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6769` n `169` status `ready` deltaP `9.4214` edge `0.0279` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.0619` n `136` status `ready` deltaP `2.5563` edge `0.3015` maxDD `-21.0709`
- `market_context_high->fx_4h` score `0.0538` n `169` status `ready` deltaP `8.3192` edge `0.009` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1179` n `169` status `ready` deltaP `4.4166` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.4456` n `136` status `ready` deltaP `2.866` edge `0.0969` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7536` n `169` status `ready` deltaP `-1.978` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7759` n `169` status `ready` deltaP `-4.0596` edge `-0.0088` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-0.9507` n `136` status `ready` deltaP `-0.1746` edge `0.0501` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1979` n `169` status `ready` deltaP `-1.6068` edge `-0.0026` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2109` n `169` status `ready` deltaP `-1.8843` edge `-0.0101` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.5996` n `169` status `ready` deltaP `-9.2779` edge `-0.0411` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9289` n `169` status `ready` deltaP `-6.0002` edge `-0.0309` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2487` n `169` status `ready` deltaP `-11.4059` edge `-0.1288` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6618` n `169` status `ready` deltaP `-10.6898` edge `-0.0605` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0155` n `169` status `ready` deltaP `-12.6073` edge `-0.155` maxDD `-15.3937`
- `market_context_high->crypto_major_24h` score `-4.1309` n `136` status `ready` deltaP `-1.1571` edge `-0.0871` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.3163` n `136` status `ready` deltaP `-11.9075` edge `-0.136` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-8.6446` n `136` status `ready` deltaP `-5.3752` edge `-0.2009` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
