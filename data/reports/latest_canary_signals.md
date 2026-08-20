# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T14:37:32.320738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0396` n `12`; crypto_alt avg `-0.0158` n `230`; crypto_major avg `-0.1555` n `8`; equity avg `0.0023` n `121`; fx avg `-0.0069` n `6`; index avg `0.0109` n `25`; metal avg `0.0776` n `20`; unknown avg `0.0282` n `792`
- 1h: commodity avg `-0.1785` n `12`; crypto_alt avg `0.6084` n `230`; crypto_major avg `0.9554` n `8`; equity avg `-0.1058` n `121`; fx avg `0.009` n `6`; index avg `-0.0237` n `25`; metal avg `0.0667` n `20`; unknown avg `-0.1058` n `792`
- 4h: commodity avg `-0.1314` n `12`; crypto_alt avg `0.2253` n `230`; crypto_major avg `0.598` n `8`; equity avg `-0.8766` n `121`; fx avg `-0.0114` n `6`; index avg `-0.0992` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.1972` n `792`
- 24h: commodity avg `-0.0135` n `12`; crypto_alt avg `7.2044` n `230`; crypto_major avg `12.0445` n `8`; equity avg `-0.0189` n `121`; fx avg `0.1856` n `6`; index avg `-0.0185` n `25`; metal avg `0.2089` n `20`; unknown avg `2.5011` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
