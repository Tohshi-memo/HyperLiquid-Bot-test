# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T00:22:29.808061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `-0.1392` n `232`; crypto_major avg `-0.2111` n `8`; equity avg `-0.1853` n `133`; fx avg `-0.039` n `6`; index avg `-0.0399` n `26`; metal avg `0.008` n `20`; unknown avg `0.1284` n `792`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.0992` n `232`; crypto_major avg `0.0953` n `8`; equity avg `-0.116` n `133`; fx avg `0.0261` n `6`; index avg `-0.0721` n `26`; metal avg `0.0219` n `20`; unknown avg `0.2538` n `790`
- 4h: commodity avg `0.084` n `12`; crypto_alt avg `0.0628` n `232`; crypto_major avg `-0.1013` n `8`; equity avg `0.2035` n `133`; fx avg `0.0351` n `6`; index avg `-0.0411` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.0016` n `784`
- 24h: commodity avg `0.1423` n `12`; crypto_alt avg `-0.2553` n `232`; crypto_major avg `-0.5261` n `8`; equity avg `0.7652` n `133`; fx avg `-0.3078` n `6`; index avg `0.002` n `26`; metal avg `0.4509` n `20`; unknown avg `-0.5135` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
