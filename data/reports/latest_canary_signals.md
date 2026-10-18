# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T21:52:55.090235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `13`; crypto_alt avg `0.4793` n `237`; crypto_major avg `0.2786` n `8`; equity avg `0.3745` n `151`; fx avg `0.0083` n `6`; index avg `0.061` n `26`; metal avg `0.0109` n `20`; unknown avg `0.9809` n `1154`
- 1h: commodity avg `-0.0385` n `13`; crypto_alt avg `0.8223` n `237`; crypto_major avg `0.7827` n `8`; equity avg `0.4897` n `151`; fx avg `-0.0295` n `6`; index avg `0.0716` n `26`; metal avg `0.0283` n `20`; unknown avg `1.6575` n `1114`
- 4h: commodity avg `-0.0131` n `13`; crypto_alt avg `-0.7868` n `237`; crypto_major avg `-0.0531` n `8`; equity avg `0.281` n `151`; fx avg `-0.0393` n `6`; index avg `0.0357` n `26`; metal avg `-0.0169` n `20`; unknown avg `4.8471` n `1096`
- 24h: commodity avg `-0.019` n `13`; crypto_alt avg `-2.9291` n `236`; crypto_major avg `-0.5339` n `8`; equity avg `0.2903` n `151`; fx avg `-0.0427` n `6`; index avg `0.0466` n `26`; metal avg `0.0208` n `20`; unknown avg `0.0124` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2065`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1431`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0739`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
