# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T09:37:28.936256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `0.07` n `228`; crypto_major avg `0.0458` n `8`; equity avg `0.0293` n `88`; fx avg `0.0383` n `6`; index avg `0.002` n `23`; metal avg `-0.0031` n `20`; unknown avg `-0.0093` n `764`
- 1h: commodity avg `0.0102` n `12`; crypto_alt avg `-0.1395` n `228`; crypto_major avg `-0.2307` n `8`; equity avg `-0.0016` n `88`; fx avg `0.005` n `6`; index avg `0.0016` n `23`; metal avg `-0.0171` n `20`; unknown avg `-0.2533` n `764`
- 4h: commodity avg `0.0407` n `12`; crypto_alt avg `-0.3168` n `228`; crypto_major avg `-0.156` n `8`; equity avg `0.2291` n `88`; fx avg `0.0114` n `6`; index avg `0.011` n `23`; metal avg `-0.0176` n `20`; unknown avg `-0.127` n `716`
- 24h: commodity avg `0.1321` n `12`; crypto_alt avg `0.7988` n `228`; crypto_major avg `0.7962` n `8`; equity avg `1.8209` n `87`; fx avg `0.0308` n `6`; index avg `0.08` n `23`; metal avg `0.3663` n `20`; unknown avg `-0.1358` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
