# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T23:44:01.461995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `0.1113` n `229`; crypto_major avg `0.0671` n `8`; equity avg `0.0389` n `88`; fx avg `0.0112` n `6`; index avg `0.0147` n `25`; metal avg `0.01` n `20`; unknown avg `0.4391` n `765`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.2912` n `229`; crypto_major avg `0.2818` n `8`; equity avg `-0.0535` n `88`; fx avg `0.0094` n `6`; index avg `0.0334` n `25`; metal avg `0.0085` n `20`; unknown avg `0.3501` n `765`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `0.3376` n `229`; crypto_major avg `-0.0075` n `8`; equity avg `0.4466` n `88`; fx avg `0.0074` n `6`; index avg `0.1657` n `25`; metal avg `0.1628` n `20`; unknown avg `1.9449` n `765`
- 24h: commodity avg `0.1113` n `12`; crypto_alt avg `2.4059` n `228`; crypto_major avg `3.1374` n `8`; equity avg `-2.0783` n `88`; fx avg `-0.1372` n `6`; index avg `-0.3842` n `25`; metal avg `0.9685` n `20`; unknown avg `3.3602` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
