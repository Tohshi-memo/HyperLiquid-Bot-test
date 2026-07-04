# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T19:37:29.481863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0121` n `229`; crypto_major avg `-0.1218` n `8`; equity avg `0.0024` n `88`; fx avg `-0.0399` n `6`; index avg `0.0043` n `25`; metal avg `0.0114` n `20`; unknown avg `0.1533` n `765`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.1321` n `229`; crypto_major avg `-0.2172` n `8`; equity avg `0.0706` n `88`; fx avg `-0.0384` n `6`; index avg `0.0064` n `25`; metal avg `0.0364` n `20`; unknown avg `-0.4832` n `765`
- 4h: commodity avg `-0.0446` n `12`; crypto_alt avg `0.1065` n `229`; crypto_major avg `-0.1367` n `8`; equity avg `0.0321` n `88`; fx avg `-0.0443` n `6`; index avg `-0.0189` n `25`; metal avg `0.046` n `20`; unknown avg `-0.6695` n `765`
- 24h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.9048` n `229`; crypto_major avg `1.0856` n `8`; equity avg `0.1757` n `88`; fx avg `-0.0537` n `6`; index avg `-0.0567` n `25`; metal avg `0.0859` n `20`; unknown avg `-0.1955` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
