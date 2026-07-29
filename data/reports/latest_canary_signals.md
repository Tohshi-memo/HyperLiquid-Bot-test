# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T08:07:24.239980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `0.1293` n `230`; crypto_major avg `0.0156` n `8`; equity avg `-0.0633` n `102`; fx avg `0.0139` n `6`; index avg `0.0109` n `25`; metal avg `-0.0211` n `20`; unknown avg `-0.2482` n `777`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.1143` n `230`; crypto_major avg `-0.0068` n `8`; equity avg `0.0424` n `102`; fx avg `0.0275` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0304` n `20`; unknown avg `-0.0063` n `777`
- 4h: commodity avg `-0.1532` n `12`; crypto_alt avg `1.0872` n `230`; crypto_major avg `1.2941` n `8`; equity avg `1.8834` n `102`; fx avg `-0.0147` n `6`; index avg `0.4786` n `25`; metal avg `0.2351` n `20`; unknown avg `0.0198` n `761`
- 24h: commodity avg `0.0272` n `12`; crypto_alt avg `-1.1715` n `230`; crypto_major avg `1.1484` n `8`; equity avg `-1.194` n `102`; fx avg `-0.0966` n `6`; index avg `-0.1018` n `25`; metal avg `-0.0459` n `20`; unknown avg `-0.3172` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
