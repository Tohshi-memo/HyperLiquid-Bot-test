# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T17:52:29.069267+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11590`

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

- `market_context_high->equity_24h` score `2.9748` n `103` status `ready` deltaP `4.5729` edge `0.5234` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3635` n `103` status `ready` deltaP `12.0382` edge `0.1743` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4824` n `103` status `ready` deltaP `14.1339` edge `0.0966` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.1023` n `106` status `ready` deltaP `12.7584` edge `0.0411` maxDD `-0.7439`
- `market_context_high->fx_24h` score `1.0292` n `103` status `ready` deltaP `24.5263` edge `0.0551` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3964` n `103` status `ready` deltaP `9.1002` edge `0.1433` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.5072` n `106` status `ready` deltaP `3.0731` edge `0.0201` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.531` n `106` status `ready` deltaP `-3.3527` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5552` n `106` status `ready` deltaP `1.3925` edge `-0.006` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6367` n `106` status `ready` deltaP `-3.9063` edge `-0.006` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6897` n `103` status `ready` deltaP `-2.4909` edge `-0.0113` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8295` n `103` status `ready` deltaP `1.7848` edge `-0.0057` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8743` n `106` status `ready` deltaP `-10.061` edge `-0.0262` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.1246` n `103` status `ready` deltaP `0.9117` edge `-0.0494` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.3695` n `106` status `ready` deltaP `-6.9173` edge `-0.0517` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-3.2308` n `103` status `ready` deltaP `6.9141` edge `-0.0659` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.7294` n `103` status `ready` deltaP `-12.4461` edge `-0.0835` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.4132` n `103` status `ready` deltaP `-11.9509` edge `-0.1229` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0521` n `103` status `ready` deltaP `-14.7111` edge `-0.2338` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
