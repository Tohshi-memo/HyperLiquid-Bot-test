# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T03:37:30.140686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `-0.0646` n `8`; equity avg `0.0721` n `120`; fx avg `0.0107` n `6`; index avg `0.0223` n `25`; metal avg `0.0444` n `20`; unknown avg `0.0081` n `789`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.1752` n `230`; crypto_major avg `0.0332` n `8`; equity avg `0.0357` n `120`; fx avg `-0.0283` n `6`; index avg `0.0202` n `25`; metal avg `0.0465` n `20`; unknown avg `-0.267` n `789`
- 4h: commodity avg `0.0146` n `12`; crypto_alt avg `0.058` n `230`; crypto_major avg `-0.3431` n `8`; equity avg `0.4871` n `120`; fx avg `-0.1477` n `6`; index avg `-0.0301` n `25`; metal avg `0.1823` n `20`; unknown avg `0.157` n `789`
- 24h: commodity avg `0.3156` n `12`; crypto_alt avg `0.8143` n `230`; crypto_major avg `0.3745` n `8`; equity avg `-2.7457` n `120`; fx avg `-0.1357` n `6`; index avg `-0.4595` n `25`; metal avg `-0.5073` n `20`; unknown avg `-0.1386` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
