# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T20:52:30.395051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.0098` n `231`; crypto_major avg `-0.0154` n `8`; equity avg `-0.0203` n `127`; fx avg `-0.0002` n `6`; index avg `-0.0009` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.0732` n `792`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.0504` n `231`; crypto_major avg `-0.0658` n `8`; equity avg `-0.0895` n `127`; fx avg `0.0045` n `6`; index avg `0.0072` n `26`; metal avg `-0.0263` n `20`; unknown avg `0.0273` n `792`
- 4h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.7867` n `231`; crypto_major avg `-0.5965` n `8`; equity avg `0.1363` n `127`; fx avg `0.0072` n `6`; index avg `-0.0091` n `26`; metal avg `0.0173` n `20`; unknown avg `0.1914` n `792`
- 24h: commodity avg `0.3579` n `12`; crypto_alt avg `3.0292` n `231`; crypto_major avg `4.1167` n `8`; equity avg `1.0225` n `127`; fx avg `-0.0337` n `6`; index avg `0.1276` n `26`; metal avg `0.2549` n `20`; unknown avg `1.1255` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
