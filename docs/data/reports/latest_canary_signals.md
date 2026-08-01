# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T09:22:27.856745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `-0.0694` n `230`; crypto_major avg `-0.0535` n `8`; equity avg `-0.0459` n `102`; fx avg `0.0093` n `6`; index avg `-0.0154` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.0008` n `781`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.0289` n `230`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0983` n `102`; fx avg `0.0002` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0147` n `20`; unknown avg `-0.012` n `781`
- 4h: commodity avg `0.0139` n `12`; crypto_alt avg `-0.2292` n `230`; crypto_major avg `-0.1704` n `8`; equity avg `-0.0034` n `102`; fx avg `0.0128` n `6`; index avg `0.0075` n `25`; metal avg `0.0152` n `20`; unknown avg `-0.0131` n `765`
- 24h: commodity avg `0.674` n `12`; crypto_alt avg `0.52` n `230`; crypto_major avg `-0.9862` n `8`; equity avg `-2.803` n `102`; fx avg `0.0127` n `6`; index avg `-0.3576` n `25`; metal avg `-0.0316` n `20`; unknown avg `4.8644` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1034`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0685`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `669`, weak_sample_signal
