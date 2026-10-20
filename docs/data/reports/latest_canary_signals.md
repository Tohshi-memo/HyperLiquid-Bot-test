# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T02:22:29.746290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `13`; crypto_alt avg `0.2437` n `237`; crypto_major avg `0.1603` n `8`; equity avg `0.4077` n `151`; fx avg `-0.0171` n `6`; index avg `0.0727` n `26`; metal avg `0.058` n `20`; unknown avg `1.0415` n `1198`
- 1h: commodity avg `-0.078` n `13`; crypto_alt avg `0.4246` n `237`; crypto_major avg `0.2284` n `8`; equity avg `0.6846` n `151`; fx avg `-0.0057` n `6`; index avg `0.1475` n `26`; metal avg `0.2075` n `20`; unknown avg `3.2958` n `1196`
- 4h: commodity avg `0.0624` n `13`; crypto_alt avg `-0.5998` n `237`; crypto_major avg `-0.6204` n `8`; equity avg `-0.4897` n `151`; fx avg `-0.0232` n `6`; index avg `-0.0935` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.1241` n `1188`
- 24h: commodity avg `0.164` n `13`; crypto_alt avg `-0.2633` n `237`; crypto_major avg `-0.5249` n `8`; equity avg `-0.2027` n `151`; fx avg `-0.0054` n `6`; index avg `-0.0138` n `26`; metal avg `-0.2193` n `20`; unknown avg `4.9155` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
