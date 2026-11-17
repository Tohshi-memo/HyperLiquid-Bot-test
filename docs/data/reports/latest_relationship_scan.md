# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T20:52:46.775516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4041`

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

- `market_context_high->unknown_24h` score `1490.859` n `98` status `ready` deltaP `3.4722` edge `124.2151` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.4992` n `34` status `ready` deltaP `65.8598` edge `4.0065` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.5288` n `34` status `ready` deltaP `55.6402` edge `1.3398` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.4652` n `98` status `ready` deltaP `46.5384` edge `1.9995` maxDD `-22.8301`
- `news_risk_high->crypto_major_24h` score `15.2316` n `34` status `ready` deltaP `27.931` edge `1.8809` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `14.6198` n `98` status `ready` deltaP `32.7735` edge `1.8682` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.655` n `34` status `ready` deltaP `57.1793` edge `0.3704` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.5809` n `34` status `ready` deltaP `54.8611` edge `0.266` maxDD `0.0`
- `news_risk_high->metal_4h` score `6.9297` n `34` status `ready` deltaP `55.7478` edge `0.2103` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `6.2138` n `34` status `ready` deltaP `29.1652` edge `0.3452` maxDD `-0.4122`
- `news_risk_high->crypto_major_4h` score `5.3111` n `34` status `ready` deltaP `22.6327` edge `0.3344` maxDD `-1.7491`
- `news_risk_high->crypto_alt_4h` score `5.0412` n `34` status `ready` deltaP `31.6087` edge `0.5123` maxDD `-4.137`
- `news_risk_high->crypto_alt_24h` score `4.8318` n `34` status `ready` deltaP `7.8635` edge `1.0176` maxDD `-29.0448`
- `news_risk_high->index_4h` score `4.3227` n `34` status `ready` deltaP `36.3612` edge `0.1403` maxDD `-0.1319`
- `news_risk_high->crypto_alt_1h` score `3.189` n `34` status `ready` deltaP `23.2828` edge `0.1632` maxDD `-2.5469`
- `news_risk_high->crypto_major_1h` score `2.8678` n `34` status `ready` deltaP `19.2938` edge `0.1455` maxDD `-1.4777`
- `news_risk_high->metal_1h` score `2.7465` n `34` status `ready` deltaP `29.1652` edge `0.0562` maxDD `-0.0743`
- `news_risk_high->index_1h` score `2.0381` n `34` status `ready` deltaP `23.7319` edge `0.0334` maxDD `-0.0751`
- `news_risk_high->commodity_4h` score `1.5389` n `34` status `ready` deltaP `26.1209` edge `0.0485` maxDD `-0.3611`
- `news_risk_high->commodity_1h` score `-0.4442` n `34` status `ready` deltaP `-3.1878` edge `0.0177` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
