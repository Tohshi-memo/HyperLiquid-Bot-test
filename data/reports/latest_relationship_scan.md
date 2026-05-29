# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T07:37:17.748651+00:00`
- Price records: `672`
- Market context records: `2224`
- Flow alert records: `8294`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.6892` n `33` status `ready` deltaP `57.6547` edge `1.8986` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.0038` n `33` status `ready` deltaP `48.0114` edge `0.9742` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.4812` n `33` status `ready` deltaP `38.9836` edge `0.895` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.9355` n `132` status `ready` deltaP `37.4538` edge `0.9219` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6894` n `132` status `ready` deltaP `41.6713` edge `0.7493` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `10.1406` n `33` status `ready` deltaP `38.5575` edge `0.6106` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.9982` n `33` status `ready` deltaP `20.5019` edge `0.9468` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.467` n `132` status `ready` deltaP `21.2214` edge `0.382` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9377` n `43` status `ready` deltaP `32.9197` edge `0.3525` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3314` n `132` status `ready` deltaP `23.1107` edge `0.233` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.2174` n `132` status `ready` deltaP `26.6214` edge `0.159` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1709` n `137` status `ready` deltaP `17.303` edge `0.1966` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.017` n `137` status `ready` deltaP `16.5731` edge `0.2273` maxDD `-4.9097`
- `news_risk_high->fx_24h` score `2.976` n `33` status `ready` deltaP `31.0606` edge `0.0594` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.5134` n `33` status `ready` deltaP `-1.0733` edge `0.2983` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2036` n `43` status `ready` deltaP `27.8892` edge `0.0161` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `1.8336` n `132` status `ready` deltaP `24.1636` edge `0.4732` maxDD `-32.8525`
- `market_context_high->index_24h` score `1.7495` n `132` status `ready` deltaP `9.1698` edge `0.2075` maxDD `-4.1604`
- `news_risk_high->index_24h` score `1.6776` n `33` status `ready` deltaP `11.4426` edge `0.1054` maxDD `-1.3507`
- `news_risk_high->unknown_1h` score `1.37` n `43` status `ready` deltaP `20.8954` edge `0.0218` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
