# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T12:46:08.579648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.0853` n `231`; crypto_major avg `-0.0054` n `8`; equity avg `-0.0824` n `122`; fx avg `0.0037` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0315` n `20`; unknown avg `0.0843` n `797`
- 1h: commodity avg `-0.1131` n `12`; crypto_alt avg `-0.0944` n `231`; crypto_major avg `-0.2086` n `8`; equity avg `-0.3825` n `122`; fx avg `-0.0188` n `6`; index avg `-0.04` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0422` n `797`
- 4h: commodity avg `0.1348` n `12`; crypto_alt avg `-0.3569` n `231`; crypto_major avg `-0.3776` n `8`; equity avg `-0.4696` n `122`; fx avg `-0.0155` n `6`; index avg `-0.0462` n `25`; metal avg `-0.0596` n `20`; unknown avg `-0.1531` n `797`
- 24h: commodity avg `-0.0894` n `12`; crypto_alt avg `-1.3846` n `231`; crypto_major avg `-1.2949` n `8`; equity avg `-0.1375` n `122`; fx avg `-0.0341` n `6`; index avg `-0.0568` n `25`; metal avg `0.0761` n `20`; unknown avg `0.566` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
