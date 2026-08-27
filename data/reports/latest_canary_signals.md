# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T12:07:27.275527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.086` n `231`; crypto_major avg `0.0884` n `8`; equity avg `0.093` n `127`; fx avg `0.0071` n `6`; index avg `0.0292` n `26`; metal avg `0.011` n `20`; unknown avg `0.0489` n `792`
- 1h: commodity avg `0.0946` n `12`; crypto_alt avg `-0.225` n `231`; crypto_major avg `-0.314` n `8`; equity avg `-0.2621` n `127`; fx avg `-0.0069` n `6`; index avg `-0.0129` n `26`; metal avg `0.031` n `20`; unknown avg `0.0052` n `792`
- 4h: commodity avg `0.2998` n `12`; crypto_alt avg `-0.124` n `231`; crypto_major avg `0.0484` n `8`; equity avg `-0.1734` n `127`; fx avg `-0.0022` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0619` n `20`; unknown avg `-0.0099` n `792`
- 24h: commodity avg `0.5228` n `12`; crypto_alt avg `1.3373` n `231`; crypto_major avg `2.0032` n `8`; equity avg `1.8438` n `127`; fx avg `-0.0972` n `6`; index avg `0.2985` n `26`; metal avg `-0.3589` n `20`; unknown avg `0.4838` n `775`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
