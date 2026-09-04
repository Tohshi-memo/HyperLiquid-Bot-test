# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T01:20:27.667869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `0.0432` n `232`; crypto_major avg `0.0208` n `8`; equity avg `-0.0527` n `133`; fx avg `0.0043` n `6`; index avg `-0.0047` n `26`; metal avg `0.0397` n `20`; unknown avg `0.0363` n `793`
- 1h: commodity avg `0.0456` n `12`; crypto_alt avg `-0.4184` n `232`; crypto_major avg `-0.2951` n `8`; equity avg `0.05` n `133`; fx avg `0.0349` n `6`; index avg `0.0058` n `26`; metal avg `-0.0279` n `20`; unknown avg `3.1361` n `784`
- 4h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.6699` n `232`; crypto_major avg `-0.4646` n `8`; equity avg `0.2539` n `133`; fx avg `0.0398` n `6`; index avg `0.0136` n `26`; metal avg `-0.0334` n `20`; unknown avg `2.5086` n `784`
- 24h: commodity avg `-0.1398` n `12`; crypto_alt avg `3.1111` n `232`; crypto_major avg `4.5709` n `8`; equity avg `1.4972` n `133`; fx avg `-0.1499` n `6`; index avg `0.1992` n `26`; metal avg `0.7151` n `20`; unknown avg `1.1306` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
