# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T06:22:28.543825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.0383` n `230`; crypto_major avg `0.1683` n `8`; equity avg `0.0158` n `112`; fx avg `-0.0158` n `6`; index avg `0.0013` n `25`; metal avg `0.0658` n `20`; unknown avg `0.0402` n `782`
- 1h: commodity avg `-0.0671` n `12`; crypto_alt avg `0.3664` n `230`; crypto_major avg `0.4258` n `8`; equity avg `0.1351` n `112`; fx avg `-0.0127` n `6`; index avg `-0.0019` n `25`; metal avg `0.2299` n `20`; unknown avg `-0.0074` n `766`
- 4h: commodity avg `0.0368` n `12`; crypto_alt avg `0.0555` n `230`; crypto_major avg `-0.0721` n `8`; equity avg `0.3744` n `112`; fx avg `0.0119` n `6`; index avg `0.059` n `25`; metal avg `0.2615` n `20`; unknown avg `-0.0092` n `766`
- 24h: commodity avg `0.5206` n `12`; crypto_alt avg `0.4453` n `230`; crypto_major avg `-0.933` n `8`; equity avg `1.2292` n `109`; fx avg `-0.0203` n `6`; index avg `-0.0409` n `25`; metal avg `0.2773` n `20`; unknown avg `110.8213` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
