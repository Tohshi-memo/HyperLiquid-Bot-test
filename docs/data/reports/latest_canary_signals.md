# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T00:37:31.039520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0507` n `13`; crypto_alt avg `-0.1132` n `235`; crypto_major avg `-0.0175` n `8`; equity avg `-0.0158` n `143`; fx avg `-0.0021` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.5116` n `1079`
- 1h: commodity avg `0.0065` n `13`; crypto_alt avg `-0.0382` n `235`; crypto_major avg `0.1329` n `8`; equity avg `-0.0125` n `143`; fx avg `0.0013` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.3023` n `1071`
- 4h: commodity avg `0.0619` n `13`; crypto_alt avg `0.0736` n `235`; crypto_major avg `-0.0008` n `8`; equity avg `0.0396` n `143`; fx avg `0.0093` n `6`; index avg `0.0031` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.1836` n `1055`
- 24h: commodity avg `-0.0499` n `13`; crypto_alt avg `1.4173` n `235`; crypto_major avg `0.4121` n `8`; equity avg `0.1586` n `143`; fx avg `-0.017` n `6`; index avg `0.035` n `26`; metal avg `-0.0165` n `20`; unknown avg `0.0175` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
