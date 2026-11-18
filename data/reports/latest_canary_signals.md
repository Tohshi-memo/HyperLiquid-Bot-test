# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T07:07:32.377547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0789` n `13`; crypto_alt avg `0.2269` n `239`; crypto_major avg `0.3401` n `8`; equity avg `0.1033` n `163`; fx avg `-0.0286` n `6`; index avg `0.0091` n `27`; metal avg `-0.0496` n `20`; unknown avg `-0.0316` n `1260`
- 1h: commodity avg `-0.2298` n `13`; crypto_alt avg `0.1001` n `239`; crypto_major avg `0.0147` n `8`; equity avg `0.2025` n `163`; fx avg `-0.0323` n `6`; index avg `0.0149` n `27`; metal avg `-0.064` n `20`; unknown avg `9.9094` n `1258`
- 4h: commodity avg `-0.3944` n `13`; crypto_alt avg `0.6314` n `239`; crypto_major avg `0.4215` n `8`; equity avg `0.6078` n `163`; fx avg `-0.02` n `6`; index avg `0.0839` n `27`; metal avg `-0.1689` n `20`; unknown avg `4.6316` n `1224`
- 24h: commodity avg `-0.1226` n `13`; crypto_alt avg `0.4404` n `239`; crypto_major avg `0.619` n `8`; equity avg `0.6296` n `163`; fx avg `-0.1115` n `6`; index avg `0.0261` n `27`; metal avg `-0.9372` n `20`; unknown avg `483.7105` n `1089`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
