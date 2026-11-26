# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T18:52:31.724332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `0.0241` n `239`; crypto_major avg `0.0543` n `8`; equity avg `0.0477` n `168`; fx avg `-0.0005` n `6`; index avg `0.0016` n `27`; metal avg `-0.0086` n `20`; unknown avg `0.3156` n `1261`
- 1h: commodity avg `0.0333` n `13`; crypto_alt avg `0.403` n `239`; crypto_major avg `0.3381` n `8`; equity avg `0.1738` n `168`; fx avg `0.0034` n `6`; index avg `0.0083` n `27`; metal avg `-0.0072` n `20`; unknown avg `3.6984` n `1221`
- 4h: commodity avg `0.035` n `13`; crypto_alt avg `0.4988` n `239`; crypto_major avg `0.2831` n `8`; equity avg `-0.0008` n `168`; fx avg `-0.0013` n `6`; index avg `0.0007` n `27`; metal avg `-0.101` n `20`; unknown avg `3.6426` n `1201`
- 24h: commodity avg `0.0524` n `13`; crypto_alt avg `2.3644` n `239`; crypto_major avg `1.4372` n `8`; equity avg `1.4581` n `168`; fx avg `-0.0325` n `6`; index avg `0.0654` n `27`; metal avg `0.3393` n `20`; unknown avg `7.4441` n `1035`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
