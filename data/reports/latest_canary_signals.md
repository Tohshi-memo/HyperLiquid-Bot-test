# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T01:37:29.483801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.4626` n `234`; crypto_major avg `-0.2946` n `8`; equity avg `-0.106` n `141`; fx avg `-0.0302` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0145` n `20`; unknown avg `0.4896` n `946`
- 1h: commodity avg `-0.069` n `12`; crypto_alt avg `-0.3373` n `234`; crypto_major avg `-0.2638` n `8`; equity avg `0.1863` n `141`; fx avg `-0.0711` n `6`; index avg `0.0677` n `26`; metal avg `0.1362` n `20`; unknown avg `1.857` n `944`
- 4h: commodity avg `-0.374` n `12`; crypto_alt avg `-0.5872` n `234`; crypto_major avg `-0.42` n `8`; equity avg `0.2583` n `141`; fx avg `-0.0701` n `6`; index avg `0.0652` n `26`; metal avg `0.0891` n `20`; unknown avg `3.5404` n `898`
- 24h: commodity avg `0.4842` n `12`; crypto_alt avg `3.3937` n `234`; crypto_major avg `0.7285` n `8`; equity avg `0.0739` n `141`; fx avg `-0.0579` n `6`; index avg `-0.0323` n `26`; metal avg `-0.0068` n `20`; unknown avg `23.9956` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
