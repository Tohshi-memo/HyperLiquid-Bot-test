# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T13:22:32.057482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5633` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.142` n `12`; crypto_alt avg `0.051` n `229`; crypto_major avg `-0.0444` n `8`; equity avg `-0.1706` n `88`; fx avg `0.0119` n `6`; index avg `-0.0272` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.1211` n `765`
- 1h: commodity avg `0.0444` n `12`; crypto_alt avg `-0.3816` n `229`; crypto_major avg `-0.9547` n `8`; equity avg `-0.3647` n `88`; fx avg `0.0287` n `6`; index avg `-0.0355` n `25`; metal avg `-0.1648` n `20`; unknown avg `-0.2635` n `765`
- 4h: commodity avg `0.029` n `12`; crypto_alt avg `-0.9926` n `229`; crypto_major avg `-1.5767` n `8`; equity avg `-0.4813` n `88`; fx avg `0.0288` n `6`; index avg `-0.0134` n `25`; metal avg `-0.2396` n `20`; unknown avg `-0.1892` n `765`
- 24h: commodity avg `-0.0946` n `12`; crypto_alt avg `-1.4973` n `229`; crypto_major avg `-1.553` n `8`; equity avg `-1.1652` n `88`; fx avg `0.1515` n `6`; index avg `-0.035` n `25`; metal avg `-0.4533` n `20`; unknown avg `0.5493` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
