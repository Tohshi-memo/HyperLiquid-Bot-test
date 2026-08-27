# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T14:07:25.778727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0743` n `12`; crypto_alt avg `0.3514` n `231`; crypto_major avg `0.3183` n `8`; equity avg `-0.2004` n `127`; fx avg `-0.0041` n `6`; index avg `-0.0526` n `26`; metal avg `0.0171` n `20`; unknown avg `0.0452` n `792`
- 1h: commodity avg `0.2399` n `12`; crypto_alt avg `0.393` n `231`; crypto_major avg `0.3955` n `8`; equity avg `-0.4198` n `127`; fx avg `0.0312` n `6`; index avg `-0.0929` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0104` n `792`
- 4h: commodity avg `0.3043` n `12`; crypto_alt avg `-0.1356` n `231`; crypto_major avg `-0.4824` n `8`; equity avg `-0.7508` n `127`; fx avg `0.0389` n `6`; index avg `-0.1021` n `26`; metal avg `0.0309` n `20`; unknown avg `0.0119` n `792`
- 24h: commodity avg `0.5482` n `12`; crypto_alt avg `2.0972` n `231`; crypto_major avg `2.4419` n `8`; equity avg `1.1489` n `127`; fx avg `-0.0342` n `6`; index avg `0.0604` n `26`; metal avg `-0.3429` n `20`; unknown avg `0.5364` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
