# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T08:22:24.285514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.0576` n `231`; crypto_major avg `0.0369` n `8`; equity avg `-0.0113` n `127`; fx avg `0.0041` n `6`; index avg `-0.0005` n `26`; metal avg `0.003` n `20`; unknown avg `-0.0073` n `793`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.2441` n `231`; crypto_major avg `-0.0926` n `8`; equity avg `-0.0056` n `127`; fx avg `0.0081` n `6`; index avg `-0.0027` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0175` n `793`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.3606` n `231`; crypto_major avg `-0.2286` n `8`; equity avg `0.0486` n `127`; fx avg `0.0126` n `6`; index avg `0.0084` n `26`; metal avg `0.0084` n `20`; unknown avg `0.1165` n `761`
- 24h: commodity avg `-0.0027` n `12`; crypto_alt avg `-2.2486` n `231`; crypto_major avg `-2.7254` n `8`; equity avg `-1.3511` n `127`; fx avg `-0.0169` n `6`; index avg `-0.1211` n `26`; metal avg `-0.5999` n `20`; unknown avg `-0.4481` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
