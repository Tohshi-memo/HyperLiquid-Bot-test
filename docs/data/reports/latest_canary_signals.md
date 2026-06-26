# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T16:22:32.183893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `-0.3057` n `228`; crypto_major avg `-0.4951` n `8`; equity avg `-0.2418` n `86`; fx avg `-0.0083` n `6`; index avg `-0.0408` n `23`; metal avg `-0.0359` n `20`; unknown avg `-0.0203` n `765`
- 1h: commodity avg `0.1898` n `12`; crypto_alt avg `0.4851` n `228`; crypto_major avg `0.2625` n `8`; equity avg `0.1813` n `86`; fx avg `-0.0084` n `6`; index avg `0.0436` n `23`; metal avg `0.0479` n `20`; unknown avg `0.0209` n `765`
- 4h: commodity avg `-0.1233` n `12`; crypto_alt avg `1.6012` n `228`; crypto_major avg `1.5745` n `8`; equity avg `1.26` n `86`; fx avg `-0.0369` n `6`; index avg `0.1445` n `23`; metal avg `0.408` n `20`; unknown avg `0.1599` n `765`
- 24h: commodity avg `-0.4101` n `12`; crypto_alt avg `1.3852` n `228`; crypto_major avg `1.7901` n `8`; equity avg `-0.9284` n `86`; fx avg `-0.0667` n `6`; index avg `-0.3091` n `23`; metal avg `0.4237` n `20`; unknown avg `0.1553` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
