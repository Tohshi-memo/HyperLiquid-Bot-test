# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T00:22:23.005770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.7842` n `228`; crypto_major avg `0.6557` n `8`; equity avg `-0.0141` n `69`; fx avg `0.0163` n `6`; index avg `-0.0187` n `23`; metal avg `0.0238` n `18`; unknown avg `0.1022` n `422`
- 1h: commodity avg `-0.3241` n `12`; crypto_alt avg `0.9084` n `228`; crypto_major avg `1.0318` n `8`; equity avg `0.3001` n `69`; fx avg `0.0233` n `6`; index avg `0.2496` n `23`; metal avg `0.3449` n `18`; unknown avg `0.086` n `422`
- 4h: commodity avg `0.2938` n `12`; crypto_alt avg `0.0085` n `228`; crypto_major avg `-0.1614` n `8`; equity avg `-0.1032` n `69`; fx avg `-0.0333` n `6`; index avg `0.114` n `23`; metal avg `-0.1726` n `18`; unknown avg `0.3056` n `422`
- 24h: commodity avg `0.5326` n `12`; crypto_alt avg `-4.1658` n `228`; crypto_major avg `-5.3335` n `8`; equity avg `1.6419` n `69`; fx avg `0.0536` n `6`; index avg `1.0765` n `23`; metal avg `0.1127` n `18`; unknown avg `-1.3487` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
