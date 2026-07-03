# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T12:52:28.374343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.0447` n `229`; crypto_major avg `0.1081` n `8`; equity avg `-0.0165` n `88`; fx avg `0.0149` n `6`; index avg `0.0058` n `25`; metal avg `0.0543` n `20`; unknown avg `-0.0172` n `765`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.0119` n `229`; crypto_major avg `-0.2792` n `8`; equity avg `-0.0572` n `88`; fx avg `0.0051` n `6`; index avg `0.0085` n `25`; metal avg `-0.0237` n `20`; unknown avg `0.048` n `765`
- 4h: commodity avg `-0.1076` n `12`; crypto_alt avg `0.908` n `229`; crypto_major avg `0.8277` n `8`; equity avg `0.1787` n `88`; fx avg `0.0342` n `6`; index avg `0.0161` n `25`; metal avg `-0.0961` n `20`; unknown avg `1.0681` n `755`
- 24h: commodity avg `0.3739` n `12`; crypto_alt avg `1.7677` n `229`; crypto_major avg `1.7198` n `8`; equity avg `-0.947` n `88`; fx avg `-0.0937` n `6`; index avg `-0.0055` n `25`; metal avg `0.5333` n `20`; unknown avg `6.1852` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
