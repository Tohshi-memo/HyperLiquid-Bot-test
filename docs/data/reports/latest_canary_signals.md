# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T16:52:26.826281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.0345` n `229`; crypto_major avg `-0.0682` n `8`; equity avg `-0.0176` n `88`; fx avg `-0.0145` n `6`; index avg `-0.0066` n `25`; metal avg `0.0469` n `20`; unknown avg `-0.0479` n `765`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.0612` n `229`; crypto_major avg `-0.0351` n `8`; equity avg `0.0505` n `88`; fx avg `-0.0188` n `6`; index avg `0.0429` n `25`; metal avg `0.0572` n `20`; unknown avg `-0.2446` n `765`
- 4h: commodity avg `0.1229` n `12`; crypto_alt avg `0.3602` n `229`; crypto_major avg `0.3569` n `8`; equity avg `-0.0682` n `88`; fx avg `-0.0492` n `6`; index avg `0.0082` n `25`; metal avg `-0.0526` n `20`; unknown avg `1.4033` n `765`
- 24h: commodity avg `0.2618` n `12`; crypto_alt avg `2.4035` n `229`; crypto_major avg `1.8333` n `8`; equity avg `1.8671` n `88`; fx avg `-0.0671` n `6`; index avg `0.5775` n `25`; metal avg `0.5716` n `20`; unknown avg `8.203` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
