# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T16:37:36.280202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0103` n `230`; crypto_major avg `-0.1851` n `8`; equity avg `-0.2999` n `112`; fx avg `-0.0089` n `6`; index avg `-0.0299` n `25`; metal avg `-0.0303` n `20`; unknown avg `-0.0161` n `782`
- 1h: commodity avg `0.0768` n `12`; crypto_alt avg `-0.0069` n `230`; crypto_major avg `-0.1891` n `8`; equity avg `-0.3487` n `112`; fx avg `-0.0176` n `6`; index avg `-0.0537` n `25`; metal avg `-0.0467` n `20`; unknown avg `-0.0412` n `782`
- 4h: commodity avg `0.3901` n `12`; crypto_alt avg `-0.1431` n `230`; crypto_major avg `-0.4861` n `8`; equity avg `-0.4207` n `112`; fx avg `0.0424` n `6`; index avg `-0.1183` n `25`; metal avg `-0.2442` n `20`; unknown avg `0.0523` n `782`
- 24h: commodity avg `0.4206` n `12`; crypto_alt avg `-0.2495` n `230`; crypto_major avg `-0.1908` n `8`; equity avg `0.5841` n `112`; fx avg `-0.1452` n `6`; index avg `-0.0448` n `25`; metal avg `0.266` n `20`; unknown avg `-0.0022` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
