# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T01:07:25.430701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.3439` n `228`; crypto_major avg `0.1188` n `8`; equity avg `-0.1523` n `74`; fx avg `-0.0057` n `6`; index avg `-0.0947` n `23`; metal avg `0.016` n `18`; unknown avg `-0.0158` n `643`
- 1h: commodity avg `0.1636` n `12`; crypto_alt avg `0.5115` n `228`; crypto_major avg `0.164` n `8`; equity avg `-0.0872` n `74`; fx avg `-0.0393` n `6`; index avg `-0.0789` n `23`; metal avg `0.0412` n `18`; unknown avg `0.026` n `643`
- 4h: commodity avg `0.021` n `12`; crypto_alt avg `0.5949` n `228`; crypto_major avg `-0.2264` n `8`; equity avg `0.1971` n `74`; fx avg `0.0321` n `6`; index avg `0.1337` n `23`; metal avg `0.032` n `18`; unknown avg `2.538` n `643`
- 24h: commodity avg `-0.695` n `12`; crypto_alt avg `0.1815` n `228`; crypto_major avg `0.1316` n `8`; equity avg `-0.7342` n `74`; fx avg `0.0169` n `6`; index avg `0.4329` n `23`; metal avg `0.7812` n `18`; unknown avg `41.0023` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
