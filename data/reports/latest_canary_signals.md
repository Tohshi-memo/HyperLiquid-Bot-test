# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T06:37:27.940544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0799` n `232`; crypto_major avg `-0.1511` n `8`; equity avg `-0.0147` n `134`; fx avg `0.0211` n `6`; index avg `0.0235` n `26`; metal avg `0.0203` n `20`; unknown avg `0.3187` n `786`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.2458` n `232`; crypto_major avg `-0.3299` n `8`; equity avg `0.0385` n `134`; fx avg `-0.0288` n `6`; index avg `0.0374` n `26`; metal avg `-0.0344` n `20`; unknown avg `0.3129` n `764`
- 4h: commodity avg `0.1245` n `12`; crypto_alt avg `-0.1928` n `232`; crypto_major avg `-0.6285` n `8`; equity avg `0.091` n `134`; fx avg `-0.0297` n `6`; index avg `0.0294` n `26`; metal avg `-0.1013` n `20`; unknown avg `0.2895` n `730`
- 24h: commodity avg `0.0894` n `12`; crypto_alt avg `0.3975` n `232`; crypto_major avg `-0.5888` n `8`; equity avg `0.4247` n `134`; fx avg `-0.0314` n `6`; index avg `0.05` n `26`; metal avg `-0.1648` n `20`; unknown avg `382.886` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
