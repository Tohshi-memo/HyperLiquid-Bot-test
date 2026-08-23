# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T23:07:26.991828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.1894` n `231`; crypto_major avg `-0.1988` n `8`; equity avg `0.013` n `122`; fx avg `-0.0101` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0071` n `20`; unknown avg `1.2689` n `793`
- 1h: commodity avg `-0.0814` n `12`; crypto_alt avg `-0.1871` n `231`; crypto_major avg `-0.1204` n `8`; equity avg `0.0478` n `122`; fx avg `-0.0015` n `6`; index avg `0.0211` n `25`; metal avg `-0.0307` n `20`; unknown avg `0.0385` n `793`
- 4h: commodity avg `-0.1275` n `12`; crypto_alt avg `0.1079` n `231`; crypto_major avg `0.4893` n `8`; equity avg `0.0089` n `122`; fx avg `-0.0872` n `6`; index avg `-0.021` n `25`; metal avg `-0.051` n `20`; unknown avg `1.0825` n `793`
- 24h: commodity avg `-0.2692` n `12`; crypto_alt avg `3.3818` n `231`; crypto_major avg `1.617` n `8`; equity avg `0.744` n `122`; fx avg `-0.1115` n `6`; index avg `0.1058` n `25`; metal avg `0.0496` n `20`; unknown avg `5.9147` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
