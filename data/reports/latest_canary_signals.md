# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T11:52:26.730420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `-0.0882` n `228`; crypto_major avg `-0.1855` n `8`; equity avg `-0.0719` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0071` n `23`; metal avg `0.0417` n `20`; unknown avg `-0.1717` n `765`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `0.022` n `228`; crypto_major avg `-0.141` n `8`; equity avg `-0.037` n `88`; fx avg `-0.0158` n `6`; index avg `0.0201` n `23`; metal avg `0.458` n `20`; unknown avg `0.1184` n `765`
- 4h: commodity avg `-0.1504` n `12`; crypto_alt avg `0.3229` n `228`; crypto_major avg `-0.6744` n `8`; equity avg `0.1873` n `88`; fx avg `0.0181` n `6`; index avg `0.057` n `23`; metal avg `0.585` n `20`; unknown avg `0.165` n `765`
- 24h: commodity avg `-0.4973` n `12`; crypto_alt avg `0.2992` n `228`; crypto_major avg `-1.0589` n `8`; equity avg `0.4314` n `88`; fx avg `0.1356` n `6`; index avg `-0.0198` n `23`; metal avg `-0.3531` n `20`; unknown avg `-0.0789` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
