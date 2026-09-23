# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T11:52:31.170653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0531` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0378` n `12`; crypto_alt avg `0.5532` n `234`; crypto_major avg `0.2585` n `8`; equity avg `0.0955` n `140`; fx avg `-0.0` n `6`; index avg `0.0128` n `26`; metal avg `0.0481` n `20`; unknown avg `3.6324` n `946`
- 1h: commodity avg `0.1228` n `12`; crypto_alt avg `-0.6004` n `234`; crypto_major avg `-0.3395` n `8`; equity avg `-0.4542` n `140`; fx avg `0.0091` n `6`; index avg `-0.0521` n `26`; metal avg `-0.1065` n `20`; unknown avg `6.473` n `944`
- 4h: commodity avg `0.2255` n `12`; crypto_alt avg `-0.6241` n `234`; crypto_major avg `-1.1373` n `8`; equity avg `-0.5269` n `140`; fx avg `-0.0405` n `6`; index avg `-0.0842` n `26`; metal avg `-0.204` n `20`; unknown avg `3.7573` n `937`
- 24h: commodity avg `0.7654` n `12`; crypto_alt avg `3.1825` n `234`; crypto_major avg `0.2647` n `8`; equity avg `0.5266` n `140`; fx avg `0.0168` n `6`; index avg `0.0098` n `26`; metal avg `-0.2022` n `20`; unknown avg `3.294` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
