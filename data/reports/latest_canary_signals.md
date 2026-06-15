# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T21:07:31.609056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.35` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.1398` n `228`; crypto_major avg `-0.1817` n `8`; equity avg `-0.0091` n `77`; fx avg `0.0247` n `6`; index avg `0.0207` n `23`; metal avg `0.0307` n `18`; unknown avg `-0.125` n `679`
- 1h: commodity avg `-0.2011` n `12`; crypto_alt avg `-0.3951` n `228`; crypto_major avg `-0.4862` n `8`; equity avg `-0.0785` n `77`; fx avg `0.0163` n `6`; index avg `-0.0749` n `23`; metal avg `-0.174` n `18`; unknown avg `0.0524` n `679`
- 4h: commodity avg `0.2929` n `12`; crypto_alt avg `-1.0647` n `228`; crypto_major avg `-0.8676` n `8`; equity avg `-0.0581` n `77`; fx avg `-0.0227` n `6`; index avg `-0.0765` n `23`; metal avg `-0.2764` n `18`; unknown avg `-0.01` n `679`
- 24h: commodity avg `-0.4392` n `12`; crypto_alt avg `4.1759` n `228`; crypto_major avg `6.0662` n `8`; equity avg `2.834` n `76`; fx avg `0.0342` n `6`; index avg `1.2174` n `23`; metal avg `1.9471` n `18`; unknown avg `1.9718` n `519`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
