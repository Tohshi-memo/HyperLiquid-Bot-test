# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T16:07:35.051487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0147` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1214` n `12`; crypto_alt avg `-0.4064` n `228`; crypto_major avg `-0.3449` n `8`; equity avg `-0.3962` n `74`; fx avg `0.0026` n `6`; index avg `-0.1373` n `23`; metal avg `-0.0644` n `18`; unknown avg `0.1693` n `643`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `-1.2336` n `228`; crypto_major avg `-1.3245` n `8`; equity avg `-1.1441` n `74`; fx avg `0.0172` n `6`; index avg `-0.3098` n `23`; metal avg `0.1119` n `18`; unknown avg `0.3111` n `643`
- 4h: commodity avg `0.2277` n `12`; crypto_alt avg `-0.6717` n `228`; crypto_major avg `0.0708` n `8`; equity avg `-1.2302` n `74`; fx avg `0.0022` n `6`; index avg `-0.0123` n `23`; metal avg `-0.1316` n `18`; unknown avg `27.7277` n `643`
- 24h: commodity avg `-2.1512` n `12`; crypto_alt avg `0.9675` n `228`; crypto_major avg `1.9923` n `8`; equity avg `1.3842` n `74`; fx avg `0.102` n `6`; index avg `1.4741` n `23`; metal avg `2.5244` n `18`; unknown avg `40.4931` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
