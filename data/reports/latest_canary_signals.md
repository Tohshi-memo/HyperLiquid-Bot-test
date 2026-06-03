# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T10:07:25.983648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.3105` n `12`; crypto_alt avg `0.2201` n `228`; crypto_major avg `0.1846` n `8`; equity avg `-0.0189` n `72`; fx avg `-0.0188` n `6`; index avg `0.0405` n `23`; metal avg `0.3632` n `18`; unknown avg `-0.0519` n `420`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `0.3294` n `228`; crypto_major avg `0.3545` n `8`; equity avg `-0.1409` n `72`; fx avg `-0.0062` n `6`; index avg `0.0403` n `23`; metal avg `0.1726` n `18`; unknown avg `-0.2081` n `420`
- 4h: commodity avg `0.617` n `12`; crypto_alt avg `0.6208` n `228`; crypto_major avg `0.3376` n `8`; equity avg `-0.4166` n `72`; fx avg `0.0279` n `6`; index avg `0.0081` n `23`; metal avg `-0.0163` n `18`; unknown avg `0.5405` n `420`
- 24h: commodity avg `1.7799` n `12`; crypto_alt avg `-0.3219` n `228`; crypto_major avg `-2.6268` n `8`; equity avg `0.3572` n `72`; fx avg `0.0444` n `6`; index avg `0.8764` n `23`; metal avg `-1.2853` n `18`; unknown avg `0.7888` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
