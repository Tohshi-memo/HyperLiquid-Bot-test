# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T12:52:30.756338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2320.445` n `112` status `ready` deltaP `-7.3661` edge `193.4625` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `93.8598` n `98` status `ready` deltaP `-5.7924` edge `7.8889` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `63.6821` n `112` status `ready` deltaP `1.2195` edge `5.312` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.2865` n `45` status `ready` deltaP `45.7292` edge `1.1408` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7369` n `112` status `ready` deltaP `27.1578` edge `0.9894` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.7702` n `98` status `ready` deltaP `17.7234` edge `0.418` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.6592` n `112` status `ready` deltaP `42.2371` edge `0.125` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.0336` n `112` status `ready` deltaP `20.3397` edge `0.0394` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8277` n `98` status `ready` deltaP `7.4972` edge `0.1019` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5971` n `112` status `ready` deltaP `13.4035` edge `0.0162` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.5963` n `112` status `ready` deltaP `5.4878` edge `0.1792` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `0.2852` n `112` status `ready` deltaP `8.1801` edge `0.072` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.2651` n `112` status `ready` deltaP `5.0631` edge `0.0878` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.0697` n `112` status `ready` deltaP `5.4962` edge `-0.0008` maxDD `-0.1525`
- `market_context_high->metal_24h` score `0.0658` n `112` status `ready` deltaP `12.5744` edge `0.1893` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `-0.0694` n `112` status `ready` deltaP `9.3423` edge `0.0507` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1647` n `112` status `ready` deltaP `4.1159` edge `-0.0011` maxDD `-0.2054`
- `market_context_high->crypto_major_4h` score `-0.4725` n `112` status `ready` deltaP `14.9608` edge `0.1349` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.4766` n `112` status `ready` deltaP `2.2241` edge `0.0013` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.5536` n `112` status `ready` deltaP `-1.1709` edge `0.0131` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
