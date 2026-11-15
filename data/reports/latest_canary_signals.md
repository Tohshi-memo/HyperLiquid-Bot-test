# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T13:52:33.699686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `-0.013` n `239`; crypto_major avg `0.042` n `8`; equity avg `-0.0267` n `162`; fx avg `0.0049` n `6`; index avg `0.0027` n `27`; metal avg `0.0021` n `20`; unknown avg `0.2868` n `1264`
- 1h: commodity avg `-0.0721` n `13`; crypto_alt avg `-0.1457` n `239`; crypto_major avg `0.1651` n `8`; equity avg `0.0184` n `162`; fx avg `-0.0031` n `6`; index avg `0.008` n `27`; metal avg `-0.0122` n `20`; unknown avg `158.7345` n `1261`
- 4h: commodity avg `-0.0497` n `13`; crypto_alt avg `0.4197` n `239`; crypto_major avg `0.6349` n `8`; equity avg `0.0774` n `162`; fx avg `-0.0241` n `6`; index avg `0.0041` n `27`; metal avg `0.014` n `20`; unknown avg `0.0723` n `1253`
- 24h: commodity avg `-0.0268` n `13`; crypto_alt avg `-3.0247` n `239`; crypto_major avg `-2.1119` n `8`; equity avg `-0.5237` n `162`; fx avg `-0.0096` n `6`; index avg `-0.0451` n `27`; metal avg `-0.3296` n `20`; unknown avg `260.4127` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
