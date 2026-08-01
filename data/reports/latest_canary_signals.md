# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T23:07:36.174754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.024` n `230`; crypto_major avg `0.0234` n `8`; equity avg `-0.0188` n `102`; fx avg `0.0023` n `6`; index avg `0.0029` n `25`; metal avg `0.0005` n `20`; unknown avg `1.8904` n `782`
- 1h: commodity avg `0.094` n `12`; crypto_alt avg `-0.1118` n `230`; crypto_major avg `-0.0373` n `8`; equity avg `-0.1166` n `102`; fx avg `-0.0211` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0039` n `20`; unknown avg `1.8616` n `782`
- 4h: commodity avg `-0.1121` n `12`; crypto_alt avg `0.2746` n `230`; crypto_major avg `0.4403` n `8`; equity avg `0.2827` n `102`; fx avg `0.005` n `6`; index avg `0.0188` n `25`; metal avg `0.0487` n `20`; unknown avg `0.1791` n `782`
- 24h: commodity avg `-0.1931` n `12`; crypto_alt avg `-0.3648` n `230`; crypto_major avg `-0.7743` n `8`; equity avg `-0.1308` n `102`; fx avg `-0.05` n `6`; index avg `-0.0043` n `25`; metal avg `0.0426` n `20`; unknown avg `-0.0011` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
