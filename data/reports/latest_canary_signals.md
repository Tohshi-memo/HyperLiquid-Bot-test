# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T02:07:31.316355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `13`; crypto_alt avg `0.4014` n `235`; crypto_major avg `0.2777` n `8`; equity avg `0.0155` n `151`; fx avg `0.0102` n `6`; index avg `-0.0021` n `26`; metal avg `0.0101` n `20`; unknown avg `0.1854` n `1131`
- 1h: commodity avg `0.0029` n `13`; crypto_alt avg `-0.2791` n `235`; crypto_major avg `-0.1582` n `8`; equity avg `-0.1239` n `151`; fx avg `0.0281` n `6`; index avg `0.0084` n `26`; metal avg `0.0325` n `20`; unknown avg `0.5958` n `1131`
- 4h: commodity avg `-0.4598` n `13`; crypto_alt avg `0.1069` n `235`; crypto_major avg `0.2565` n `8`; equity avg `-0.0004` n `151`; fx avg `-0.0169` n `6`; index avg `-0.0184` n `26`; metal avg `0.1401` n `20`; unknown avg `0.6535` n `1109`
- 24h: commodity avg `-0.3799` n `13`; crypto_alt avg `1.4944` n `235`; crypto_major avg `0.8378` n `8`; equity avg `0.2567` n `151`; fx avg `-0.0274` n `6`; index avg `0.0212` n `26`; metal avg `0.1904` n `20`; unknown avg `0.7615` n `948`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
