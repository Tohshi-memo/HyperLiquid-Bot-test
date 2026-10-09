# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T06:01:10.066924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `0.0595` n `235`; crypto_major avg `0.0558` n `8`; equity avg `0.0161` n `150`; fx avg `-0.0051` n `6`; index avg `0.0034` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.0631` n `1046`
- 1h: commodity avg `0.0054` n `13`; crypto_alt avg `0.2087` n `235`; crypto_major avg `0.1818` n `8`; equity avg `0.2524` n `150`; fx avg `0.0187` n `6`; index avg `0.0174` n `26`; metal avg `0.0434` n `20`; unknown avg `-0.1759` n `1046`
- 4h: commodity avg `-0.0687` n `13`; crypto_alt avg `0.7213` n `235`; crypto_major avg `0.4193` n `8`; equity avg `0.4758` n `150`; fx avg `0.018` n `6`; index avg `0.0686` n `26`; metal avg `0.1353` n `20`; unknown avg `-0.2355` n `1040`
- 24h: commodity avg `0.0308` n `13`; crypto_alt avg `-1.1776` n `235`; crypto_major avg `-2.0713` n `8`; equity avg `-1.1741` n `150`; fx avg `0.1526` n `6`; index avg `-0.0961` n `26`; metal avg `0.3728` n `20`; unknown avg `5.1495` n `985`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
