# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T22:15:44.642863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0387` n `228`; crypto_major avg `0.1426` n `8`; equity avg `0.0249` n `69`; fx avg `-0.0012` n `6`; index avg `0.0248` n `23`; metal avg `0.0287` n `18`; unknown avg `0.0113` n `422`
- 1h: commodity avg `0.0848` n `12`; crypto_alt avg `-0.2253` n `228`; crypto_major avg `-0.0888` n `8`; equity avg `-0.0669` n `69`; fx avg `-0.0244` n `6`; index avg `-0.111` n `23`; metal avg `-0.0014` n `18`; unknown avg `-0.026` n `422`
- 4h: commodity avg `0.2914` n `12`; crypto_alt avg `-0.7686` n `228`; crypto_major avg `-0.0917` n `8`; equity avg `-0.7883` n `69`; fx avg `-0.0271` n `6`; index avg `-0.526` n `23`; metal avg `-0.3058` n `18`; unknown avg `-0.3601` n `422`
- 24h: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.5394` n `228`; crypto_major avg `-1.5878` n `8`; equity avg `-0.1893` n `69`; fx avg `0.0382` n `6`; index avg `-0.0151` n `23`; metal avg `-0.0284` n `18`; unknown avg `2.1725` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
