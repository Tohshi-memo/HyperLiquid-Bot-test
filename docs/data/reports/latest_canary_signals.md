# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T16:37:28.242581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.6064` n `228`; crypto_major avg `-0.5173` n `8`; equity avg `-0.0403` n `88`; fx avg `0.0` n `6`; index avg `0.0096` n `23`; metal avg `-0.0113` n `20`; unknown avg `0.2149` n `764`
- 1h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.6417` n `228`; crypto_major avg `-0.5481` n `8`; equity avg `-0.0617` n `88`; fx avg `0.0` n `6`; index avg `-0.0218` n `23`; metal avg `-0.0072` n `20`; unknown avg `-0.4114` n `764`
- 4h: commodity avg `0.1419` n `12`; crypto_alt avg `-0.5832` n `228`; crypto_major avg `-0.7073` n `8`; equity avg `-0.0397` n `88`; fx avg `-0.0039` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0666` n `20`; unknown avg `0.2487` n `764`
- 24h: commodity avg `0.3473` n `12`; crypto_alt avg `-1.4961` n `228`; crypto_major avg `-2.1438` n `8`; equity avg `-0.0144` n `88`; fx avg `-0.0047` n `6`; index avg `-0.0464` n `23`; metal avg `-0.0813` n `20`; unknown avg `14.7715` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
