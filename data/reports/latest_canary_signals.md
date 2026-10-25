# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T03:52:26.843367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.084` n `237`; crypto_major avg `0.0185` n `8`; equity avg `-0.0038` n `152`; fx avg `0.0012` n `6`; index avg `0.0019` n `26`; metal avg `-0.0027` n `20`; unknown avg `1.5545` n `1229`
- 1h: commodity avg `-0.0135` n `13`; crypto_alt avg `0.1085` n `237`; crypto_major avg `-0.0152` n `8`; equity avg `0.0723` n `152`; fx avg `0.0009` n `6`; index avg `0.0172` n `26`; metal avg `0.0004` n `20`; unknown avg `1.871` n `1223`
- 4h: commodity avg `-0.0321` n `13`; crypto_alt avg `-0.4311` n `237`; crypto_major avg `0.2348` n `8`; equity avg `0.1008` n `152`; fx avg `-0.0025` n `6`; index avg `0.0219` n `26`; metal avg `-0.0035` n `20`; unknown avg `1.8735` n `1207`
- 24h: commodity avg `0.1726` n `13`; crypto_alt avg `-1.1395` n `237`; crypto_major avg `0.0082` n `8`; equity avg `-0.0006` n `152`; fx avg `-0.0313` n `6`; index avg `0.0016` n `26`; metal avg `-0.0786` n `20`; unknown avg `12.4912` n `1062`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
