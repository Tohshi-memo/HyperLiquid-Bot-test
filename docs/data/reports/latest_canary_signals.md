# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T01:22:25.221160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `13`; crypto_alt avg `-0.4876` n `239`; crypto_major avg `-0.4595` n `8`; equity avg `-0.6989` n `162`; fx avg `0.0253` n `6`; index avg `-0.0804` n `27`; metal avg `-0.1996` n `20`; unknown avg `0.3846` n `1261`
- 1h: commodity avg `-0.1039` n `13`; crypto_alt avg `-0.8829` n `239`; crypto_major avg `-0.8339` n `8`; equity avg `-1.1851` n `162`; fx avg `0.0121` n `6`; index avg `-0.1686` n `27`; metal avg `-0.2785` n `20`; unknown avg `0.6396` n `1253`
- 4h: commodity avg `-0.2852` n `13`; crypto_alt avg `-0.3092` n `239`; crypto_major avg `-0.4234` n `8`; equity avg `-0.2522` n `162`; fx avg `-0.0221` n `6`; index avg `-0.0205` n `27`; metal avg `0.0559` n `20`; unknown avg `0.0758` n `1193`
- 24h: commodity avg `-0.3184` n `13`; crypto_alt avg `2.2599` n `239`; crypto_major avg `3.9469` n `8`; equity avg `1.1079` n `162`; fx avg `0.0119` n `6`; index avg `0.0926` n `27`; metal avg `0.4139` n `20`; unknown avg `1.7441` n `1128`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
