# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T18:07:24.557994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `12`; crypto_alt avg `0.1301` n `230`; crypto_major avg `0.2329` n `8`; equity avg `0.049` n `112`; fx avg `-0.0012` n `6`; index avg `0.0056` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0039` n `782`
- 1h: commodity avg `0.0834` n `12`; crypto_alt avg `0.0655` n `230`; crypto_major avg `0.1024` n `8`; equity avg `0.0457` n `112`; fx avg `0.0017` n `6`; index avg `-0.0059` n `25`; metal avg `0.0543` n `20`; unknown avg `-0.1462` n `782`
- 4h: commodity avg `0.1007` n `12`; crypto_alt avg `-0.2374` n `230`; crypto_major avg `-0.614` n `8`; equity avg `0.5959` n `112`; fx avg `-0.0168` n `6`; index avg `0.0264` n `25`; metal avg `0.0401` n `20`; unknown avg `-0.1362` n `782`
- 24h: commodity avg `0.4224` n `12`; crypto_alt avg `-0.494` n `230`; crypto_major avg `-0.6389` n `8`; equity avg `0.6058` n `112`; fx avg `-0.1417` n `6`; index avg `-0.04` n `25`; metal avg `0.3` n `20`; unknown avg `-0.1126` n `765`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.2361`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
