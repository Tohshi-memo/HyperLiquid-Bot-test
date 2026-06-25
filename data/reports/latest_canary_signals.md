# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T05:37:32.552802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.1349` n `228`; crypto_major avg `0.1306` n `8`; equity avg `-0.0021` n `86`; fx avg `-0.0351` n `6`; index avg `0.0329` n `23`; metal avg `-0.0541` n `20`; unknown avg `10.5634` n `765`
- 1h: commodity avg `-0.0241` n `12`; crypto_alt avg `1.382` n `228`; crypto_major avg `1.3335` n `8`; equity avg `0.3788` n `86`; fx avg `-0.0641` n `6`; index avg `0.0913` n `23`; metal avg `-0.064` n `20`; unknown avg `23.5686` n `765`
- 4h: commodity avg `0.03` n `12`; crypto_alt avg `1.1948` n `228`; crypto_major avg `1.0558` n `8`; equity avg `0.3407` n `86`; fx avg `-0.0483` n `6`; index avg `0.1265` n `23`; metal avg `0.1362` n `20`; unknown avg `0.9925` n `748`
- 24h: commodity avg `-0.4921` n `12`; crypto_alt avg `-1.1875` n `228`; crypto_major avg `-1.2884` n `8`; equity avg `-0.1532` n `86`; fx avg `-0.0187` n `6`; index avg `0.5429` n `23`; metal avg `-1.6237` n `20`; unknown avg `-0.4283` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
