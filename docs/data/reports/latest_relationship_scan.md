# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T00:37:32.734287+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.8926` n `72` status `ready` deltaP `7.08` edge `0.1578` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.32` n `72` status `ready` deltaP `10.4844` edge `0.0189` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.171` n `72` status `ready` deltaP `6.7708` edge `0.1436` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0445` n `72` status `ready` deltaP `7.1607` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0155` n `72` status `ready` deltaP `0.7901` edge `0.0477` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0619` n `72` status `ready` deltaP `5.0474` edge `0.003` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.2013` n `72` status `ready` deltaP `-2.7778` edge `0.046` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.29` n `72` status `ready` deltaP `-0.0249` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4569` n `72` status `ready` deltaP `-2.4368` edge `-0.0066` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.3274` n `72` status `ready` deltaP `-5.9451` edge `-0.04` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-2.0296` n `72` status `ready` deltaP `-7.0276` edge `-0.0284` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.455` n `72` status `ready` deltaP `-5.0399` edge `-0.0482` maxDD `-5.8225`
- `news_risk_high->commodity_1h` score `-2.6022` n `72` status `ready` deltaP `-16.7748` edge `-0.0067` maxDD `-1.5323`
- `news_risk_high->crypto_major_4h` score `-2.8304` n `72` status `ready` deltaP `-7.7574` edge `-0.0174` maxDD `-9.0069`
- `news_risk_high->crypto_alt_4h` score `-3.0751` n `72` status `ready` deltaP `-9.5867` edge `-0.0683` maxDD `-13.9624`
- `news_risk_high->equity_24h` score `-3.3122` n `72` status `ready` deltaP `22.0487` edge `0.587` maxDD `-86.0244`
- `news_risk_high->metal_24h` score `-3.3562` n `72` status `ready` deltaP `-0.5208` edge `-0.2372` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.2389` n `72` status `ready` deltaP `-28.2521` edge `-0.0051` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-9.822` n `72` status `ready` deltaP `-26.5625` edge `-0.0735` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.2701` n `72` status `ready` deltaP `-29.6875` edge `-0.0576` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
