# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T21:22:22.294061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.2813` n `228`; crypto_major avg `-0.2021` n `8`; equity avg `-0.0126` n `69`; fx avg `0.0032` n `6`; index avg `0.0112` n `23`; metal avg `0.0177` n `18`; unknown avg `-0.3515` n `422`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.8033` n `228`; crypto_major avg `-0.7109` n `8`; equity avg `-0.019` n `69`; fx avg `0.006` n `6`; index avg `-0.0542` n `23`; metal avg `-0.0261` n `18`; unknown avg `-0.4328` n `422`
- 4h: commodity avg `-0.1377` n `12`; crypto_alt avg `-0.0539` n `228`; crypto_major avg `0.1189` n `8`; equity avg `-0.4256` n `69`; fx avg `0.0266` n `6`; index avg `-0.0587` n `23`; metal avg `0.0512` n `18`; unknown avg `-0.2436` n `422`
- 24h: commodity avg `0.5456` n `12`; crypto_alt avg `0.36` n `228`; crypto_major avg `-1.1507` n `8`; equity avg `-0.1781` n `69`; fx avg `0.0638` n `6`; index avg `0.0891` n `23`; metal avg `-0.0853` n `18`; unknown avg `2.1575` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
