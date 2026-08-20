# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T23:07:25.179066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.0291` n `230`; crypto_major avg `-0.0498` n `8`; equity avg `-0.0576` n `121`; fx avg `0.0239` n `6`; index avg `-0.0067` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.1562` n `793`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.1204` n `230`; crypto_major avg `0.0946` n `8`; equity avg `0.0626` n `121`; fx avg `0.0197` n `6`; index avg `0.0256` n `25`; metal avg `0.0776` n `20`; unknown avg `-0.2448` n `793`
- 4h: commodity avg `-0.0576` n `12`; crypto_alt avg `0.9431` n `230`; crypto_major avg `0.6297` n `8`; equity avg `0.3672` n `121`; fx avg `-0.0097` n `6`; index avg `0.0219` n `25`; metal avg `0.1163` n `20`; unknown avg `-0.3454` n `792`
- 24h: commodity avg `0.352` n `12`; crypto_alt avg `4.6438` n `230`; crypto_major avg `4.8675` n `8`; equity avg `-1.1732` n `121`; fx avg `0.1964` n `6`; index avg `-0.1435` n `25`; metal avg `0.1491` n `20`; unknown avg `2.5859` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
