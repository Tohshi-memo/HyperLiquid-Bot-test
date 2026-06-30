# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T10:22:30.875902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0059` n `228`; crypto_major avg `-0.0627` n `8`; equity avg `0.0245` n `88`; fx avg `0.001` n `6`; index avg `-0.0062` n `23`; metal avg `0.022` n `20`; unknown avg `0.3713` n `765`
- 1h: commodity avg `0.0845` n `12`; crypto_alt avg `0.0567` n `228`; crypto_major avg `0.0919` n `8`; equity avg `0.0627` n `88`; fx avg `0.0089` n `6`; index avg `-0.0073` n `23`; metal avg `0.12` n `20`; unknown avg `0.3532` n `765`
- 4h: commodity avg `0.383` n `12`; crypto_alt avg `-0.5216` n `228`; crypto_major avg `-0.2428` n `8`; equity avg `-0.165` n `88`; fx avg `0.023` n `6`; index avg `-0.0619` n `23`; metal avg `0.4072` n `20`; unknown avg `0.248` n `765`
- 24h: commodity avg `0.1794` n `12`; crypto_alt avg `-1.0212` n `228`; crypto_major avg `-0.0726` n `8`; equity avg `1.3427` n `88`; fx avg `0.1342` n `6`; index avg `0.1115` n `23`; metal avg `0.2739` n `20`; unknown avg `9.4955` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
