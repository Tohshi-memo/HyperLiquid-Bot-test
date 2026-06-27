# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T06:07:26.329356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `12`; crypto_alt avg `-0.1377` n `228`; crypto_major avg `-0.2038` n `8`; equity avg `-0.0427` n `88`; fx avg `0.0043` n `6`; index avg `-0.0056` n `23`; metal avg `0.0012` n `20`; unknown avg `-0.1173` n `748`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.0948` n `228`; crypto_major avg `-0.0778` n `8`; equity avg `-0.0455` n `88`; fx avg `0.0052` n `6`; index avg `-0.0101` n `23`; metal avg `0.0023` n `20`; unknown avg `-0.1115` n `732`
- 4h: commodity avg `0.0833` n `12`; crypto_alt avg `0.0861` n `228`; crypto_major avg `0.1303` n `8`; equity avg `0.0273` n `88`; fx avg `0.0114` n `6`; index avg `-0.0148` n `23`; metal avg `-0.0016` n `20`; unknown avg `-0.5752` n `732`
- 24h: commodity avg `-0.2646` n `12`; crypto_alt avg `2.297` n `228`; crypto_major avg `1.8647` n `8`; equity avg `1.8673` n `87`; fx avg `-0.0002` n `6`; index avg `0.1405` n `23`; metal avg `1.1702` n `20`; unknown avg `-0.2901` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
