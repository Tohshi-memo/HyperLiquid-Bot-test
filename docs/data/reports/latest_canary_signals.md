# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T13:52:24.725487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0039` n `230`; crypto_major avg `-0.011` n `8`; equity avg `-0.0089` n `92`; fx avg `0.0` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.0003` n `765`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.0818` n `230`; crypto_major avg `0.0964` n `8`; equity avg `-0.0134` n `92`; fx avg `0.0` n `6`; index avg `0.0066` n `25`; metal avg `0.0105` n `20`; unknown avg `-0.0039` n `765`
- 4h: commodity avg `0.0203` n `12`; crypto_alt avg `0.3676` n `230`; crypto_major avg `0.2863` n `8`; equity avg `-0.0751` n `92`; fx avg `-0.0134` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0122` n `20`; unknown avg `-0.1829` n `765`
- 24h: commodity avg `0.1288` n `12`; crypto_alt avg `0.2458` n `229`; crypto_major avg `-0.5796` n `8`; equity avg `-0.1346` n `92`; fx avg `-0.0395` n `6`; index avg `0.0847` n `25`; metal avg `0.0424` n `20`; unknown avg `2.9262` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
