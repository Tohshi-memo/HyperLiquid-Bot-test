# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T03:07:37.502128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.0433` n `230`; crypto_major avg `-0.0748` n `8`; equity avg `-0.0515` n `107`; fx avg `0.0181` n `6`; index avg `-0.0292` n `25`; metal avg `-0.034` n `20`; unknown avg `-0.0587` n `780`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `0.0664` n `230`; crypto_major avg `0.0035` n `8`; equity avg `-0.1281` n `107`; fx avg `0.0684` n `6`; index avg `-0.0489` n `25`; metal avg `0.0723` n `20`; unknown avg `-0.1563` n `780`
- 4h: commodity avg `0.1924` n `12`; crypto_alt avg `0.276` n `230`; crypto_major avg `0.3478` n `8`; equity avg `-0.3377` n `107`; fx avg `0.0251` n `6`; index avg `-0.0643` n `25`; metal avg `0.1805` n `20`; unknown avg `-0.3113` n `780`
- 24h: commodity avg `0.2729` n `12`; crypto_alt avg `1.1712` n `230`; crypto_major avg `1.0011` n `8`; equity avg `1.4023` n `107`; fx avg `0.0215` n `6`; index avg `0.0924` n `25`; metal avg `-0.018` n `20`; unknown avg `0.223` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
