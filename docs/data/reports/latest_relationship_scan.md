# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T01:52:25.763034+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.3126` n `91` status `ready` deltaP `7.4252` edge `0.264` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.5416` n `96` status `ready` deltaP `8.8668` edge `0.1582` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.4808` n `96` status `ready` deltaP `12.4564` edge `0.0705` maxDD `-0.4112`
- `market_context_high->commodity_24h` score `1.3931` n `91` status `ready` deltaP `16.3386` edge `0.253` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.2158` n `96` status `ready` deltaP `18.0894` edge `0.0383` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9487` n `96` status `ready` deltaP `11.1534` edge `0.1068` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7881` n `96` status `ready` deltaP `14.2652` edge `0.0093` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.4863` n `96` status `ready` deltaP `11.4329` edge `0.0913` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.3122` n `91` status `ready` deltaP `16.5598` edge `-0.063` maxDD `-0.3771`
- `market_context_high->unknown_1h` score `0.3055` n `96` status `ready` deltaP `9.0569` edge `-0.0122` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1224` n `96` status `ready` deltaP `5.6699` edge `0.0111` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.0619` n `96` status `ready` deltaP `6.1229` edge `0.0015` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.1207` n `96` status `ready` deltaP `5.3607` edge `0.0197` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3637` n `96` status `ready` deltaP `2.8256` edge `0.0147` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.3806` n `96` status `ready` deltaP `-2.2206` edge `0.0019` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4063` n `96` status `ready` deltaP `2.3827` edge `0.0165` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4675` n `96` status `ready` deltaP `2.4137` edge `0.009` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9149` n `96` status `ready` deltaP `-8.1899` edge `-0.0061` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.5846` n `91` status `ready` deltaP `-1.2458` edge `0.0822` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0427` n `91` status `ready` deltaP `-24.2617` edge `-0.0252` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
