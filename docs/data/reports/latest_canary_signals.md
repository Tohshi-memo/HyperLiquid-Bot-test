# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T18:37:24.520274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.0487` n `235`; crypto_major avg `0.0298` n `8`; equity avg `0.009` n `143`; fx avg `-0.003` n `6`; index avg `0.0026` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.0043` n `1078`
- 1h: commodity avg `0.1186` n `13`; crypto_alt avg `-0.2361` n `235`; crypto_major avg `0.0097` n `8`; equity avg `0.0147` n `143`; fx avg `-0.0107` n `6`; index avg `0.0102` n `26`; metal avg `0.0029` n `20`; unknown avg `0.3995` n `1076`
- 4h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.2432` n `235`; crypto_major avg `0.4869` n `8`; equity avg `0.0976` n `143`; fx avg `-0.0122` n `6`; index avg `0.0275` n `26`; metal avg `0.0062` n `20`; unknown avg `0.2084` n `966`
- 24h: commodity avg `0.2085` n `13`; crypto_alt avg `1.8377` n `235`; crypto_major avg `1.0093` n `8`; equity avg `0.3087` n `143`; fx avg `-0.0511` n `6`; index avg `0.0836` n `26`; metal avg `0.0434` n `20`; unknown avg `0.3007` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
