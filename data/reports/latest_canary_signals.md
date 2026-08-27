# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T12:52:35.813317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `12`; crypto_alt avg `0.1116` n `231`; crypto_major avg `0.0774` n `8`; equity avg `-0.1444` n `127`; fx avg `-0.0003` n `6`; index avg `-0.0266` n `26`; metal avg `-0.0452` n `20`; unknown avg `-0.0482` n `792`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `0.0996` n `231`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0392` n `127`; fx avg `0.0122` n `6`; index avg `-0.0016` n `26`; metal avg `-0.102` n `20`; unknown avg `0.0076` n `792`
- 4h: commodity avg `0.2953` n `12`; crypto_alt avg `-0.8183` n `231`; crypto_major avg `-0.7216` n `8`; equity avg `-0.5465` n `127`; fx avg `0.0067` n `6`; index avg `-0.0631` n `26`; metal avg `-0.1212` n `20`; unknown avg `0.0574` n `792`
- 24h: commodity avg `0.6041` n `12`; crypto_alt avg `1.2171` n `231`; crypto_major avg `1.7696` n `8`; equity avg `2.0858` n `127`; fx avg `-0.0847` n `6`; index avg `0.3076` n `26`; metal avg `-0.4274` n `20`; unknown avg `0.3904` n `775`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
