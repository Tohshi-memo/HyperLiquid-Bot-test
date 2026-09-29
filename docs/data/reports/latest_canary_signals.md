# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T13:37:35.050602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.2052` n `234`; crypto_major avg `-0.2275` n `8`; equity avg `-0.2828` n `141`; fx avg `0.0103` n `6`; index avg `-0.0549` n `26`; metal avg `-0.0314` n `20`; unknown avg `25.1473` n `963`
- 1h: commodity avg `-0.185` n `12`; crypto_alt avg `-0.0899` n `234`; crypto_major avg `-0.2655` n `8`; equity avg `-0.1982` n `141`; fx avg `0.0236` n `6`; index avg `-0.0501` n `26`; metal avg `-0.0667` n `20`; unknown avg `69.4562` n `961`
- 4h: commodity avg `-0.3797` n `12`; crypto_alt avg `0.797` n `234`; crypto_major avg `0.6743` n `8`; equity avg `0.2334` n `141`; fx avg `-0.0049` n `6`; index avg `0.0377` n `26`; metal avg `0.0031` n `20`; unknown avg `1.6153` n `955`
- 24h: commodity avg `-0.8196` n `12`; crypto_alt avg `1.0842` n `234`; crypto_major avg `0.6384` n `8`; equity avg `-0.1526` n `141`; fx avg `-0.0721` n `6`; index avg `-0.045` n `26`; metal avg `-0.1636` n `20`; unknown avg `90.6122` n `808`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
