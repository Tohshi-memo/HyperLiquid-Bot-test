# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T19:22:28.807072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.1242` n `234`; crypto_major avg `0.0422` n `8`; equity avg `0.0147` n `141`; fx avg `-0.0019` n `6`; index avg `0.0024` n `26`; metal avg `0.0043` n `20`; unknown avg `0.5316` n `936`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.1465` n `234`; crypto_major avg `0.0336` n `8`; equity avg `0.0089` n `141`; fx avg `0.0015` n `6`; index avg `-0.0035` n `26`; metal avg `0.0086` n `20`; unknown avg `1.9197` n `934`
- 4h: commodity avg `-0.0675` n `12`; crypto_alt avg `1.4411` n `234`; crypto_major avg `0.546` n `8`; equity avg `0.1563` n `141`; fx avg `0.0076` n `6`; index avg `0.0198` n `26`; metal avg `0.0155` n `20`; unknown avg `4.3855` n `928`
- 24h: commodity avg `-0.1407` n `12`; crypto_alt avg `0.8351` n `234`; crypto_major avg `0.6322` n `8`; equity avg `0.3943` n `141`; fx avg `-0.0092` n `6`; index avg `0.0351` n `26`; metal avg `-0.0042` n `20`; unknown avg `121.6321` n `871`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
