# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T04:22:31.418117+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.7644` n `90` status `ready` deltaP `-3.592` edge `3.3082` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.96` n `62` status `ready` deltaP `38.663` edge `0.6759` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0817` n `62` status `ready` deltaP `22.8679` edge `0.5721` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.4862` n `62` status `ready` deltaP `16.3463` edge `0.4415` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.9217` n `62` status `ready` deltaP `35.7513` edge `0.1718` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.4562` n `90` status `ready` deltaP `10.829` edge `0.7965` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.0617` n `62` status `ready` deltaP `33.3064` edge `0.0593` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4803` n `62` status `ready` deltaP `10.1748` edge `0.1744` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4551` n `90` status `ready` deltaP `16.7275` edge `0.1895` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.3799` n `62` status `ready` deltaP `18.4834` edge `0.1349` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0116` n `62` status `ready` deltaP `25.1739` edge `0.0148` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.9817` n `90` status `ready` deltaP `13.909` edge `0.1153` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.544` n `62` status `ready` deltaP `-6.567` edge `0.297` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.447` n `62` status `ready` deltaP `21.0144` edge `0.087` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2369` n `90` status `ready` deltaP `21.5371` edge `0.1635` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.1262` n `62` status `ready` deltaP `3.1582` edge `0.1247` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0659` n `90` status `ready` deltaP `21.7351` edge `0.0186` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7118` n `90` status `ready` deltaP `11.9461` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1471` n `90` status `ready` deltaP `10.1031` edge `0.0404` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1433` n `90` status `ready` deltaP `7.1964` edge `0.5642` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
