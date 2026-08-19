# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T10:37:27.425844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0764` n `12`; crypto_alt avg `0.0785` n `230`; crypto_major avg `-0.0031` n `8`; equity avg `0.1669` n `120`; fx avg `0.0024` n `6`; index avg `0.0231` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0397` n `791`
- 1h: commodity avg `0.0858` n `12`; crypto_alt avg `0.0553` n `230`; crypto_major avg `-0.023` n `8`; equity avg `-0.3313` n `120`; fx avg `-0.042` n `6`; index avg `-0.0318` n `25`; metal avg `0.0708` n `20`; unknown avg `-0.0599` n `791`
- 4h: commodity avg `0.1222` n `12`; crypto_alt avg `0.124` n `230`; crypto_major avg `0.2044` n `8`; equity avg `0.9598` n `120`; fx avg `-0.0714` n `6`; index avg `0.1864` n `25`; metal avg `0.1085` n `20`; unknown avg `-0.0978` n `789`
- 24h: commodity avg `0.5389` n `12`; crypto_alt avg `0.2177` n `230`; crypto_major avg `0.253` n `8`; equity avg `-1.6973` n `120`; fx avg `-0.2153` n `6`; index avg `-0.1855` n `25`; metal avg `-0.4468` n `20`; unknown avg `-0.3909` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
