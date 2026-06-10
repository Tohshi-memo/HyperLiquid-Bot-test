# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T21:52:31.989929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.6633` n `228`; crypto_major avg `-0.5768` n `8`; equity avg `-0.1364` n `74`; fx avg `-0.0126` n `6`; index avg `-0.0203` n `23`; metal avg `-0.0159` n `18`; unknown avg `-0.0156` n `550`
- 1h: commodity avg `0.2787` n `12`; crypto_alt avg `-1.0946` n `228`; crypto_major avg `-0.8452` n `8`; equity avg `-0.1004` n `74`; fx avg `-0.0205` n `6`; index avg `0.0483` n `23`; metal avg `0.0346` n `18`; unknown avg `-0.143` n `550`
- 4h: commodity avg `0.0552` n `12`; crypto_alt avg `-2.0768` n `228`; crypto_major avg `-1.5946` n `8`; equity avg `-1.5276` n `74`; fx avg `-0.03` n `6`; index avg `-0.68` n `23`; metal avg `-1.0309` n `18`; unknown avg `-0.0566` n `550`
- 24h: commodity avg `1.5101` n `12`; crypto_alt avg `-3.0423` n `228`; crypto_major avg `-3.0608` n `8`; equity avg `-2.1494` n `74`; fx avg `0.0235` n `6`; index avg `-1.6839` n `23`; metal avg `-2.5356` n `18`; unknown avg `-0.5583` n `537`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
