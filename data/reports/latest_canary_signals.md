# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T00:30:23.954762+00:00`
- Correlation status: `ready`
- Asset price records: `406`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0836` n `7`; crypto_alt avg `-0.2446` n `223`; crypto_major avg `-0.3063` n `7`; equity avg `-0.2816` n `47`; fx avg `-0.0288` n `4`; index avg `0.0106` n `6`; metal avg `0.1799` n `7`; unknown avg `-0.026` n `313`
- 1h: commodity avg `0.3542` n `7`; crypto_alt avg `0.0952` n `223`; crypto_major avg `-0.1293` n `7`; equity avg `-0.1124` n `47`; fx avg `-0.2553` n `4`; index avg `0.021` n `6`; metal avg `0.1755` n `7`; unknown avg `0.0808` n `313`
- 4h: commodity avg `-0.327` n `7`; crypto_alt avg `-0.1942` n `223`; crypto_major avg `-0.5586` n `7`; equity avg `0.3068` n `47`; fx avg `-0.1524` n `4`; index avg `0.2419` n `6`; metal avg `0.7189` n `7`; unknown avg `0.113` n `313`
- 24h: commodity avg `-1.4453` n `7`; crypto_alt avg `2.1825` n `223`; crypto_major avg `2.1154` n `7`; equity avg `2.6877` n `47`; fx avg `-0.1573` n `4`; index avg `1.8942` n `6`; metal avg `1.4938` n `7`; unknown avg `1.3702` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1924`, n `402`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1861`, n `402`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `402`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `402`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `402`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1074`, n `398`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.102`, n `402`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `402`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `402`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0998`, n `398`, weak_sample_signal
