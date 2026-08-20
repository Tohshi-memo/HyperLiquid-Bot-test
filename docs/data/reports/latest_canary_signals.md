# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T13:37:32.977899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.5345` n `230`; crypto_major avg `-0.8603` n `8`; equity avg `0.1739` n `121`; fx avg `-0.0024` n `6`; index avg `0.1121` n `25`; metal avg `0.0679` n `20`; unknown avg `0.297` n `792`
- 1h: commodity avg `-0.0917` n `12`; crypto_alt avg `-0.3186` n `230`; crypto_major avg `-0.2295` n `8`; equity avg `0.6847` n `121`; fx avg `-0.0356` n `6`; index avg `0.2053` n `25`; metal avg `0.2115` n `20`; unknown avg `0.2742` n `792`
- 4h: commodity avg `0.0283` n `12`; crypto_alt avg `-0.1971` n `230`; crypto_major avg `-0.4076` n `8`; equity avg `-0.7025` n `121`; fx avg `-0.0151` n `6`; index avg `-0.0353` n `25`; metal avg `0.0329` n `20`; unknown avg `0.7595` n `792`
- 24h: commodity avg `0.1607` n `12`; crypto_alt avg `6.7838` n `230`; crypto_major avg `11.3214` n `8`; equity avg `-0.085` n `121`; fx avg `0.1695` n `6`; index avg `-0.0387` n `25`; metal avg `0.3258` n `20`; unknown avg `2.6945` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
