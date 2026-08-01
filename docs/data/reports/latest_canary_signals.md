# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T12:07:30.806005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `0.1245` n `230`; crypto_major avg `0.0805` n `8`; equity avg `-0.0011` n `102`; fx avg `0.0293` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.0079` n `781`
- 1h: commodity avg `0.0348` n `12`; crypto_alt avg `0.1703` n `230`; crypto_major avg `0.0775` n `8`; equity avg `0.0692` n `102`; fx avg `-0.0265` n `6`; index avg `-0.0312` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.0059` n `781`
- 4h: commodity avg `0.0442` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `-0.1214` n `8`; equity avg `-0.048` n `102`; fx avg `-0.0507` n `6`; index avg `-0.0418` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.2009` n `781`
- 24h: commodity avg `0.2589` n `12`; crypto_alt avg `0.6153` n `230`; crypto_major avg `-1.1794` n `8`; equity avg `-2.432` n `102`; fx avg `-0.1478` n `6`; index avg `-0.271` n `25`; metal avg `-0.042` n `20`; unknown avg `4.6217` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
