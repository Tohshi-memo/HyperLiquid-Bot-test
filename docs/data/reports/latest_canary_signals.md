# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T22:52:24.524245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.1103` n `230`; crypto_major avg `-0.1007` n `8`; equity avg `-0.1159` n `120`; fx avg `0.0024` n `6`; index avg `-0.0231` n `25`; metal avg `0.0037` n `20`; unknown avg `1.0633` n `789`
- 1h: commodity avg `0.034` n `12`; crypto_alt avg `-0.0063` n `230`; crypto_major avg `-0.032` n `8`; equity avg `-0.1401` n `120`; fx avg `-0.0008` n `6`; index avg `-0.0289` n `25`; metal avg `-0.0519` n `20`; unknown avg `1.6139` n `789`
- 4h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.4249` n `230`; crypto_major avg `-0.2672` n `8`; equity avg `-0.4309` n `120`; fx avg `0.0025` n `6`; index avg `-0.0659` n `25`; metal avg `-0.1602` n `20`; unknown avg `-0.1331` n `789`
- 24h: commodity avg `0.288` n `12`; crypto_alt avg `-0.5559` n `230`; crypto_major avg `0.086` n `8`; equity avg `-4.732` n `120`; fx avg `-0.0534` n `6`; index avg `-0.7577` n `25`; metal avg `-0.8014` n `20`; unknown avg `-0.2304` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
