# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T03:22:26.994043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.2867` n `230`; crypto_major avg `-0.2776` n `8`; equity avg `-0.1383` n `92`; fx avg `-0.0037` n `6`; index avg `-0.0219` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.1274` n `766`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `-1.0084` n `230`; crypto_major avg `-0.8925` n `8`; equity avg `-0.6644` n `92`; fx avg `0.0202` n `6`; index avg `-0.1153` n `25`; metal avg `-0.1754` n `20`; unknown avg `0.331` n `766`
- 4h: commodity avg `0.1061` n `12`; crypto_alt avg `-1.1346` n `230`; crypto_major avg `-0.9676` n `8`; equity avg `-1.8224` n `92`; fx avg `0.0959` n `6`; index avg `-0.3915` n `25`; metal avg `-0.1771` n `20`; unknown avg `0.3596` n `766`
- 24h: commodity avg `0.1556` n `12`; crypto_alt avg `-2.2545` n `230`; crypto_major avg `-1.2869` n `8`; equity avg `-2.23` n `92`; fx avg `0.0357` n `6`; index avg `-0.432` n `25`; metal avg `-0.4959` n `20`; unknown avg `-0.0267` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1775`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.115`, n `670`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.113`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1037`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0896`, n `670`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0888`, n `670`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `670`, weak_sample_signal
