# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T07:22:32.389565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `-0.0394` n `230`; crypto_major avg `-0.1024` n `8`; equity avg `0.0782` n `102`; fx avg `-0.0096` n `6`; index avg `-0.0134` n `25`; metal avg `0.013` n `20`; unknown avg `0.0972` n `777`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0851` n `230`; crypto_major avg `0.2403` n `8`; equity avg `0.7201` n `102`; fx avg `-0.0014` n `6`; index avg `0.221` n `25`; metal avg `0.1048` n `20`; unknown avg `-0.0109` n `777`
- 4h: commodity avg `-0.0783` n `12`; crypto_alt avg `-0.4275` n `230`; crypto_major avg `0.5466` n `8`; equity avg `0.8335` n `102`; fx avg `-0.0713` n `6`; index avg `0.2651` n `25`; metal avg `0.1595` n `20`; unknown avg `-0.0175` n `761`
- 24h: commodity avg `0.0104` n `12`; crypto_alt avg `-1.4724` n `230`; crypto_major avg `0.9405` n `8`; equity avg `-1.3627` n `102`; fx avg `-0.1352` n `6`; index avg `-0.2019` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.2494` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
