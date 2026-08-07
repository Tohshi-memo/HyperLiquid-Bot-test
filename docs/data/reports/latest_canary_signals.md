# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T15:37:27.738793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.033` n `12`; crypto_alt avg `0.1213` n `230`; crypto_major avg `0.0928` n `8`; equity avg `0.3603` n `112`; fx avg `-0.0216` n `6`; index avg `0.0304` n `25`; metal avg `-0.0506` n `20`; unknown avg `0.0461` n `782`
- 1h: commodity avg `0.0892` n `12`; crypto_alt avg `-0.0142` n `230`; crypto_major avg `-0.2894` n `8`; equity avg `0.691` n `112`; fx avg `-0.0084` n `6`; index avg `0.0941` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0174` n `782`
- 4h: commodity avg `0.4123` n `12`; crypto_alt avg `-0.237` n `230`; crypto_major avg `-0.1219` n `8`; equity avg `0.4785` n `112`; fx avg `-0.0408` n `6`; index avg `0.0443` n `25`; metal avg `-0.0566` n `20`; unknown avg `-0.0133` n `782`
- 24h: commodity avg `0.3428` n `12`; crypto_alt avg `-0.24` n `230`; crypto_major avg `-0.0023` n `8`; equity avg `0.9322` n `112`; fx avg `-0.1278` n `6`; index avg `0.0096` n `25`; metal avg `0.3142` n `20`; unknown avg `0.0506` n `765`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
