# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T19:45:49.753156+00:00`
- Correlation status: `ready`
- Asset price records: `387`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0297` n `7`; crypto_alt avg `0.0372` n `223`; crypto_major avg `0.0356` n `7`; equity avg `0.1741` n `47`; fx avg `0.0197` n `4`; index avg `-0.0043` n `6`; metal avg `-0.0689` n `7`; unknown avg `0.0405` n `313`
- 1h: commodity avg `-0.0231` n `7`; crypto_alt avg `0.2748` n `223`; crypto_major avg `0.1823` n `7`; equity avg `0.1198` n `47`; fx avg `0.0327` n `4`; index avg `0.0063` n `6`; metal avg `-0.2139` n `7`; unknown avg `1.2056` n `313`
- 4h: commodity avg `0.0558` n `7`; crypto_alt avg `0.5184` n `223`; crypto_major avg `0.2323` n `7`; equity avg `-0.0362` n `47`; fx avg `0.0285` n `4`; index avg `0.2141` n `6`; metal avg `-0.5736` n `7`; unknown avg `1.1488` n `313`
- 24h: commodity avg `-1.2483` n `7`; crypto_alt avg `1.9196` n `223`; crypto_major avg `2.4619` n `7`; equity avg `1.8442` n `47`; fx avg `-0.0015` n `4`; index avg `1.5235` n `6`; metal avg `0.6207` n `7`; unknown avg `2.2059` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `383`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2001`, n `383`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `383`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `383`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1137`, n `379`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `383`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `383`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `379`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `383`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `383`, weak_sample_signal
