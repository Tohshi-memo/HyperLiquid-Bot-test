# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T05:52:31.427493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `-0.1229` n `239`; crypto_major avg `-0.1168` n `8`; equity avg `-0.1626` n `162`; fx avg `0.0062` n `6`; index avg `-0.013` n `27`; metal avg `-0.0541` n `20`; unknown avg `0.5263` n `1266`
- 1h: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.0968` n `239`; crypto_major avg `-0.0811` n `8`; equity avg `-0.444` n `162`; fx avg `0.0145` n `6`; index avg `-0.048` n `27`; metal avg `0.0416` n `20`; unknown avg `3.8669` n `1260`
- 4h: commodity avg `-0.1208` n `13`; crypto_alt avg `0.7407` n `239`; crypto_major avg `0.5067` n `8`; equity avg `-0.1821` n `162`; fx avg `-0.0075` n `6`; index avg `-0.068` n `27`; metal avg `0.1321` n `20`; unknown avg `-0.9125` n `1238`
- 24h: commodity avg `-1.2169` n `13`; crypto_alt avg `1.0188` n `239`; crypto_major avg `1.5743` n `8`; equity avg `-2.1977` n `162`; fx avg `-0.0159` n `6`; index avg `-0.2193` n `27`; metal avg `0.1365` n `20`; unknown avg `563.809` n `981`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
