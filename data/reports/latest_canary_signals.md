# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T20:52:26.960373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.2425` n `232`; crypto_major avg `-0.2096` n `8`; equity avg `-0.0199` n `131`; fx avg `0.0042` n `6`; index avg `0.0009` n `26`; metal avg `0.0192` n `20`; unknown avg `0.0539` n `793`
- 1h: commodity avg `0.0348` n `12`; crypto_alt avg `-0.2076` n `232`; crypto_major avg `0.0151` n `8`; equity avg `0.0674` n `131`; fx avg `0.0059` n `6`; index avg `0.0296` n `26`; metal avg `0.0185` n `20`; unknown avg `0.4252` n `779`
- 4h: commodity avg `0.3642` n `12`; crypto_alt avg `-0.2679` n `232`; crypto_major avg `-0.5233` n `8`; equity avg `-0.1807` n `131`; fx avg `0.0199` n `6`; index avg `-0.0538` n `26`; metal avg `-0.2895` n `20`; unknown avg `-0.1327` n `779`
- 24h: commodity avg `0.8822` n `12`; crypto_alt avg `-0.447` n `232`; crypto_major avg `-2.0378` n `8`; equity avg `-1.8983` n `130`; fx avg `0.057` n `6`; index avg `-0.329` n `26`; metal avg `-0.8866` n `20`; unknown avg `-0.0674` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0319`, n `668`, weak_sample_signal
