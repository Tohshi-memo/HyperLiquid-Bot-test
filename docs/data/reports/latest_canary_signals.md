# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T20:46:48.166492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0631` n `12`; crypto_alt avg `0.2111` n `234`; crypto_major avg `0.1387` n `8`; equity avg `0.0706` n `141`; fx avg `0.0007` n `6`; index avg `0.0193` n `26`; metal avg `0.0375` n `20`; unknown avg `4.9744` n `946`
- 1h: commodity avg `-0.1982` n `12`; crypto_alt avg `-0.2632` n `234`; crypto_major avg `-0.2181` n `8`; equity avg `-0.1432` n `141`; fx avg `-0.0101` n `6`; index avg `-0.0363` n `26`; metal avg `-0.0487` n `20`; unknown avg `5.3489` n `898`
- 4h: commodity avg `0.0907` n `12`; crypto_alt avg `-0.0811` n `234`; crypto_major avg `-0.0284` n `8`; equity avg `-0.1996` n `141`; fx avg `0.0053` n `6`; index avg `-0.0853` n `26`; metal avg `-0.0494` n `20`; unknown avg `7.3374` n `869`
- 24h: commodity avg `0.7763` n `12`; crypto_alt avg `4.2882` n `234`; crypto_major avg `1.7469` n `8`; equity avg `-0.2997` n `141`; fx avg `0.0398` n `6`; index avg `-0.1202` n `26`; metal avg `-0.119` n `20`; unknown avg `15.6137` n `849`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
