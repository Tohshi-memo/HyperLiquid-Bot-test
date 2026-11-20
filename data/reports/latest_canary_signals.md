# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T06:52:36.323104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `13`; crypto_alt avg `0.1215` n `239`; crypto_major avg `0.2104` n `8`; equity avg `-0.0231` n `165`; fx avg `-0.0016` n `6`; index avg `-0.0009` n `27`; metal avg `0.0511` n `20`; unknown avg `158.5991` n `1262`
- 1h: commodity avg `-0.0175` n `13`; crypto_alt avg `-0.0155` n `239`; crypto_major avg `0.0412` n `8`; equity avg `-0.1371` n `165`; fx avg `0.0082` n `6`; index avg `-0.0103` n `27`; metal avg `0.1741` n `20`; unknown avg `0.2229` n `1238`
- 4h: commodity avg `-0.1334` n `13`; crypto_alt avg `0.222` n `239`; crypto_major avg `0.5249` n `8`; equity avg `-0.3406` n `165`; fx avg `0.0103` n `6`; index avg `-0.0317` n `27`; metal avg `0.0518` n `20`; unknown avg `162.8977` n `1224`
- 24h: commodity avg `-0.114` n `13`; crypto_alt avg `-3.0005` n `239`; crypto_major avg `-2.4807` n `8`; equity avg `-6.6956` n `165`; fx avg `0.0435` n `6`; index avg `-0.6212` n `27`; metal avg `-1.476` n `20`; unknown avg `306.808` n `1171`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
