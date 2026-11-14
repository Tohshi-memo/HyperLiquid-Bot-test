# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T02:07:24.474348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.1794` n `239`; crypto_major avg `-0.2522` n `8`; equity avg `-0.0076` n `162`; fx avg `-0.0147` n `6`; index avg `-0.004` n `27`; metal avg `-0.0126` n `20`; unknown avg `6.5057` n `1256`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `-0.48` n `239`; crypto_major avg `-0.4086` n `8`; equity avg `0.0095` n `162`; fx avg `-0.0026` n `6`; index avg `-0.02` n `27`; metal avg `0.0054` n `20`; unknown avg `4.1662` n `1256`
- 4h: commodity avg `0.0579` n `13`; crypto_alt avg `-0.4387` n `239`; crypto_major avg `-0.4673` n `8`; equity avg `-0.3523` n `162`; fx avg `-0.0291` n `6`; index avg `-0.0361` n `27`; metal avg `-0.005` n `20`; unknown avg `0.3108` n `1206`
- 24h: commodity avg `-0.0618` n `13`; crypto_alt avg `-1.8958` n `239`; crypto_major avg `-3.0645` n `8`; equity avg `-4.1465` n `162`; fx avg `-0.0862` n `6`; index avg `-0.3819` n `27`; metal avg `-0.588` n `20`; unknown avg `63.7956` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
