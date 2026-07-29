# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T00:07:31.780167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `0.2566` n `230`; crypto_major avg `0.2836` n `8`; equity avg `0.7226` n `102`; fx avg `0.033` n `6`; index avg `0.0805` n `25`; metal avg `0.0291` n `20`; unknown avg `-0.0249` n `777`
- 1h: commodity avg `-0.166` n `12`; crypto_alt avg `0.8344` n `230`; crypto_major avg `0.8127` n `8`; equity avg `2.2162` n `102`; fx avg `0.048` n `6`; index avg `0.3301` n `25`; metal avg `0.1069` n `20`; unknown avg `0.1777` n `776`
- 4h: commodity avg `0.6062` n `12`; crypto_alt avg `0.2399` n `230`; crypto_major avg `0.227` n `8`; equity avg `1.4973` n `102`; fx avg `0.0357` n `6`; index avg `0.2515` n `25`; metal avg `0.0481` n `20`; unknown avg `-0.0692` n `776`
- 24h: commodity avg `-0.2634` n `12`; crypto_alt avg `0.1796` n `230`; crypto_major avg `0.4756` n `8`; equity avg `-1.2505` n `102`; fx avg `-0.1166` n `6`; index avg `-0.0816` n `25`; metal avg `-0.2861` n `20`; unknown avg `0.4293` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
