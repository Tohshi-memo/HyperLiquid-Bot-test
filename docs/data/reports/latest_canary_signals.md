# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T05:07:30.282647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `-0.2591` n `228`; crypto_major avg `-0.267` n `8`; equity avg `-0.0277` n `88`; fx avg `0.0001` n `6`; index avg `-0.0159` n `23`; metal avg `-0.0112` n `20`; unknown avg `0.3965` n `764`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-0.1532` n `228`; crypto_major avg `-0.3077` n `8`; equity avg `-0.0479` n `88`; fx avg `0.007` n `6`; index avg `-0.0062` n `23`; metal avg `-0.0285` n `20`; unknown avg `0.0104` n `756`
- 4h: commodity avg `-0.1783` n `12`; crypto_alt avg `0.3135` n `228`; crypto_major avg `-0.0553` n `8`; equity avg `0.0451` n `88`; fx avg `-0.0077` n `6`; index avg `0.0076` n `23`; metal avg `0.0032` n `20`; unknown avg `15.7958` n `714`
- 24h: commodity avg `0.2604` n `12`; crypto_alt avg `-0.3418` n `228`; crypto_major avg `-1.2797` n `8`; equity avg `0.0304` n `88`; fx avg `-0.0096` n `6`; index avg `-0.1163` n `23`; metal avg `-0.0434` n `20`; unknown avg `16.403` n `666`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
