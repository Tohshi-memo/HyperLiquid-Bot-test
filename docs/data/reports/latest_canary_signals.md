# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T11:52:25.008685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.0858` n `230`; crypto_major avg `0.0141` n `8`; equity avg `0.0097` n `113`; fx avg `0.0014` n `6`; index avg `0.0034` n `25`; metal avg `-0.0216` n `20`; unknown avg `-0.0263` n `787`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `-0.2579` n `230`; crypto_major avg `-0.2775` n `8`; equity avg `0.1488` n `113`; fx avg `-0.0093` n `6`; index avg `0.0177` n `25`; metal avg `-0.0654` n `20`; unknown avg `0.4613` n `787`
- 4h: commodity avg `-0.1901` n `12`; crypto_alt avg `-0.1965` n `230`; crypto_major avg `-0.6618` n `8`; equity avg `-0.0121` n `113`; fx avg `-0.0069` n `6`; index avg `0.0169` n `25`; metal avg `0.1133` n `20`; unknown avg `0.5187` n `787`
- 24h: commodity avg `-0.4477` n `12`; crypto_alt avg `-0.9429` n `230`; crypto_major avg `-0.9155` n `8`; equity avg `1.2617` n `113`; fx avg `0.0114` n `6`; index avg `0.1573` n `25`; metal avg `-0.6252` n `20`; unknown avg `0.6531` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2251`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
