# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T12:07:31.565134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.0717` n `230`; crypto_major avg `0.0399` n `8`; equity avg `-0.1243` n `108`; fx avg `0.0001` n `6`; index avg `-0.0213` n `25`; metal avg `0.0417` n `20`; unknown avg `0.0199` n `782`
- 1h: commodity avg `-0.1085` n `12`; crypto_alt avg `-0.104` n `230`; crypto_major avg `-0.0727` n `8`; equity avg `-0.1322` n `108`; fx avg `0.004` n `6`; index avg `0.0243` n `25`; metal avg `0.2151` n `20`; unknown avg `-0.0599` n `782`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `-0.2539` n `230`; crypto_major avg `-0.2068` n `8`; equity avg `-0.6759` n `108`; fx avg `-0.0158` n `6`; index avg `-0.0391` n `25`; metal avg `0.0753` n `20`; unknown avg `0.5621` n `781`
- 24h: commodity avg `-0.4279` n `12`; crypto_alt avg `0.4943` n `230`; crypto_major avg `0.1656` n `8`; equity avg `1.6015` n `108`; fx avg `0.087` n `6`; index avg `0.516` n `25`; metal avg `0.9872` n `20`; unknown avg `0.0099` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
