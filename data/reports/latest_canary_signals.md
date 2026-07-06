# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T11:52:30.654107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0549` n `12`; crypto_alt avg `-0.0251` n `229`; crypto_major avg `0.032` n `8`; equity avg `0.0695` n `88`; fx avg `0.0049` n `6`; index avg `0.0093` n `25`; metal avg `-0.0371` n `20`; unknown avg `-0.0452` n `765`
- 1h: commodity avg `0.0764` n `12`; crypto_alt avg `-0.0488` n `229`; crypto_major avg `0.1322` n `8`; equity avg `0.053` n `88`; fx avg `0.0109` n `6`; index avg `0.016` n `25`; metal avg `-0.0443` n `20`; unknown avg `-0.1117` n `765`
- 4h: commodity avg `0.1934` n `12`; crypto_alt avg `0.0288` n `229`; crypto_major avg `-0.0868` n `8`; equity avg `-0.0188` n `88`; fx avg `0.0042` n `6`; index avg `0.0017` n `25`; metal avg `-0.1467` n `20`; unknown avg `-0.1791` n `765`
- 24h: commodity avg `-0.1138` n `12`; crypto_alt avg `0.443` n `229`; crypto_major avg `0.9242` n `8`; equity avg `-0.6676` n `88`; fx avg `0.0811` n `6`; index avg `0.0035` n `25`; metal avg `-0.2025` n `20`; unknown avg `0.9277` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
