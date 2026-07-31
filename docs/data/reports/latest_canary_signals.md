# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T22:22:32.329851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0792` n `12`; crypto_alt avg `0.0849` n `230`; crypto_major avg `0.0757` n `8`; equity avg `-0.0909` n `102`; fx avg `0.04` n `6`; index avg `-0.0032` n `25`; metal avg `0.0036` n `20`; unknown avg `0.5892` n `781`
- 1h: commodity avg `0.0489` n `12`; crypto_alt avg `-0.0926` n `230`; crypto_major avg `-0.0756` n `8`; equity avg `-0.2202` n `102`; fx avg `0.0386` n `6`; index avg `-0.0459` n `25`; metal avg `0.0179` n `20`; unknown avg `1.9063` n `781`
- 4h: commodity avg `0.5116` n `12`; crypto_alt avg `-0.5145` n `230`; crypto_major avg `-0.5489` n `8`; equity avg `-1.0434` n `102`; fx avg `-0.0496` n `6`; index avg `-0.1306` n `25`; metal avg `-0.0639` n `20`; unknown avg `1.7718` n `780`
- 24h: commodity avg `0.6992` n `12`; crypto_alt avg `-0.673` n `230`; crypto_major avg `-2.3214` n `8`; equity avg `-1.7217` n `102`; fx avg `0.1218` n `6`; index avg `-0.003` n `25`; metal avg `-0.435` n `20`; unknown avg `2.5396` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
