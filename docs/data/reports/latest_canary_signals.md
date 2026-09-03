# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T07:07:32.710168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.3219` n `232`; crypto_major avg `0.3251` n `8`; equity avg `0.0769` n `133`; fx avg `-0.0479` n `6`; index avg `-0.0022` n `26`; metal avg `0.008` n `20`; unknown avg `0.1312` n `790`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `0.4839` n `232`; crypto_major avg `0.501` n `8`; equity avg `-0.0468` n `133`; fx avg `-0.0823` n `6`; index avg `-0.0525` n `26`; metal avg `-0.0564` n `20`; unknown avg `0.0323` n `788`
- 4h: commodity avg `-0.1948` n `12`; crypto_alt avg `0.6224` n `232`; crypto_major avg `0.3619` n `8`; equity avg `-0.1689` n `133`; fx avg `-0.1433` n `6`; index avg `-0.0908` n `26`; metal avg `-0.007` n `20`; unknown avg `-0.001` n `754`
- 24h: commodity avg `0.11` n `12`; crypto_alt avg `0.6999` n `232`; crypto_major avg `0.708` n `8`; equity avg `1.1117` n `133`; fx avg `-0.4288` n `6`; index avg `0.0597` n `26`; metal avg `0.6714` n `20`; unknown avg `-0.302` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0383`, n `668`, weak_sample_signal
