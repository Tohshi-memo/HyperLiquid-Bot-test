# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T01:33:35.023380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `12`; crypto_alt avg `0.0902` n `228`; crypto_major avg `0.0126` n `8`; equity avg `-0.0464` n `74`; fx avg `-0.0226` n `6`; index avg `-0.0498` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.3449` n `643`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `0.5034` n `228`; crypto_major avg `0.1626` n `8`; equity avg `-0.1806` n `74`; fx avg `-0.035` n `6`; index avg `-0.1097` n `23`; metal avg `0.0509` n `18`; unknown avg `-0.2174` n `643`
- 4h: commodity avg `-0.1282` n `12`; crypto_alt avg `0.4454` n `228`; crypto_major avg `-0.4165` n `8`; equity avg `0.048` n `74`; fx avg `0.0315` n `6`; index avg `0.1137` n `23`; metal avg `0.0623` n `18`; unknown avg `-0.2769` n `643`
- 24h: commodity avg `-0.6845` n `12`; crypto_alt avg `0.6245` n `228`; crypto_major avg `0.4598` n `8`; equity avg `-0.442` n `74`; fx avg `-0.0092` n `6`; index avg `0.5894` n `23`; metal avg `0.7768` n `18`; unknown avg `40.4824` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
