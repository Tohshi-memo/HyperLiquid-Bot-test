# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T10:07:26.794515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.034` n `230`; crypto_major avg `-0.1087` n `8`; equity avg `-0.0176` n `108`; fx avg `0.0089` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0355` n `20`; unknown avg `-0.0032` n `781`
- 1h: commodity avg `0.0976` n `12`; crypto_alt avg `-0.0004` n `230`; crypto_major avg `-0.1576` n `8`; equity avg `0.0228` n `108`; fx avg `0.0131` n `6`; index avg `0.0034` n `25`; metal avg `-0.0851` n `20`; unknown avg `0.6694` n `781`
- 4h: commodity avg `0.2822` n `12`; crypto_alt avg `-0.123` n `230`; crypto_major avg `-0.1111` n `8`; equity avg `-0.9366` n `108`; fx avg `0.0579` n `6`; index avg `-0.1429` n `25`; metal avg `-0.1254` n `20`; unknown avg `0.7468` n `781`
- 24h: commodity avg `-1.2042` n `12`; crypto_alt avg `0.682` n `230`; crypto_major avg `0.9299` n `8`; equity avg `2.7172` n `108`; fx avg `-0.0079` n `6`; index avg `0.6344` n `25`; metal avg `1.0859` n `20`; unknown avg `0.1477` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
