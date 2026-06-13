# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T08:22:31.218004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `-0.0458` n `228`; crypto_major avg `0.1328` n `8`; equity avg `-0.0311` n `74`; fx avg `0.0016` n `6`; index avg `-0.0063` n `23`; metal avg `0.0162` n `18`; unknown avg `0.1443` n `643`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `0.3227` n `228`; crypto_major avg `0.3044` n `8`; equity avg `0.0926` n `74`; fx avg `0.0047` n `6`; index avg `-0.0333` n `23`; metal avg `0.0423` n `18`; unknown avg `0.1677` n `643`
- 4h: commodity avg `-0.0537` n `12`; crypto_alt avg `0.9677` n `228`; crypto_major avg `0.5929` n `8`; equity avg `0.0968` n `74`; fx avg `0.0083` n `6`; index avg `-0.0216` n `23`; metal avg `0.1165` n `18`; unknown avg `-0.2949` n `619`
- 24h: commodity avg `0.5405` n `12`; crypto_alt avg `1.0428` n `228`; crypto_major avg `0.326` n `8`; equity avg `-0.5913` n `74`; fx avg `0.0561` n `6`; index avg `0.676` n `23`; metal avg `0.1425` n `18`; unknown avg `28.0558` n `619`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
