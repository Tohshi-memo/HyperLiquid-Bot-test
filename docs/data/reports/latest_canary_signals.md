# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T23:20:31.167911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1662` n `12`; crypto_alt avg `0.0025` n `228`; crypto_major avg `0.0832` n `8`; equity avg `0.0637` n `74`; fx avg `-0.0089` n `6`; index avg `0.0672` n `23`; metal avg `-0.0346` n `18`; unknown avg `-0.1014` n `556`
- 1h: commodity avg `0.0956` n `12`; crypto_alt avg `-0.3322` n `228`; crypto_major avg `-0.21` n `8`; equity avg `0.094` n `74`; fx avg `0.029` n `6`; index avg `-0.0032` n `23`; metal avg `0.2835` n `18`; unknown avg `-0.0908` n `556`
- 4h: commodity avg `-0.7221` n `12`; crypto_alt avg `-0.0453` n `228`; crypto_major avg `-0.2153` n `8`; equity avg `0.8592` n `74`; fx avg `0.0251` n `6`; index avg `0.712` n `23`; metal avg `0.5329` n `18`; unknown avg `-0.4231` n `556`
- 24h: commodity avg `-2.808` n `12`; crypto_alt avg `4.3005` n `228`; crypto_major avg `4.213` n `8`; equity avg `5.3713` n `74`; fx avg `0.1472` n `6`; index avg `2.8842` n `23`; metal avg `4.6226` n `18`; unknown avg `2.4468` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
