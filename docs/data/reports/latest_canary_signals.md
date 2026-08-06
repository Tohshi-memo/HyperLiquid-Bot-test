# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T11:07:32.270950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `12`; crypto_alt avg `-0.2036` n `230`; crypto_major avg `-0.1351` n `8`; equity avg `-0.4051` n `109`; fx avg `0.0097` n `6`; index avg `-0.0624` n `25`; metal avg `-0.0575` n `20`; unknown avg `-0.0636` n `781`
- 1h: commodity avg `0.1296` n `12`; crypto_alt avg `-0.1572` n `230`; crypto_major avg `-0.1205` n `8`; equity avg `-0.6862` n `109`; fx avg `0.0086` n `6`; index avg `-0.1062` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.0327` n `781`
- 4h: commodity avg `0.0886` n `12`; crypto_alt avg `-0.6252` n `230`; crypto_major avg `-0.66` n `8`; equity avg `-0.7228` n `109`; fx avg `0.0021` n `6`; index avg `-0.1131` n `25`; metal avg `0.1187` n `20`; unknown avg `108.1395` n `781`
- 24h: commodity avg `-0.1569` n `12`; crypto_alt avg `-0.3201` n `230`; crypto_major avg `-0.679` n `8`; equity avg `-2.1002` n `109`; fx avg `0.0025` n `6`; index avg `-0.4085` n `25`; metal avg `0.4396` n `20`; unknown avg `112.983` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
