# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T20:22:32.961687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `-0.0189` n `228`; crypto_major avg `-0.0755` n `8`; equity avg `0.0189` n `77`; fx avg `-0.0013` n `6`; index avg `-0.0447` n `23`; metal avg `-0.102` n `18`; unknown avg `-0.04` n `687`
- 1h: commodity avg `0.2033` n `12`; crypto_alt avg `0.2943` n `228`; crypto_major avg `0.0513` n `8`; equity avg `0.1706` n `77`; fx avg `-0.0079` n `6`; index avg `-0.0078` n `23`; metal avg `-0.1308` n `18`; unknown avg `0.0422` n `687`
- 4h: commodity avg `0.8127` n `12`; crypto_alt avg `-1.4825` n `228`; crypto_major avg `-0.553` n `8`; equity avg `-0.0685` n `77`; fx avg `-0.0362` n `6`; index avg `-0.1715` n `23`; metal avg `-0.6037` n `18`; unknown avg `3.5737` n `687`
- 24h: commodity avg `-0.3486` n `12`; crypto_alt avg `4.9704` n `228`; crypto_major avg `6.7264` n `8`; equity avg `3.0814` n `76`; fx avg `-0.0087` n `6`; index avg `1.2528` n `23`; metal avg `2.1092` n `18`; unknown avg `5.8942` n `527`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
