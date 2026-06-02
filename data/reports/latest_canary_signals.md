# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T07:37:23.127983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.74` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.4204` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0223` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8578` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1842` n `12`; crypto_alt avg `0.1944` n `228`; crypto_major avg `0.0623` n `8`; equity avg `0.021` n `69`; fx avg `0.013` n `6`; index avg `-0.0003` n `23`; metal avg `-0.058` n `18`; unknown avg `0.686` n `422`
- 1h: commodity avg `0.267` n `12`; crypto_alt avg `-0.0393` n `228`; crypto_major avg `-0.0143` n `8`; equity avg `-0.0207` n `69`; fx avg `0.0102` n `6`; index avg `0.0971` n `23`; metal avg `0.079` n `18`; unknown avg `0.6895` n `422`
- 4h: commodity avg `0.0079` n `12`; crypto_alt avg `-1.0758` n `228`; crypto_major avg `-1.3137` n `8`; equity avg `0.7086` n `69`; fx avg `0.0708` n `6`; index avg `0.5441` n `23`; metal avg `1.1067` n `18`; unknown avg `0.3518` n `412`
- 24h: commodity avg `-0.9565` n `12`; crypto_alt avg `-0.0909` n `228`; crypto_major avg `-1.1195` n `8`; equity avg `0.2499` n `69`; fx avg `0.1525` n `6`; index avg `-0.6635` n `23`; metal avg `1.1402` n `18`; unknown avg `1.3329` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
