# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T07:22:26.639032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `0.5528` n `235`; crypto_major avg `0.3161` n `8`; equity avg `0.1147` n `150`; fx avg `0.0235` n `6`; index avg `0.0307` n `26`; metal avg `0.034` n `20`; unknown avg `0.1413` n `1077`
- 1h: commodity avg `0.307` n `13`; crypto_alt avg `0.8514` n `235`; crypto_major avg `0.5449` n `8`; equity avg `-0.2118` n `150`; fx avg `0.0274` n `6`; index avg `-0.0507` n `26`; metal avg `0.02` n `20`; unknown avg `0.3003` n `1075`
- 4h: commodity avg `0.3732` n `13`; crypto_alt avg `0.1993` n `235`; crypto_major avg `-0.1143` n `8`; equity avg `-0.7655` n `150`; fx avg `-0.0055` n `6`; index avg `-0.1418` n `26`; metal avg `-0.1667` n `20`; unknown avg `0.3978` n `1041`
- 24h: commodity avg `0.7435` n `13`; crypto_alt avg `-0.8005` n `235`; crypto_major avg `-2.1109` n `8`; equity avg `-1.9215` n `150`; fx avg `-0.083` n `6`; index avg `-0.3244` n `26`; metal avg `-0.2339` n `20`; unknown avg `416.827` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
