# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T14:52:31.112699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.0196` n `230`; crypto_major avg `-0.0063` n `8`; equity avg `0.0172` n `102`; fx avg `0.0023` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0005` n `782`
- 1h: commodity avg `-0.0703` n `12`; crypto_alt avg `0.0412` n `230`; crypto_major avg `0.0613` n `8`; equity avg `0.009` n `102`; fx avg `-0.011` n `6`; index avg `0.0192` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.032` n `782`
- 4h: commodity avg `0.0064` n `12`; crypto_alt avg `0.2065` n `230`; crypto_major avg `0.1462` n `8`; equity avg `-0.072` n `102`; fx avg `-0.0259` n `6`; index avg `-0.0343` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.1219` n `781`
- 24h: commodity avg `0.3603` n `12`; crypto_alt avg `0.4225` n `230`; crypto_major avg `-0.5057` n `8`; equity avg `-0.8118` n `102`; fx avg `-0.0605` n `6`; index avg `-0.0392` n `25`; metal avg `0.016` n `20`; unknown avg `4.2055` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
