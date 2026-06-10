# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T20:37:27.399624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0561` n `12`; crypto_alt avg `-0.0679` n `228`; crypto_major avg `-0.1276` n `8`; equity avg `-0.1009` n `74`; fx avg `-0.008` n `6`; index avg `-0.0484` n `23`; metal avg `0.0043` n `18`; unknown avg `0.0034` n `550`
- 1h: commodity avg `0.2068` n `12`; crypto_alt avg `-0.348` n `228`; crypto_major avg `-0.3757` n `8`; equity avg `-0.683` n `74`; fx avg `-0.0226` n `6`; index avg `-0.254` n `23`; metal avg `-0.2678` n `18`; unknown avg `-0.1563` n `550`
- 4h: commodity avg `-0.1533` n `12`; crypto_alt avg `-1.8636` n `228`; crypto_major avg `-1.6545` n `8`; equity avg `-1.6981` n `74`; fx avg `-0.0417` n `6`; index avg `-1.0196` n `23`; metal avg `-1.4695` n `18`; unknown avg `-0.1842` n `548`
- 24h: commodity avg `1.3065` n `12`; crypto_alt avg `-2.3806` n `228`; crypto_major avg `-2.7372` n `8`; equity avg `-2.2672` n `74`; fx avg `-0.0302` n `6`; index avg `-1.7659` n `23`; metal avg `-2.5194` n `18`; unknown avg `-0.5404` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
