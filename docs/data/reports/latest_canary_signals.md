# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T22:07:31.976051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0754` n `229`; crypto_major avg `-0.0532` n `8`; equity avg `0.0063` n `88`; fx avg `0.0045` n `6`; index avg `0.0031` n `25`; metal avg `0.0031` n `20`; unknown avg `0.0112` n `765`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0679` n `229`; crypto_major avg `0.0469` n `8`; equity avg `0.0274` n `88`; fx avg `0.0012` n `6`; index avg `0.0149` n `25`; metal avg `0.0053` n `20`; unknown avg `3.7522` n `765`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.6427` n `229`; crypto_major avg `-0.584` n `8`; equity avg `0.0547` n `88`; fx avg `-0.0238` n `6`; index avg `0.019` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.4772` n `765`
- 24h: commodity avg `-0.026` n `12`; crypto_alt avg `0.2105` n `229`; crypto_major avg `0.5575` n `8`; equity avg `0.2179` n `88`; fx avg `-0.027` n `6`; index avg `-0.0092` n `25`; metal avg `0.0865` n `20`; unknown avg `-0.1765` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
