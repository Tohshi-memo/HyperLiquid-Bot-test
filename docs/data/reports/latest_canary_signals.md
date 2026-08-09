# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T04:37:27.074140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.018` n `230`; crypto_major avg `-0.0424` n `8`; equity avg `0.0107` n `112`; fx avg `-0.0001` n `6`; index avg `0.0004` n `25`; metal avg `-0.0078` n `20`; unknown avg `1.2443` n `784`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `0.326` n `230`; crypto_major avg `0.0434` n `8`; equity avg `0.0006` n `112`; fx avg `-0.0044` n `6`; index avg `0.0039` n `25`; metal avg `-0.0081` n `20`; unknown avg `1.2581` n `784`
- 4h: commodity avg `0.1296` n `12`; crypto_alt avg `0.3989` n `230`; crypto_major avg `-0.1982` n `8`; equity avg `-0.0882` n `112`; fx avg `0.0018` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.1962` n `784`
- 24h: commodity avg `0.2637` n `12`; crypto_alt avg `1.6791` n `230`; crypto_major avg `0.4598` n `8`; equity avg `0.518` n `112`; fx avg `-0.0011` n `6`; index avg `0.0512` n `25`; metal avg `0.0102` n `20`; unknown avg `-0.0032` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
