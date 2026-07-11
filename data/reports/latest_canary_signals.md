# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T08:07:27.795923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `-0.0035` n `8`; equity avg `-0.0022` n `92`; fx avg `-0.0048` n `6`; index avg `0.0028` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.0016` n `765`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0598` n `230`; crypto_major avg `0.0205` n `8`; equity avg `0.0149` n `92`; fx avg `-0.0007` n `6`; index avg `0.0079` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.0357` n `763`
- 4h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.2077` n `229`; crypto_major avg `0.033` n `8`; equity avg `0.1116` n `92`; fx avg `0.0181` n `6`; index avg `0.0186` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0101` n `733`
- 24h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.3377` n `229`; crypto_major avg `-0.1696` n `8`; equity avg `0.3531` n `92`; fx avg `-0.0826` n `6`; index avg `0.2109` n `25`; metal avg `0.0923` n `20`; unknown avg `2.9139` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
