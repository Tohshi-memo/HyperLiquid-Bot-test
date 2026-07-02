# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T10:22:25.670123+00:00`
- Price records: `672`
- Market context records: `5445`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->equity_24h` score `4.2075` n `185` status `ready` deltaP `11.8694` edge `0.6251` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.3955` n `196` status `ready` deltaP `16.1554` edge `0.4045` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.3517` n `185` status `ready` deltaP `17.7647` edge `0.6149` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.8201` n `196` status `ready` deltaP `13.2715` edge `0.3104` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.5993` n `196` status `ready` deltaP `11.2183` edge `0.3059` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5802` n `198` status `ready` deltaP `8.7719` edge `0.0864` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2839` n `185` status `ready` deltaP `11.5184` edge `0.0364` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1659` n `198` status `ready` deltaP `6.8651` edge `0.0174` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2811` n `198` status `ready` deltaP `1.3095` edge `0.064` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.3039` n `198` status `ready` deltaP `3.6291` edge `0.018` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.3786` n `198` status `ready` deltaP `2.3392` edge `0.0774` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5731` n `198` status `ready` deltaP `0.1679` edge `0.0` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7455` n `196` status `ready` deltaP `8.1446` edge `0.0445` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.1214` n `185` status `ready` deltaP `16.1627` edge `0.0974` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1564` n `196` status `ready` deltaP `0.4418` edge `0.0032` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4692` n `198` status `ready` deltaP `-3.1422` edge `-0.0067` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6743` n `196` status `ready` deltaP `-8.5802` edge `-0.0332` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2879` n `196` status `ready` deltaP `-6.9748` edge `-0.047` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-7.3416` n `185` status `ready` deltaP `8.4769` edge `0.2014` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4845` n `185` status `ready` deltaP `-5.7742` edge `-0.1833` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
