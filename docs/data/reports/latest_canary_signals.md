# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T16:22:36.644125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `-0.0675` n `235`; crypto_major avg `-0.1213` n `8`; equity avg `-0.0295` n `150`; fx avg `-0.016` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0416` n `20`; unknown avg `0.1384` n `1084`
- 1h: commodity avg `-0.1063` n `13`; crypto_alt avg `0.786` n `235`; crypto_major avg `0.1035` n `8`; equity avg `-0.0517` n `150`; fx avg `-0.0185` n `6`; index avg `0.0013` n `26`; metal avg `-0.024` n `20`; unknown avg `1.1769` n `1020`
- 4h: commodity avg `0.3776` n `13`; crypto_alt avg `0.1474` n `235`; crypto_major avg `-0.5819` n `8`; equity avg `-0.5672` n `150`; fx avg `-0.0012` n `6`; index avg `-0.0684` n `26`; metal avg `0.0181` n `20`; unknown avg `0.2671` n `996`
- 24h: commodity avg `0.1986` n `13`; crypto_alt avg `2.701` n `235`; crypto_major avg `1.382` n `8`; equity avg `-0.1652` n `150`; fx avg `0.0155` n `6`; index avg `-0.0054` n `26`; metal avg `0.6692` n `20`; unknown avg `1.3581` n `915`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
