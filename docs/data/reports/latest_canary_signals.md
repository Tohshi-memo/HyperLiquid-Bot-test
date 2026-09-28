# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T02:52:35.561059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.3144` n `234`; crypto_major avg `-0.1073` n `8`; equity avg `-0.054` n `141`; fx avg `-0.0093` n `6`; index avg `-0.0074` n `26`; metal avg `-0.044` n `20`; unknown avg `0.1354` n `960`
- 1h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.4781` n `234`; crypto_major avg `-0.2695` n `8`; equity avg `-0.2867` n `141`; fx avg `-0.0381` n `6`; index avg `-0.0431` n `26`; metal avg `-0.1422` n `20`; unknown avg `314.4157` n `958`
- 4h: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.9935` n `234`; crypto_major avg `-0.8534` n `8`; equity avg `-1.2265` n `141`; fx avg `0.0685` n `6`; index avg `-0.0756` n `26`; metal avg `-0.5148` n `20`; unknown avg `160.7962` n `942`
- 24h: commodity avg `-0.4375` n `12`; crypto_alt avg `-0.6955` n `234`; crypto_major avg `-1.3609` n `8`; equity avg `-1.3596` n `141`; fx avg `0.0596` n `6`; index avg `-0.1403` n `26`; metal avg `-0.7171` n `20`; unknown avg `12.0831` n `817`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
