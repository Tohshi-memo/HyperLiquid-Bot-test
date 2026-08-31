# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T05:22:26.234113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `0.5239` n `232`; crypto_major avg `0.538` n `8`; equity avg `0.2079` n `128`; fx avg `-0.0118` n `6`; index avg `0.021` n `26`; metal avg `0.0547` n `20`; unknown avg `1.2507` n `793`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `0.7814` n `232`; crypto_major avg `0.8219` n `8`; equity avg `0.6508` n `128`; fx avg `0.0069` n `6`; index avg `0.1327` n `26`; metal avg `0.1062` n `20`; unknown avg `0.8783` n `791`
- 4h: commodity avg `0.1801` n `12`; crypto_alt avg `0.9835` n `231`; crypto_major avg `0.5408` n `8`; equity avg `0.8112` n `128`; fx avg `-0.0326` n `6`; index avg `0.226` n `26`; metal avg `0.0097` n `20`; unknown avg `-0.2094` n `779`
- 24h: commodity avg `0.4724` n `12`; crypto_alt avg `0.143` n `231`; crypto_major avg `-1.485` n `8`; equity avg `-0.5469` n `128`; fx avg `-0.0432` n `6`; index avg `-0.1102` n `26`; metal avg `-0.2878` n `20`; unknown avg `-0.4693` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
