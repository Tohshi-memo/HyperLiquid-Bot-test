# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T12:11:12.907591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `0.1416` n `230`; crypto_major avg `0.0692` n `8`; equity avg `-0.0335` n `102`; fx avg `0.0181` n `6`; index avg `-0.012` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.0098` n `781`
- 1h: commodity avg `0.0486` n `12`; crypto_alt avg `0.1874` n `230`; crypto_major avg `0.0662` n `8`; equity avg `0.0367` n `102`; fx avg `-0.0377` n `6`; index avg `-0.0358` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0064` n `781`
- 4h: commodity avg `0.058` n `12`; crypto_alt avg `0.0942` n `230`; crypto_major avg `-0.1324` n `8`; equity avg `-0.0804` n `102`; fx avg `-0.0619` n `6`; index avg `-0.0463` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.197` n `781`
- 24h: commodity avg `0.2726` n `12`; crypto_alt avg `0.6326` n `230`; crypto_major avg `-1.1916` n `8`; equity avg `-2.4626` n `102`; fx avg `-0.1588` n `6`; index avg `-0.2754` n `25`; metal avg `-0.0432` n `20`; unknown avg `4.6241` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
