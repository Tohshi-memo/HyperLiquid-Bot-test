# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T00:37:30.710248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.035` n `12`; crypto_alt avg `-0.3878` n `230`; crypto_major avg `-0.4486` n `8`; equity avg `0.0173` n `121`; fx avg `-0.0098` n `6`; index avg `0.0009` n `25`; metal avg `-0.0371` n `20`; unknown avg `0.1585` n `793`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.0985` n `230`; crypto_major avg `0.0038` n `8`; equity avg `0.2369` n `121`; fx avg `-0.0971` n `6`; index avg `0.0437` n `25`; metal avg `-0.0548` n `20`; unknown avg `-0.025` n `793`
- 4h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.7972` n `230`; crypto_major avg `0.5821` n `8`; equity avg `0.2892` n `121`; fx avg `-0.0868` n `6`; index avg `0.0294` n `25`; metal avg `0.0209` n `20`; unknown avg `-0.2699` n `792`
- 24h: commodity avg `0.2942` n `12`; crypto_alt avg `4.1755` n `230`; crypto_major avg `5.109` n `8`; equity avg `-1.0079` n `121`; fx avg `0.1038` n `6`; index avg `-0.1401` n `25`; metal avg `0.1218` n `20`; unknown avg `2.5095` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
