# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T18:07:29.826254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0322` n `12`; crypto_alt avg `-0.1398` n `229`; crypto_major avg `-0.2323` n `8`; equity avg `-0.0375` n `88`; fx avg `-0.0129` n `6`; index avg `0.0017` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.3356` n `765`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `0.3937` n `229`; crypto_major avg `0.5399` n `8`; equity avg `0.07` n `88`; fx avg `-0.0051` n `6`; index avg `0.0208` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.2484` n `765`
- 4h: commodity avg `-0.005` n `12`; crypto_alt avg `1.0053` n `229`; crypto_major avg `0.9776` n `8`; equity avg `0.0574` n `88`; fx avg `0.0226` n `6`; index avg `-0.009` n `25`; metal avg `0.0268` n `20`; unknown avg `0.0593` n `765`
- 24h: commodity avg `-0.0053` n `12`; crypto_alt avg `1.5951` n `229`; crypto_major avg `1.9974` n `8`; equity avg `0.1605` n `88`; fx avg `-0.0155` n `6`; index avg `-0.0772` n `25`; metal avg `0.0366` n `20`; unknown avg `0.8867` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
