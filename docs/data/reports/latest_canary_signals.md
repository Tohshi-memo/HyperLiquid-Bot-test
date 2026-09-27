# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T23:07:26.323898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0322` n `12`; crypto_alt avg `0.0207` n `234`; crypto_major avg `-0.0131` n `8`; equity avg `0.023` n `141`; fx avg `-0.0109` n `6`; index avg `0.0051` n `26`; metal avg `0.0144` n `20`; unknown avg `2.2045` n `960`
- 1h: commodity avg `0.0004` n `12`; crypto_alt avg `0.0533` n `234`; crypto_major avg `-0.1589` n `8`; equity avg `-0.1476` n `141`; fx avg `0.0007` n `6`; index avg `-0.0457` n `26`; metal avg `-0.0761` n `20`; unknown avg `2.9891` n `934`
- 4h: commodity avg `-0.3148` n `12`; crypto_alt avg `-0.6432` n `234`; crypto_major avg `-0.8371` n `8`; equity avg `-0.3563` n `141`; fx avg `-0.0215` n `6`; index avg `-0.0935` n `26`; metal avg `-0.1795` n `20`; unknown avg `2.3214` n `860`
- 24h: commodity avg `-0.525` n `12`; crypto_alt avg `0.2515` n `234`; crypto_major avg `-0.3655` n `8`; equity avg `-0.0289` n `141`; fx avg `-0.0258` n `6`; index avg `-0.0545` n `26`; metal avg `-0.1901` n `20`; unknown avg `4.8753` n `827`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
