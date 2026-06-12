# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T05:37:26.432973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2204` n `12`; crypto_alt avg `-0.1598` n `228`; crypto_major avg `-0.1146` n `8`; equity avg `-0.2542` n `74`; fx avg `0.0014` n `6`; index avg `-0.1842` n `23`; metal avg `-0.2047` n `18`; unknown avg `-0.4503` n `557`
- 1h: commodity avg `-0.0674` n `12`; crypto_alt avg `-0.4793` n `228`; crypto_major avg `-0.3934` n `8`; equity avg `-0.3064` n `74`; fx avg `-0.016` n `6`; index avg `-0.1824` n `23`; metal avg `-0.3678` n `18`; unknown avg `-0.4324` n `557`
- 4h: commodity avg `-0.3216` n `12`; crypto_alt avg `0.1054` n `228`; crypto_major avg `0.2792` n `8`; equity avg `0.0728` n `74`; fx avg `0.0152` n `6`; index avg `0.0393` n `23`; metal avg `-0.0361` n `18`; unknown avg `1.9266` n `557`
- 24h: commodity avg `-2.3213` n `12`; crypto_alt avg `1.4816` n `228`; crypto_major avg `2.0913` n `8`; equity avg `3.3944` n `74`; fx avg `0.0064` n `6`; index avg `1.7877` n `23`; metal avg `2.3649` n `18`; unknown avg `1.6871` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
