# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T00:52:27.930176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-0.019` n `228`; crypto_major avg `0.0399` n `8`; equity avg `0.0348` n `74`; fx avg `-0.0292` n `6`; index avg `0.0188` n `23`; metal avg `0.0438` n `18`; unknown avg `-0.0116` n `643`
- 1h: commodity avg `0.0956` n `12`; crypto_alt avg `0.3366` n `228`; crypto_major avg `0.0623` n `8`; equity avg `0.129` n `74`; fx avg `-0.0074` n `6`; index avg `0.1281` n `23`; metal avg `0.0566` n `18`; unknown avg `-0.025` n `643`
- 4h: commodity avg `-0.1325` n `12`; crypto_alt avg `0.2672` n `228`; crypto_major avg `-0.3004` n `8`; equity avg `0.3327` n `74`; fx avg `0.0014` n `6`; index avg `0.2016` n `23`; metal avg `0.0089` n `18`; unknown avg `-0.3556` n `643`
- 24h: commodity avg `-0.6077` n `12`; crypto_alt avg `-0.4718` n `228`; crypto_major avg `-0.2608` n `8`; equity avg `-0.9316` n `74`; fx avg `0.0228` n `6`; index avg `0.4611` n `23`; metal avg `0.4456` n `18`; unknown avg `40.9467` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
