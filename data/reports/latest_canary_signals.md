# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T04:22:32.748645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `0.1312` n `230`; crypto_major avg `0.2041` n `8`; equity avg `-0.0084` n `107`; fx avg `0.0106` n `6`; index avg `0.0093` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0386` n `781`
- 1h: commodity avg `0.0461` n `12`; crypto_alt avg `0.194` n `230`; crypto_major avg `0.267` n `8`; equity avg `0.2033` n `107`; fx avg `0.0451` n `6`; index avg `0.0167` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.1301` n `781`
- 4h: commodity avg `0.0943` n `12`; crypto_alt avg `0.3503` n `230`; crypto_major avg `0.5247` n `8`; equity avg `0.0427` n `107`; fx avg `0.0317` n `6`; index avg `-0.0526` n `25`; metal avg `0.1585` n `20`; unknown avg `-0.2901` n `780`
- 24h: commodity avg `0.342` n `12`; crypto_alt avg `1.1436` n `230`; crypto_major avg `1.1518` n `8`; equity avg `1.5027` n `107`; fx avg `0.0511` n `6`; index avg `0.074` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.2394` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
