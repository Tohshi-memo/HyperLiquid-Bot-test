# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T18:37:26.303798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `-0.1851` n `229`; crypto_major avg `-0.3838` n `8`; equity avg `-0.0147` n `91`; fx avg `-0.0067` n `6`; index avg `-0.0302` n `25`; metal avg `0.0215` n `20`; unknown avg `-0.1109` n `764`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.5105` n `229`; crypto_major avg `-0.7121` n `8`; equity avg `-0.0433` n `91`; fx avg `-0.0192` n `6`; index avg `-0.0563` n `25`; metal avg `0.045` n `20`; unknown avg `-0.1437` n `764`
- 4h: commodity avg `-0.5155` n `12`; crypto_alt avg `-0.0191` n `229`; crypto_major avg `-0.0136` n `8`; equity avg `0.1266` n `91`; fx avg `0.0026` n `6`; index avg `0.13` n `25`; metal avg `0.2133` n `20`; unknown avg `-0.1917` n `764`
- 24h: commodity avg `0.6914` n `12`; crypto_alt avg `-3.2986` n `229`; crypto_major avg `-3.8623` n `8`; equity avg `0.1544` n `91`; fx avg `0.0148` n `6`; index avg `-0.181` n `25`; metal avg `-1.1519` n `20`; unknown avg `-0.596` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
