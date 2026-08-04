# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T05:07:27.958300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1401` n `230`; crypto_major avg `-0.1702` n `8`; equity avg `-0.1421` n `107`; fx avg `-0.0085` n `6`; index avg `-0.0208` n `25`; metal avg `-0.0392` n `20`; unknown avg `0.332` n `781`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `0.0882` n `230`; crypto_major avg `0.1941` n `8`; equity avg `-0.0063` n `107`; fx avg `-0.0238` n `6`; index avg `0.0118` n `25`; metal avg `0.0288` n `20`; unknown avg `6.8455` n `781`
- 4h: commodity avg `0.0985` n `12`; crypto_alt avg `0.4674` n `230`; crypto_major avg `0.6604` n `8`; equity avg `0.6654` n `107`; fx avg `0.0904` n `6`; index avg `0.1193` n `25`; metal avg `0.2495` n `20`; unknown avg `3.9319` n `780`
- 24h: commodity avg `0.3731` n `12`; crypto_alt avg `1.2573` n `230`; crypto_major avg `1.3456` n `8`; equity avg `1.6931` n `107`; fx avg `0.0341` n `6`; index avg `0.1286` n `25`; metal avg `0.0096` n `20`; unknown avg `0.2144` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
