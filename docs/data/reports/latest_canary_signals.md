# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T00:52:29.904793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `3.8062` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0619` n `12`; crypto_alt avg `-0.1022` n `228`; crypto_major avg `-0.104` n `8`; equity avg `-0.1133` n `74`; fx avg `0.0145` n `6`; index avg `-0.0132` n `23`; metal avg `-0.2892` n `18`; unknown avg `-0.1323` n `645`
- 1h: commodity avg `-0.1121` n `12`; crypto_alt avg `-0.2043` n `228`; crypto_major avg `-0.2033` n `8`; equity avg `0.239` n `74`; fx avg `-0.0361` n `6`; index avg `0.4247` n `23`; metal avg `-0.0019` n `18`; unknown avg `-0.1422` n `645`
- 4h: commodity avg `-0.9338` n `12`; crypto_alt avg `2.6172` n `228`; crypto_major avg `2.8724` n `8`; equity avg `1.4018` n `74`; fx avg `0.0262` n `6`; index avg `0.6318` n `23`; metal avg `1.7533` n `18`; unknown avg `2.4158` n `637`
- 24h: commodity avg `-0.8402` n `12`; crypto_alt avg `1.8905` n `228`; crypto_major avg `2.2403` n `8`; equity avg `1.59` n `74`; fx avg `-0.0196` n `6`; index avg `0.7542` n `23`; metal avg `1.6748` n `18`; unknown avg `1.7305` n `585`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
