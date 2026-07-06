# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T04:52:25.533870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `0.1356` n `229`; crypto_major avg `0.1675` n `8`; equity avg `0.0143` n `88`; fx avg `0.0027` n `6`; index avg `0.0086` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.2637` n `765`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `-0.0231` n `229`; crypto_major avg `0.2452` n `8`; equity avg `0.2694` n `88`; fx avg `-0.0191` n `6`; index avg `0.0983` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.4897` n `765`
- 4h: commodity avg `0.0275` n `12`; crypto_alt avg `-0.5172` n `229`; crypto_major avg `-0.6466` n `8`; equity avg `-0.7155` n `88`; fx avg `0.019` n `6`; index avg `-0.1869` n `25`; metal avg `-0.3356` n `20`; unknown avg `-0.3243` n `763`
- 24h: commodity avg `-0.22` n `12`; crypto_alt avg `0.3876` n `229`; crypto_major avg `1.3693` n `8`; equity avg `-0.6481` n `88`; fx avg `0.0571` n `6`; index avg `-0.0217` n `25`; metal avg `-0.2441` n `20`; unknown avg `1.0125` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
