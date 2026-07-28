# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T07:07:32.428292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.0111` n `230`; crypto_major avg `-0.078` n `8`; equity avg `-0.0046` n `102`; fx avg `0.0219` n `6`; index avg `0.0381` n `25`; metal avg `0.0123` n `20`; unknown avg `0.0127` n `774`
- 1h: commodity avg `-0.2714` n `12`; crypto_alt avg `0.4125` n `230`; crypto_major avg `0.384` n `8`; equity avg `0.2384` n `102`; fx avg `0.0067` n `6`; index avg `0.0794` n `25`; metal avg `0.0866` n `20`; unknown avg `0.0709` n `774`
- 4h: commodity avg `-0.016` n `12`; crypto_alt avg `0.3239` n `230`; crypto_major avg `0.1544` n `8`; equity avg `0.0064` n `102`; fx avg `-0.0477` n `6`; index avg `0.0416` n `25`; metal avg `0.0569` n `20`; unknown avg `-0.0211` n `758`
- 24h: commodity avg `-0.6498` n `12`; crypto_alt avg `-3.5905` n `230`; crypto_major avg `-3.631` n `8`; equity avg `-4.1044` n `102`; fx avg `-0.1943` n `6`; index avg `-0.8342` n `25`; metal avg `-0.4211` n `20`; unknown avg `1161.5416` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
