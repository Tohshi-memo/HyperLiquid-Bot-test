# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T21:37:30.464389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.0436` n `235`; crypto_major avg `0.1135` n `8`; equity avg `-0.001` n `144`; fx avg `0.0207` n `6`; index avg `0.0042` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.0921` n `1072`
- 1h: commodity avg `-0.0675` n `13`; crypto_alt avg `-0.1231` n `235`; crypto_major avg `0.3434` n `8`; equity avg `0.0537` n `144`; fx avg `0.0164` n `6`; index avg `0.0101` n `26`; metal avg `-0.006` n `20`; unknown avg `3.5194` n `1056`
- 4h: commodity avg `-0.0268` n `13`; crypto_alt avg `0.3582` n `235`; crypto_major avg `0.5837` n `8`; equity avg `0.1057` n `144`; fx avg `0.0024` n `6`; index avg `0.0229` n `26`; metal avg `0.0084` n `20`; unknown avg `3.7255` n `1044`
- 24h: commodity avg `-0.1373` n `13`; crypto_alt avg `0.8614` n `235`; crypto_major avg `1.5343` n `8`; equity avg `0.2559` n `144`; fx avg `0.0256` n `6`; index avg `-0.0036` n `26`; metal avg `0.0006` n `20`; unknown avg `1.5414` n `1004`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
