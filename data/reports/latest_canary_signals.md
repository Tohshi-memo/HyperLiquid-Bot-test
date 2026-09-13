# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T03:37:30.036415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `0.0018` n `233`; crypto_major avg `-0.1343` n `8`; equity avg `-0.032` n `136`; fx avg `0.0178` n `6`; index avg `-0.0048` n `26`; metal avg `0.0006` n `20`; unknown avg `0.1054` n `838`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `0.1238` n `233`; crypto_major avg `-0.1404` n `8`; equity avg `-0.0749` n `136`; fx avg `0.0132` n `6`; index avg `-0.0225` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.0229` n `836`
- 4h: commodity avg `0.0208` n `12`; crypto_alt avg `0.5123` n `233`; crypto_major avg `-0.0986` n `8`; equity avg `-0.1595` n `130`; fx avg `0.0221` n `6`; index avg `-0.0386` n `26`; metal avg `0.0023` n `20`; unknown avg `3.7464` n `803`
- 24h: commodity avg `0.0045` n `12`; crypto_alt avg `1.0185` n `233`; crypto_major avg `0.0323` n `8`; equity avg `-0.5035` n `136`; fx avg `0.0107` n `6`; index avg `-0.0645` n `26`; metal avg `0.0329` n `20`; unknown avg `-0.2157` n `706`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
