# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T18:52:29.182228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0068` n `229`; crypto_major avg `0.0225` n `8`; equity avg `-0.002` n `88`; fx avg `0.0` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.275` n `765`
- 1h: commodity avg `-0.0483` n `12`; crypto_alt avg `-0.3862` n `229`; crypto_major avg `-0.4402` n `8`; equity avg `-0.095` n `88`; fx avg `-0.0103` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.3703` n `765`
- 4h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.8216` n `229`; crypto_major avg `0.5843` n `8`; equity avg `-0.0085` n `88`; fx avg `0.0008` n `6`; index avg `-0.0307` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.2516` n `765`
- 24h: commodity avg `-0.0414` n `12`; crypto_alt avg `1.324` n `229`; crypto_major avg `1.6192` n `8`; equity avg `0.1373` n `88`; fx avg `-0.0119` n `6`; index avg `-0.0806` n `25`; metal avg `0.0309` n `20`; unknown avg `0.185` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
