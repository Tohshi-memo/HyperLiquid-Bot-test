# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T08:52:25.385265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `13`; crypto_alt avg `0.0679` n `239`; crypto_major avg `0.1085` n `8`; equity avg `0.239` n `168`; fx avg `-0.0007` n `6`; index avg `0.0337` n `27`; metal avg `0.1496` n `20`; unknown avg `0.381` n `1205`
- 1h: commodity avg `-0.086` n `13`; crypto_alt avg `0.1474` n `239`; crypto_major avg `0.0629` n `8`; equity avg `0.7222` n `168`; fx avg `-0.0237` n `6`; index avg `0.0834` n `27`; metal avg `0.1113` n `20`; unknown avg `2.0601` n `1131`
- 4h: commodity avg `-0.0908` n `13`; crypto_alt avg `0.2248` n `239`; crypto_major avg `0.4365` n `8`; equity avg `1.0018` n `168`; fx avg `-0.0484` n `6`; index avg `0.0363` n `27`; metal avg `0.4971` n `20`; unknown avg `0.7339` n `1113`
- 24h: commodity avg `0.4303` n `13`; crypto_alt avg `2.0129` n `239`; crypto_major avg `2.4429` n `8`; equity avg `3.8645` n `168`; fx avg `-0.0798` n `6`; index avg `0.3128` n `27`; metal avg `1.249` n `20`; unknown avg `60.691` n `1035`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
