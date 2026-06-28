# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T06:22:25.137137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.2173` n `228`; crypto_major avg `-0.1532` n `8`; equity avg `-0.0053` n `88`; fx avg `0.0065` n `6`; index avg `-0.0252` n `23`; metal avg `-0.0007` n `20`; unknown avg `0.0203` n `764`
- 1h: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.3532` n `228`; crypto_major avg `-0.1998` n `8`; equity avg `0.0002` n `88`; fx avg `-0.0009` n `6`; index avg `-0.0127` n `23`; metal avg `0.0129` n `20`; unknown avg `-0.0895` n `732`
- 4h: commodity avg `-0.2509` n `12`; crypto_alt avg `-0.1356` n `228`; crypto_major avg `-0.3057` n `8`; equity avg `-0.0277` n `88`; fx avg `-0.0089` n `6`; index avg `-0.0298` n `23`; metal avg `-0.0034` n `20`; unknown avg `15.4494` n `706`
- 24h: commodity avg `0.2584` n `12`; crypto_alt avg `-0.7378` n `228`; crypto_major avg `-1.4193` n `8`; equity avg `0.0355` n `88`; fx avg `-0.0212` n `6`; index avg `-0.1216` n `23`; metal avg `-0.0484` n `20`; unknown avg `15.9612` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2185`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
