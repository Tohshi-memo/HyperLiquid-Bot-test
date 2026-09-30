# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T08:22:30.648178+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7468`

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

- `news_risk_high->unknown_24h` score `866.1244` n `135` status `ready` deltaP `1.9097` edge `72.1643` maxDD `0.0`
- `market_context_high->unknown_1h` score `589.2452` n `39` status `ready` deltaP `9.7305` edge `49.0389` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.9389` n `135` status `ready` deltaP `28.5532` edge `1.3255` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.8968` n `135` status `ready` deltaP `27.338` edge `0.7107` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.5429` n `135` status `ready` deltaP `23.9931` edge `0.784` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.7191` n `135` status `ready` deltaP `33.5301` edge `0.1342` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.3453` n `135` status `ready` deltaP `25.706` edge `0.2348` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.8492` n `135` status `ready` deltaP `29.0187` edge `0.2041` maxDD `-9.143`
- `market_context_high->crypto_alt_1h` score `1.775` n `39` status `ready` deltaP `10.79` edge `0.1423` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `1.7673` n `135` status `ready` deltaP `10.6549` edge `0.3422` maxDD `-15.9436`
- `market_context_high->crypto_major_1h` score `1.6235` n `39` status `ready` deltaP `10.0031` edge `0.1296` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.0766` n `135` status `ready` deltaP `9.2515` edge `0.1191` maxDD `-4.2849`
- `market_context_high->equity_1h` score `1.0724` n `39` status `ready` deltaP `15.7685` edge `0.0749` maxDD `-2.4027`
- `news_risk_high->equity_1h` score `0.8744` n `135` status `ready` deltaP `9.1018` edge `0.0745` maxDD `-1.6514`
- `market_context_high->metal_1h` score `0.5203` n `39` status `ready` deltaP `9.554` edge `0.0251` maxDD `-0.4338`
- `news_risk_high->index_1h` score `0.479` n `135` status `ready` deltaP `8.6682` edge `0.0109` maxDD `-0.302`
- `market_context_high->fx_1h` score `0.4185` n `39` status `ready` deltaP `11.2007` edge `0.0054` maxDD `-0.113`
- `market_context_high->index_1h` score `0.3232` n `39` status `ready` deltaP `6.56` edge `0.0169` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.1892` n `135` status `ready` deltaP `6.3392` edge `0.0273` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.6192` n `135` status `ready` deltaP `-0.1896` edge `0.0126` maxDD `-0.7016`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
