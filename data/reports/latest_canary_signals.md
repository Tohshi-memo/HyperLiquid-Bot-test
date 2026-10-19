# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T05:52:27.111113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `0.1175` n `237`; crypto_major avg `0.0041` n `8`; equity avg `0.0595` n `151`; fx avg `-0.0191` n `6`; index avg `-0.0047` n `26`; metal avg `0.0396` n `20`; unknown avg `0.0019` n `1194`
- 1h: commodity avg `0.0069` n `13`; crypto_alt avg `0.0255` n `237`; crypto_major avg `-0.1835` n `8`; equity avg `-0.0473` n `151`; fx avg `-0.0445` n `6`; index avg `-0.0001` n `26`; metal avg `0.0103` n `20`; unknown avg `-0.1053` n `1192`
- 4h: commodity avg `-0.0684` n `13`; crypto_alt avg `-0.076` n `237`; crypto_major avg `0.2348` n `8`; equity avg `0.5455` n `151`; fx avg `-0.0489` n `6`; index avg `0.102` n `26`; metal avg `0.0998` n `20`; unknown avg `0.448` n `1184`
- 24h: commodity avg `-0.429` n `13`; crypto_alt avg `0.6463` n `237`; crypto_major avg `1.193` n `8`; equity avg `2.7612` n `151`; fx avg `-0.056` n `6`; index avg `0.5121` n `26`; metal avg `0.3538` n `20`; unknown avg `3.5764` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1979`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1194`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0715`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.068`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
