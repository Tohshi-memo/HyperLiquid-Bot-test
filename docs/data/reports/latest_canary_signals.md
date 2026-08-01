# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T10:52:32.117109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0132` n `230`; crypto_major avg `0.0309` n `8`; equity avg `0.0216` n `102`; fx avg `-0.0328` n `6`; index avg `0.0127` n `25`; metal avg `-0.007` n `20`; unknown avg `0.0142` n `781`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `-0.1296` n `230`; crypto_major avg `-0.0929` n `8`; equity avg `0.0086` n `102`; fx avg `-0.0371` n `6`; index avg `0.0062` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.002` n `781`
- 4h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.4457` n `230`; crypto_major avg `-0.3171` n `8`; equity avg `-0.0425` n `102`; fx avg `-0.0295` n `6`; index avg `0.0277` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.092` n `781`
- 24h: commodity avg `0.525` n `12`; crypto_alt avg `0.0824` n `230`; crypto_major avg `-1.3291` n `8`; equity avg `-2.6557` n `102`; fx avg `-0.0997` n `6`; index avg `-0.2684` n `25`; metal avg `-0.0705` n `20`; unknown avg `4.5807` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
