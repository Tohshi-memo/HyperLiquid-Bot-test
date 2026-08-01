# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T08:22:29.552650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.0972` n `230`; crypto_major avg `0.0595` n `8`; equity avg `-0.0002` n `102`; fx avg `0.0186` n `6`; index avg `-0.0271` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.1726` n `781`
- 1h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.1093` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `0.1341` n `102`; fx avg `0.0212` n `6`; index avg `0.0189` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.0458` n `781`
- 4h: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.2538` n `230`; crypto_major avg `-0.1945` n `8`; equity avg `0.1055` n `102`; fx avg `0.0447` n `6`; index avg `-0.0194` n `25`; metal avg `0.0292` n `20`; unknown avg `-0.0216` n `765`
- 24h: commodity avg `0.911` n `12`; crypto_alt avg `-0.0007` n `230`; crypto_major avg `-1.2988` n `8`; equity avg `-2.477` n `102`; fx avg `0.0327` n `6`; index avg `-0.2855` n `25`; metal avg `-0.141` n `20`; unknown avg `4.8572` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
