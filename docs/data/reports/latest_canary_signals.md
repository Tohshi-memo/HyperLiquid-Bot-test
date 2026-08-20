# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T23:52:24.322575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.1047` n `230`; crypto_major avg `-0.1408` n `8`; equity avg `-0.0705` n `121`; fx avg `-0.0314` n `6`; index avg `-0.0274` n `25`; metal avg `0.0166` n `20`; unknown avg `-0.0369` n `793`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `0.2746` n `230`; crypto_major avg `0.3202` n `8`; equity avg `-0.1381` n `121`; fx avg `0.0013` n `6`; index avg `-0.0639` n `25`; metal avg `0.0241` n `20`; unknown avg `-0.2838` n `793`
- 4h: commodity avg `-0.0479` n `12`; crypto_alt avg `1.261` n `230`; crypto_major avg `0.9942` n `8`; equity avg `0.0841` n `121`; fx avg `-0.0281` n `6`; index avg `-0.0498` n `25`; metal avg `0.0369` n `20`; unknown avg `-0.3221` n `792`
- 24h: commodity avg `0.3432` n `12`; crypto_alt avg `4.9119` n `230`; crypto_major avg `5.7765` n `8`; equity avg `-1.2321` n `121`; fx avg `0.1693` n `6`; index avg `-0.1734` n `25`; metal avg `0.1904` n `20`; unknown avg `2.6671` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
