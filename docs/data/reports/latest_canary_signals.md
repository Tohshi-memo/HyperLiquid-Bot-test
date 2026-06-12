# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T22:07:29.560519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.0248` n `228`; crypto_major avg `-0.0593` n `8`; equity avg `0.007` n `74`; fx avg `-0.0228` n `6`; index avg `0.101` n `23`; metal avg `-0.0039` n `18`; unknown avg `0.1642` n `643`
- 1h: commodity avg `0.1357` n `12`; crypto_alt avg `0.0097` n `228`; crypto_major avg `-0.1731` n `8`; equity avg `0.1028` n `74`; fx avg `-0.0113` n `6`; index avg `0.1371` n `23`; metal avg `-0.0541` n `18`; unknown avg `5.3025` n `643`
- 4h: commodity avg `-0.1384` n `12`; crypto_alt avg `-0.097` n `228`; crypto_major avg `-0.5366` n `8`; equity avg `-0.1318` n `74`; fx avg `-0.0528` n `6`; index avg `0.1885` n `23`; metal avg `0.1143` n `18`; unknown avg `0.2903` n `643`
- 24h: commodity avg `-0.2772` n `12`; crypto_alt avg `-0.6574` n `228`; crypto_major avg `-0.0848` n `8`; equity avg `-0.4242` n `74`; fx avg `-0.0301` n `6`; index avg `0.5155` n `23`; metal avg `-0.0523` n `18`; unknown avg `41.3178` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
