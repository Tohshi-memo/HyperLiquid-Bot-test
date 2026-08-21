# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T01:37:29.462884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.2444` n `230`; crypto_major avg `0.6351` n `8`; equity avg `0.0921` n `121`; fx avg `-0.0301` n `6`; index avg `0.0021` n `25`; metal avg `0.0486` n `20`; unknown avg `0.0066` n `793`
- 1h: commodity avg `0.0736` n `12`; crypto_alt avg `0.2973` n `230`; crypto_major avg `1.1121` n `8`; equity avg `0.1625` n `121`; fx avg `-0.0443` n `6`; index avg `0.0307` n `25`; metal avg `0.2066` n `20`; unknown avg `-0.0572` n `793`
- 4h: commodity avg `0.0919` n `12`; crypto_alt avg `0.7696` n `230`; crypto_major avg `1.2478` n `8`; equity avg `0.3141` n `121`; fx avg `-0.1169` n `6`; index avg `0.0561` n `25`; metal avg `0.2189` n `20`; unknown avg `-0.2528` n `793`
- 24h: commodity avg `0.343` n `12`; crypto_alt avg `4.7618` n `230`; crypto_major avg `6.8165` n `8`; equity avg `-0.8204` n `121`; fx avg `-0.0298` n `6`; index avg `-0.1467` n `25`; metal avg `0.4926` n `20`; unknown avg `2.6054` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
