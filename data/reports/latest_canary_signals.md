# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T18:52:38.921285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0575` n `12`; crypto_alt avg `-0.0127` n `228`; crypto_major avg `-0.0138` n `8`; equity avg `0.017` n `77`; fx avg `0.0013` n `6`; index avg `0.0013` n `23`; metal avg `0.0637` n `18`; unknown avg `-0.0713` n `687`
- 1h: commodity avg `0.208` n `12`; crypto_alt avg `-0.3435` n `228`; crypto_major avg `0.0079` n `8`; equity avg `-0.0996` n `77`; fx avg `-0.0004` n `6`; index avg `-0.0478` n `23`; metal avg `0.1407` n `18`; unknown avg `-0.4562` n `687`
- 4h: commodity avg `0.5305` n `12`; crypto_alt avg `-0.372` n `228`; crypto_major avg `0.7796` n `8`; equity avg `0.7136` n `77`; fx avg `0.0116` n `6`; index avg `0.2956` n `23`; metal avg `-0.5687` n `18`; unknown avg `3.3556` n `687`
- 24h: commodity avg `-0.6482` n `12`; crypto_alt avg `5.8764` n `228`; crypto_major avg `7.4231` n `8`; equity avg `3.0868` n `76`; fx avg `0.0712` n `6`; index avg `1.2876` n `23`; metal avg `2.2342` n `18`; unknown avg `5.4756` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
