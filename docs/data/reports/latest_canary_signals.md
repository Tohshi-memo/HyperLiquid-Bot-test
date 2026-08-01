# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T11:22:28.216520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `12`; crypto_alt avg `0.0038` n `230`; crypto_major avg `0.0098` n `8`; equity avg `0.0899` n `102`; fx avg `-0.0222` n `6`; index avg `0.0309` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0012` n `781`
- 1h: commodity avg `0.0459` n `12`; crypto_alt avg `-0.0464` n `230`; crypto_major avg `-0.072` n `8`; equity avg `0.1183` n `102`; fx avg `-0.0442` n `6`; index avg `0.0342` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.031` n `781`
- 4h: commodity avg `0.0894` n `12`; crypto_alt avg `-0.2961` n `230`; crypto_major avg `-0.2569` n `8`; equity avg `0.107` n `102`; fx avg `-0.0437` n `6`; index avg `0.0669` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.074` n `781`
- 24h: commodity avg `0.4222` n `12`; crypto_alt avg `0.1254` n `230`; crypto_major avg `-1.3928` n `8`; equity avg `-2.6318` n `102`; fx avg `-0.1423` n `6`; index avg `-0.2234` n `25`; metal avg `-0.0594` n `20`; unknown avg `4.6261` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
