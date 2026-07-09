# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T17:22:25.757013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `0.112` n `229`; crypto_major avg `0.0875` n `8`; equity avg `0.1716` n `91`; fx avg `0.0084` n `6`; index avg `0.0413` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.008` n `765`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `0.2167` n `229`; crypto_major avg `0.2547` n `8`; equity avg `0.1796` n `91`; fx avg `0.0152` n `6`; index avg `0.0524` n `25`; metal avg `-0.1156` n `20`; unknown avg `-0.0563` n `765`
- 4h: commodity avg `-0.6822` n `12`; crypto_alt avg `-0.0099` n `229`; crypto_major avg `0.0709` n `8`; equity avg `0.6813` n `91`; fx avg `-0.0` n `6`; index avg `0.1697` n `25`; metal avg `0.1091` n `20`; unknown avg `0.0416` n `765`
- 24h: commodity avg `-1.0818` n `12`; crypto_alt avg `0.7344` n `229`; crypto_major avg `0.2631` n `8`; equity avg `2.7027` n `91`; fx avg `0.0542` n `6`; index avg `0.41` n `25`; metal avg `0.9317` n `20`; unknown avg `0.9295` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
