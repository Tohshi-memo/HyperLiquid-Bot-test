# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T16:22:17.983679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2527` n `12`; crypto_alt avg `-0.1198` n `228`; crypto_major avg `0.0054` n `8`; equity avg `-0.0479` n `69`; fx avg `-0.0015` n `6`; index avg `0.0043` n `23`; metal avg `0.0008` n `18`; unknown avg `0.8393` n `421`
- 1h: commodity avg `-0.6067` n `12`; crypto_alt avg `0.0139` n `228`; crypto_major avg `0.0422` n `8`; equity avg `-0.1449` n `69`; fx avg `-0.0108` n `6`; index avg `-0.1641` n `23`; metal avg `0.0438` n `18`; unknown avg `1.3575` n `421`
- 4h: commodity avg `-0.5361` n `12`; crypto_alt avg `0.0438` n `228`; crypto_major avg `0.5749` n `8`; equity avg `0.0833` n `69`; fx avg `0.0129` n `6`; index avg `-0.0399` n `23`; metal avg `0.0147` n `18`; unknown avg `0.4509` n `421`
- 24h: commodity avg `-0.3658` n `12`; crypto_alt avg `0.7709` n `228`; crypto_major avg `1.8109` n `8`; equity avg `0.7793` n `69`; fx avg `0.0143` n `6`; index avg `0.0753` n `23`; metal avg `-0.1782` n `18`; unknown avg `1.1902` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
