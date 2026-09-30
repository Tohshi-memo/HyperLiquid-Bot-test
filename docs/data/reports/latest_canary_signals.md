# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T06:52:32.605732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `-0.0829` n `234`; crypto_major avg `-0.0695` n `8`; equity avg `0.0158` n `142`; fx avg `-0.0066` n `6`; index avg `0.0034` n `26`; metal avg `0.0388` n `20`; unknown avg `1.463` n `963`
- 1h: commodity avg `0.0196` n `12`; crypto_alt avg `-0.7744` n `234`; crypto_major avg `-0.537` n `8`; equity avg `-0.1049` n `142`; fx avg `0.0108` n `6`; index avg `-0.0162` n `26`; metal avg `0.0989` n `20`; unknown avg `1.2016` n `931`
- 4h: commodity avg `0.0476` n `12`; crypto_alt avg `-0.63` n `234`; crypto_major avg `-0.6825` n `8`; equity avg `-0.1156` n `142`; fx avg `0.0583` n `6`; index avg `0.0081` n `26`; metal avg `0.0263` n `20`; unknown avg `2.0243` n `925`
- 24h: commodity avg `-0.879` n `12`; crypto_alt avg `-0.0437` n `234`; crypto_major avg `-1.1579` n `8`; equity avg `0.4192` n `142`; fx avg `-0.1024` n `6`; index avg `0.0643` n `26`; metal avg `0.2491` n `20`; unknown avg `2860.6553` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
