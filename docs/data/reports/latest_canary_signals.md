# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T04:22:28.884273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.1183` n `230`; crypto_major avg `-0.1097` n `8`; equity avg `-0.0092` n `96`; fx avg `-0.0025` n `6`; index avg `0.0012` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0124` n `769`
- 1h: commodity avg `-0.0751` n `12`; crypto_alt avg `-0.1655` n `230`; crypto_major avg `-0.1317` n `8`; equity avg `-0.051` n `96`; fx avg `0.006` n `6`; index avg `0.0241` n `25`; metal avg `0.0045` n `20`; unknown avg `0.5096` n `769`
- 4h: commodity avg `-0.0625` n `12`; crypto_alt avg `-0.3313` n `230`; crypto_major avg `-0.206` n `8`; equity avg `0.1059` n `96`; fx avg `-0.0017` n `6`; index avg `0.0586` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.2193` n `769`
- 24h: commodity avg `0.6507` n `12`; crypto_alt avg `-0.3381` n `230`; crypto_major avg `0.0577` n `8`; equity avg `0.8261` n `96`; fx avg `0.0474` n `6`; index avg `0.1184` n `25`; metal avg `0.2033` n `20`; unknown avg `0.2215` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
