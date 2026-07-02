# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T22:22:30.976792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `-0.1806` n `229`; crypto_major avg `-0.1026` n `8`; equity avg `0.0009` n `88`; fx avg `-0.0035` n `6`; index avg `0.003` n `25`; metal avg `-0.0109` n `20`; unknown avg `-0.0461` n `765`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.2214` n `229`; crypto_major avg `-0.3694` n `8`; equity avg `0.0793` n `88`; fx avg `-0.0171` n `6`; index avg `0.0168` n `25`; metal avg `-0.0056` n `20`; unknown avg `3.2689` n `765`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.2914` n `229`; crypto_major avg `-0.7252` n `8`; equity avg `0.5722` n `88`; fx avg `0.0044` n `6`; index avg `0.162` n `25`; metal avg `0.1046` n `20`; unknown avg `3.6938` n `765`
- 24h: commodity avg `0.1199` n `12`; crypto_alt avg `0.709` n `228`; crypto_major avg `1.1763` n `8`; equity avg `-2.4275` n `88`; fx avg `-0.1362` n `6`; index avg `-0.4695` n `25`; metal avg `0.9407` n `20`; unknown avg `3.9599` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
