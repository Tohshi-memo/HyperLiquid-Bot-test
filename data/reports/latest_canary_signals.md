# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T10:22:28.707300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0053` n `230`; crypto_major avg `0.0919` n `8`; equity avg `0.4426` n `107`; fx avg `-0.0043` n `6`; index avg `0.0294` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0219` n `781`
- 1h: commodity avg `-0.0943` n `12`; crypto_alt avg `0.0415` n `230`; crypto_major avg `0.1117` n `8`; equity avg `0.6714` n `107`; fx avg `-0.0196` n `6`; index avg `0.0859` n `25`; metal avg `0.0386` n `20`; unknown avg `0.0353` n `781`
- 4h: commodity avg `0.054` n `12`; crypto_alt avg `-0.3438` n `230`; crypto_major avg `-0.1626` n `8`; equity avg `0.4835` n `107`; fx avg `0.0468` n `6`; index avg `-0.0004` n `25`; metal avg `-0.004` n `20`; unknown avg `0.9247` n `781`
- 24h: commodity avg `0.3706` n `12`; crypto_alt avg `0.8266` n `230`; crypto_major avg `1.0258` n `8`; equity avg `4.3783` n `107`; fx avg `0.1032` n `6`; index avg `0.4384` n `25`; metal avg `0.178` n `20`; unknown avg `1.0444` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
