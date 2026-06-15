# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T17:37:44.847696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.1655` n `228`; crypto_major avg `0.0824` n `8`; equity avg `0.0837` n `77`; fx avg `0.0024` n `6`; index avg `0.0005` n `23`; metal avg `-0.0801` n `18`; unknown avg `0.1434` n `687`
- 1h: commodity avg `0.1064` n `12`; crypto_alt avg `-0.4345` n `228`; crypto_major avg `-0.4106` n `8`; equity avg `0.0124` n `77`; fx avg `-0.0086` n `6`; index avg `-0.046` n `23`; metal avg `-0.2419` n `18`; unknown avg `1.1858` n `687`
- 4h: commodity avg `0.3981` n `12`; crypto_alt avg `-0.3861` n `228`; crypto_major avg `0.559` n `8`; equity avg `0.9335` n `77`; fx avg `-0.0092` n `6`; index avg `0.2387` n `23`; metal avg `-0.9006` n `18`; unknown avg `1.8486` n `687`
- 24h: commodity avg `-0.6719` n `12`; crypto_alt avg `5.9306` n `228`; crypto_major avg `7.3245` n `8`; equity avg `3.155` n `76`; fx avg `0.0508` n `6`; index avg `1.3498` n `23`; metal avg `2.1146` n `18`; unknown avg `3.676` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
