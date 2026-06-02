# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T11:52:23.133619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.75` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1192` n `12`; crypto_alt avg `0.2791` n `228`; crypto_major avg `0.059` n `8`; equity avg `0.0369` n `69`; fx avg `0.0067` n `6`; index avg `0.0605` n `23`; metal avg `0.059` n `18`; unknown avg `0.8059` n `422`
- 1h: commodity avg `0.069` n `12`; crypto_alt avg `0.0832` n `228`; crypto_major avg `0.0491` n `8`; equity avg `0.1649` n `69`; fx avg `0.0196` n `6`; index avg `0.1034` n `23`; metal avg `0.0821` n `18`; unknown avg `0.7912` n `422`
- 4h: commodity avg `0.0341` n `12`; crypto_alt avg `0.0742` n `228`; crypto_major avg `-0.2838` n `8`; equity avg `0.1937` n `69`; fx avg `-0.0012` n `6`; index avg `0.168` n `23`; metal avg `-0.2732` n `18`; unknown avg `-0.2374` n `422`
- 24h: commodity avg `-0.6829` n `12`; crypto_alt avg `0.2368` n `228`; crypto_major avg `-1.8299` n `8`; equity avg `0.7853` n `69`; fx avg `0.1501` n `6`; index avg `0.1248` n `23`; metal avg `0.7186` n `18`; unknown avg `0.9421` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
