# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T10:52:29.580745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.0697` n `230`; crypto_major avg `0.083` n `8`; equity avg `0.0494` n `92`; fx avg `-0.0015` n `6`; index avg `0.0008` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0035` n `765`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.0623` n `230`; crypto_major avg `0.1238` n `8`; equity avg `0.0311` n `92`; fx avg `-0.0123` n `6`; index avg `-0.0017` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0752` n `765`
- 4h: commodity avg `0.0118` n `12`; crypto_alt avg `0.0578` n `230`; crypto_major avg `0.1541` n `8`; equity avg `0.0731` n `92`; fx avg `-0.0067` n `6`; index avg `0.0266` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0912` n `759`
- 24h: commodity avg `-0.274` n `12`; crypto_alt avg `-0.176` n `229`; crypto_major avg `-0.6717` n `8`; equity avg `-0.1594` n `92`; fx avg `-0.0912` n `6`; index avg `0.1112` n `25`; metal avg `0.1516` n `20`; unknown avg `2.9287` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
