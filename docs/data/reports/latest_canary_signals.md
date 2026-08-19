# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T09:52:26.657375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0363` n `230`; crypto_major avg `-0.0496` n `8`; equity avg `-0.2912` n `120`; fx avg `-0.0482` n `6`; index avg `-0.039` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.017` n `791`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `-0.2701` n `230`; crypto_major avg `-0.2058` n `8`; equity avg `-0.6445` n `120`; fx avg `-0.056` n `6`; index avg `-0.0783` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.0282` n `789`
- 4h: commodity avg `0.0359` n `12`; crypto_alt avg `0.0572` n `230`; crypto_major avg `0.1746` n `8`; equity avg `0.7403` n `120`; fx avg `-0.0681` n `6`; index avg `0.1844` n `25`; metal avg `0.1242` n `20`; unknown avg `0.0242` n `757`
- 24h: commodity avg `0.4044` n `12`; crypto_alt avg `0.1443` n `230`; crypto_major avg `0.3423` n `8`; equity avg `-1.6165` n `120`; fx avg `-0.2163` n `6`; index avg `-0.1819` n `25`; metal avg `-0.4557` n `20`; unknown avg `-0.2191` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
