# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T00:37:26.281260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `0.287` n `232`; crypto_major avg `0.232` n `8`; equity avg `0.0299` n `134`; fx avg `-0.0109` n `6`; index avg `0.0007` n `26`; metal avg `0.0003` n `20`; unknown avg `120.5955` n `791`
- 1h: commodity avg `-0.0723` n `12`; crypto_alt avg `0.4823` n `232`; crypto_major avg `0.2349` n `8`; equity avg `0.2953` n `134`; fx avg `-0.0823` n `6`; index avg `0.0731` n `26`; metal avg `0.0681` n `20`; unknown avg `5.3168` n `789`
- 4h: commodity avg `-0.0425` n `12`; crypto_alt avg `0.1248` n `232`; crypto_major avg `0.0078` n `8`; equity avg `0.1862` n `134`; fx avg `-0.1174` n `6`; index avg `0.0174` n `26`; metal avg `0.1223` n `20`; unknown avg `5.1212` n `780`
- 24h: commodity avg `0.1869` n `12`; crypto_alt avg `-0.2651` n `232`; crypto_major avg `-1.2784` n `8`; equity avg `0.5211` n `134`; fx avg `-0.1596` n `6`; index avg `0.1111` n `26`; metal avg `0.2271` n `20`; unknown avg `7765.1235` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
