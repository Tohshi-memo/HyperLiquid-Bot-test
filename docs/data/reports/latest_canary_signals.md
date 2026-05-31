# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T05:22:18.359803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `-0.0036` n `228`; crypto_major avg `0.0852` n `8`; equity avg `0.0342` n `69`; fx avg `-0.0155` n `6`; index avg `0.0022` n `23`; metal avg `0.0293` n `18`; unknown avg `-0.5818` n `421`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.0713` n `228`; crypto_major avg `0.0908` n `8`; equity avg `0.053` n `69`; fx avg `-0.0208` n `6`; index avg `0.0034` n `23`; metal avg `0.0175` n `18`; unknown avg `-0.4113` n `421`
- 4h: commodity avg `0.0106` n `12`; crypto_alt avg `0.4214` n `228`; crypto_major avg `0.4361` n `8`; equity avg `0.1257` n `69`; fx avg `0.0011` n `6`; index avg `-0.0411` n `23`; metal avg `-0.0293` n `18`; unknown avg `-0.4937` n `419`
- 24h: commodity avg `0.0634` n `12`; crypto_alt avg `0.7624` n `228`; crypto_major avg `2.6121` n `8`; equity avg `0.9362` n `69`; fx avg `0.0313` n `6`; index avg `0.0509` n `23`; metal avg `0.0028` n `18`; unknown avg `0.4376` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
