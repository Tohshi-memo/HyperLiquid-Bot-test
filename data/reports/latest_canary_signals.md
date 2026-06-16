# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T04:07:30.461170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0621` n `12`; crypto_alt avg `0.0276` n `228`; crypto_major avg `0.108` n `8`; equity avg `-0.0365` n `77`; fx avg `0.0106` n `6`; index avg `-0.0674` n `23`; metal avg `-0.0332` n `18`; unknown avg `-0.1444` n `687`
- 1h: commodity avg `0.0442` n `12`; crypto_alt avg `1.1402` n `228`; crypto_major avg `0.9331` n `8`; equity avg `0.2954` n `77`; fx avg `0.0321` n `6`; index avg `0.0708` n `23`; metal avg `0.2613` n `18`; unknown avg `2.0709` n `687`
- 4h: commodity avg `-0.3622` n `12`; crypto_alt avg `-0.1379` n `228`; crypto_major avg `0.0151` n `8`; equity avg `0.0093` n `77`; fx avg `-0.0517` n `6`; index avg `0.0479` n `23`; metal avg `-0.0005` n `18`; unknown avg `-0.1584` n `671`
- 24h: commodity avg `0.4269` n `12`; crypto_alt avg `0.5334` n `228`; crypto_major avg `1.9962` n `8`; equity avg `1.1329` n `76`; fx avg `-0.0571` n `6`; index avg `0.5411` n `23`; metal avg `-0.2171` n `18`; unknown avg `0.9616` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
