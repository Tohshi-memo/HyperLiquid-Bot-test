# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T20:22:28.555364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.0319` n `235`; crypto_major avg `-0.0432` n `8`; equity avg `0.003` n `143`; fx avg `0.0062` n `6`; index avg `0.0006` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.9183` n `1079`
- 1h: commodity avg `-0.007` n `13`; crypto_alt avg `0.3535` n `235`; crypto_major avg `0.0655` n `8`; equity avg `0.0375` n `143`; fx avg `0.0155` n `6`; index avg `0.0001` n `26`; metal avg `0.0025` n `20`; unknown avg `0.1159` n `1068`
- 4h: commodity avg `0.0797` n `13`; crypto_alt avg `0.4015` n `235`; crypto_major avg `0.3972` n `8`; equity avg `0.095` n `143`; fx avg `-0.0037` n `6`; index avg `0.0158` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.3418` n `1062`
- 24h: commodity avg `0.0046` n `13`; crypto_alt avg `2.9376` n `235`; crypto_major avg `1.4866` n `8`; equity avg `0.1791` n `143`; fx avg `-0.0235` n `6`; index avg `0.0358` n `26`; metal avg `-0.0262` n `20`; unknown avg `-0.1739` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
