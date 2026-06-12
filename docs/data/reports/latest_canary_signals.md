# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T19:07:29.832139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6376` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0742` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2665` n `12`; crypto_alt avg `-0.0312` n `228`; crypto_major avg `-0.2459` n `8`; equity avg `-0.1078` n `74`; fx avg `0.0005` n `6`; index avg `-0.0003` n `23`; metal avg `-0.0398` n `18`; unknown avg `-0.0021` n `643`
- 1h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.1799` n `228`; crypto_major avg `-0.0153` n `8`; equity avg `0.0137` n `74`; fx avg `0.005` n `6`; index avg `0.0945` n `23`; metal avg `0.106` n `18`; unknown avg `-0.2328` n `643`
- 4h: commodity avg `-0.0724` n `12`; crypto_alt avg `-1.2655` n `228`; crypto_major avg `-1.0653` n `8`; equity avg `-0.4585` n `74`; fx avg `0.0207` n `6`; index avg `0.0089` n `23`; metal avg `0.5723` n `18`; unknown avg `-0.1638` n `643`
- 24h: commodity avg `-1.2548` n `12`; crypto_alt avg `0.1376` n `228`; crypto_major avg `0.8564` n `8`; equity avg `0.8047` n `74`; fx avg `0.0432` n `6`; index avg `0.9677` n `23`; metal avg `1.1126` n `18`; unknown avg `40.9888` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
