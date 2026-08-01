# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T04:07:31.214251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `12`; crypto_alt avg `0.1221` n `230`; crypto_major avg `0.0654` n `8`; equity avg `0.0075` n `102`; fx avg `0.0031` n `6`; index avg `0.0064` n `25`; metal avg `-0.007` n `20`; unknown avg `0.7372` n `781`
- 1h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.0733` n `230`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0577` n `102`; fx avg `-0.0172` n `6`; index avg `-0.0317` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.7069` n `781`
- 4h: commodity avg `-0.1515` n `12`; crypto_alt avg `0.4896` n `230`; crypto_major avg `0.1683` n `8`; equity avg `-0.1705` n `102`; fx avg `0.022` n `6`; index avg `-0.0156` n `25`; metal avg `-0.007` n `20`; unknown avg `0.2833` n `781`
- 24h: commodity avg `0.9167` n `12`; crypto_alt avg `0.3268` n `230`; crypto_major avg `-1.4415` n `8`; equity avg `-2.1508` n `102`; fx avg `-0.1199` n `6`; index avg `-0.207` n `25`; metal avg `-0.1912` n `20`; unknown avg `4.913` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
