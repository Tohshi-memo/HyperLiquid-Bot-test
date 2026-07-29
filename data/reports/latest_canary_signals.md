# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T14:56:30.906823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.72` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6784` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0461` n `12`; crypto_alt avg `-0.0742` n `230`; crypto_major avg `0.0318` n `8`; equity avg `-0.308` n `102`; fx avg `-0.0178` n `6`; index avg `-0.1341` n `25`; metal avg `-0.0349` n `20`; unknown avg `-0.023` n `778`
- 1h: commodity avg `0.1224` n `12`; crypto_alt avg `-0.3874` n `230`; crypto_major avg `-0.3008` n `8`; equity avg `-0.9951` n `102`; fx avg `0.0027` n `6`; index avg `-0.2276` n `25`; metal avg `-0.0441` n `20`; unknown avg `-0.0291` n `777`
- 4h: commodity avg `0.4704` n `12`; crypto_alt avg `-0.5217` n `230`; crypto_major avg `-0.4699` n `8`; equity avg `-2.1483` n `102`; fx avg `0.0106` n `6`; index avg `-0.3547` n `25`; metal avg `-0.1582` n `20`; unknown avg `0.4787` n `777`
- 24h: commodity avg `0.8039` n `12`; crypto_alt avg `-1.8407` n `230`; crypto_major avg `0.3525` n `8`; equity avg `-1.3625` n `102`; fx avg `-0.0305` n `6`; index avg `-0.4373` n `25`; metal avg `-0.218` n `20`; unknown avg `-0.1674` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
