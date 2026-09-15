# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T16:37:36.551909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1068` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0344` n `12`; crypto_alt avg `0.0751` n `233`; crypto_major avg `-0.0411` n `8`; equity avg `0.0211` n `137`; fx avg `-0.0062` n `6`; index avg `0.0079` n `27`; metal avg `0.0137` n `20`; unknown avg `-0.0122` n `903`
- 1h: commodity avg `0.0623` n `12`; crypto_alt avg `-0.0047` n `233`; crypto_major avg `-0.0659` n `8`; equity avg `-0.0341` n `137`; fx avg `-0.0271` n `6`; index avg `-0.0078` n `27`; metal avg `0.0823` n `20`; unknown avg `0.3354` n `901`
- 4h: commodity avg `0.3193` n `12`; crypto_alt avg `-0.856` n `233`; crypto_major avg `-1.248` n `8`; equity avg `-0.8004` n `137`; fx avg `0.0265` n `6`; index avg `-0.1412` n `27`; metal avg `0.0653` n `20`; unknown avg `1.617` n `873`
- 24h: commodity avg `0.3259` n `12`; crypto_alt avg `-2.0937` n `233`; crypto_major avg `-2.4186` n `8`; equity avg `-1.0647` n `137`; fx avg `0.2256` n `6`; index avg `-0.1413` n `27`; metal avg `-0.0097` n `20`; unknown avg `0.8596` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
