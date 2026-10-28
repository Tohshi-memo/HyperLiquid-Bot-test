# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T09:07:25.708129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0181` n `13`; crypto_alt avg `-0.0756` n `238`; crypto_major avg `-0.0867` n `8`; equity avg `-0.0479` n `154`; fx avg `-0.0058` n `6`; index avg `-0.008` n `27`; metal avg `-0.0235` n `20`; unknown avg `0.2114` n `1232`
- 1h: commodity avg `0.0026` n `13`; crypto_alt avg `0.1494` n `238`; crypto_major avg `0.2628` n `8`; equity avg `-0.191` n `154`; fx avg `0.0098` n `6`; index avg `-0.0372` n `27`; metal avg `-0.0113` n `20`; unknown avg `85.5518` n `1228`
- 4h: commodity avg `-0.0288` n `13`; crypto_alt avg `0.2099` n `238`; crypto_major avg `0.5299` n `8`; equity avg `0.1726` n `154`; fx avg `-0.0295` n `6`; index avg `0.0383` n `27`; metal avg `0.0644` n `20`; unknown avg `24.047` n `1194`
- 24h: commodity avg `-0.2059` n `13`; crypto_alt avg `1.9878` n `238`; crypto_major avg `2.4639` n `8`; equity avg `3.5399` n `154`; fx avg `0.0846` n `6`; index avg `0.4752` n `27`; metal avg `0.372` n `20`; unknown avg `16.3288` n `1026`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
