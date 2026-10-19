# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T16:22:36.875982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0515` n `13`; crypto_alt avg `0.2579` n `237`; crypto_major avg `0.1317` n `8`; equity avg `-0.1154` n `151`; fx avg `0.0128` n `6`; index avg `-0.0041` n `26`; metal avg `0.0252` n `20`; unknown avg `4.1696` n `1196`
- 1h: commodity avg `0.2553` n `13`; crypto_alt avg `-0.3554` n `237`; crypto_major avg `-0.5392` n `8`; equity avg `-0.3157` n `151`; fx avg `-0.0076` n `6`; index avg `-0.0533` n `26`; metal avg `0.004` n `20`; unknown avg `3.8439` n `1186`
- 4h: commodity avg `0.1802` n `13`; crypto_alt avg `0.0404` n `237`; crypto_major avg `-0.6371` n `8`; equity avg `-0.2655` n `151`; fx avg `0.0078` n `6`; index avg `0.0353` n `26`; metal avg `-0.161` n `20`; unknown avg `3.8724` n `1113`
- 24h: commodity avg `-0.0767` n `13`; crypto_alt avg `1.2898` n `237`; crypto_major avg `1.6048` n `8`; equity avg `3.1814` n `151`; fx avg `-0.0242` n `6`; index avg `0.6171` n `26`; metal avg `0.1045` n `20`; unknown avg `8.7671` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
