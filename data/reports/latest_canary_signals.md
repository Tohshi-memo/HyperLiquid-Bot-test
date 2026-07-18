# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T16:15:02.318025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `-0.0153` n `230`; crypto_major avg `0.1402` n `8`; equity avg `0.0257` n `96`; fx avg `-0.0007` n `6`; index avg `-0.0037` n `25`; metal avg `-0.002` n `20`; unknown avg `0.0015` n `770`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.124` n `230`; crypto_major avg `0.06` n `8`; equity avg `-0.0738` n `96`; fx avg `-0.0403` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0234` n `20`; unknown avg `-0.0598` n `770`
- 4h: commodity avg `0.0104` n `12`; crypto_alt avg `0.1175` n `230`; crypto_major avg `0.2911` n `8`; equity avg `-0.1265` n `96`; fx avg `-0.0444` n `6`; index avg `-0.0232` n `25`; metal avg `-0.0561` n `20`; unknown avg `-0.0722` n `770`
- 24h: commodity avg `0.3544` n `12`; crypto_alt avg `-0.7597` n `230`; crypto_major avg `0.3598` n `8`; equity avg `-0.8471` n `96`; fx avg `-0.0979` n `6`; index avg `-0.0414` n `25`; metal avg `-0.0331` n `20`; unknown avg `0.0682` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
