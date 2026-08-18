# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T22:37:29.824834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0146` n `230`; crypto_major avg `0.0092` n `8`; equity avg `-0.1336` n `120`; fx avg `-0.003` n `6`; index avg `-0.0284` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.1355` n `789`
- 1h: commodity avg `0.0207` n `12`; crypto_alt avg `0.0633` n `230`; crypto_major avg `0.0566` n `8`; equity avg `-0.0528` n `120`; fx avg `-0.0076` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0688` n `20`; unknown avg `-0.0368` n `789`
- 4h: commodity avg `0.0889` n `12`; crypto_alt avg `-0.3611` n `230`; crypto_major avg `-0.1748` n `8`; equity avg `-0.3963` n `120`; fx avg `-0.0107` n `6`; index avg `-0.061` n `25`; metal avg `-0.177` n `20`; unknown avg `-0.0074` n `789`
- 24h: commodity avg `0.2711` n `12`; crypto_alt avg `-0.5245` n `230`; crypto_major avg `0.1659` n `8`; equity avg `-4.6331` n `120`; fx avg `-0.0521` n `6`; index avg `-0.7279` n `25`; metal avg `-0.8064` n `20`; unknown avg `-0.2176` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
