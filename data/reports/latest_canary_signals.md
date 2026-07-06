# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T14:37:30.081300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6529` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.284` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0819` n `12`; crypto_alt avg `0.3132` n `229`; crypto_major avg `0.2326` n `8`; equity avg `0.0835` n `88`; fx avg `0.0035` n `6`; index avg `0.0147` n `25`; metal avg `0.0365` n `20`; unknown avg `0.2639` n `765`
- 1h: commodity avg `0.2381` n `12`; crypto_alt avg `1.012` n `229`; crypto_major avg `0.7641` n `8`; equity avg `1.1175` n `88`; fx avg `-0.0004` n `6`; index avg `0.1376` n `25`; metal avg `0.005` n `20`; unknown avg `0.5662` n `765`
- 4h: commodity avg `0.2603` n `12`; crypto_alt avg `-0.3892` n `229`; crypto_major avg `-1.1809` n `8`; equity avg `0.472` n `88`; fx avg `0.0324` n `6`; index avg `0.1031` n `25`; metal avg `-0.1943` n `20`; unknown avg `-0.2037` n `765`
- 24h: commodity avg `0.0501` n `12`; crypto_alt avg `-0.3129` n `229`; crypto_major avg `-0.921` n `8`; equity avg `-0.1295` n `88`; fx avg `0.1805` n `6`; index avg `0.0567` n `25`; metal avg `-0.3346` n `20`; unknown avg `0.7219` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
