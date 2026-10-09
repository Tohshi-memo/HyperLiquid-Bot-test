# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T18:22:31.094217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `-0.1895` n `235`; crypto_major avg `-0.179` n `8`; equity avg `-0.0088` n `150`; fx avg `0.0024` n `6`; index avg `0.0076` n `26`; metal avg `0.0041` n `20`; unknown avg `0.8712` n `1092`
- 1h: commodity avg `-0.0021` n `13`; crypto_alt avg `0.277` n `235`; crypto_major avg `0.144` n `8`; equity avg `0.1532` n `150`; fx avg `0.0081` n `6`; index avg `0.0292` n `26`; metal avg `0.0387` n `20`; unknown avg `0.8897` n `1090`
- 4h: commodity avg `-0.1292` n `13`; crypto_alt avg `0.4777` n `235`; crypto_major avg `-0.2965` n `8`; equity avg `0.3661` n `150`; fx avg `0.0143` n `6`; index avg `0.0467` n `26`; metal avg `0.0355` n `20`; unknown avg `1.6825` n `1020`
- 24h: commodity avg `-0.2523` n `13`; crypto_alt avg `3.1978` n `235`; crypto_major avg `1.5985` n `8`; equity avg `1.0777` n `150`; fx avg `0.0368` n `6`; index avg `0.1891` n `26`; metal avg `0.6742` n `20`; unknown avg `1.7634` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
