# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T11:37:31.673021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `-0.046` n `230`; crypto_major avg `0.0347` n `8`; equity avg `-0.0001` n `113`; fx avg `0.0128` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.0081` n `785`
- 1h: commodity avg `-0.2619` n `12`; crypto_alt avg `0.0575` n `230`; crypto_major avg `0.2344` n `8`; equity avg `0.301` n `113`; fx avg `-0.025` n `6`; index avg `0.0267` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0177` n `785`
- 4h: commodity avg `-0.3972` n `12`; crypto_alt avg `0.0837` n `230`; crypto_major avg `0.5594` n `8`; equity avg `0.3516` n `113`; fx avg `-0.0484` n `6`; index avg `0.0775` n `25`; metal avg `0.2054` n `20`; unknown avg `-0.0118` n `785`
- 24h: commodity avg `0.5465` n `12`; crypto_alt avg `-1.284` n `230`; crypto_major avg `-0.4402` n `8`; equity avg `-0.7205` n `113`; fx avg `-0.0313` n `6`; index avg `0.0807` n `25`; metal avg `0.4229` n `20`; unknown avg `0.0814` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
