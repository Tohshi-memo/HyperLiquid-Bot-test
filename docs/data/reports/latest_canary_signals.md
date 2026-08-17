# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T05:07:25.361731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.0471` n `230`; crypto_major avg `-0.0306` n `8`; equity avg `0.0735` n `114`; fx avg `0.0016` n `6`; index avg `0.0053` n `25`; metal avg `-0.0116` n `20`; unknown avg `-0.1072` n `792`
- 1h: commodity avg `0.0198` n `12`; crypto_alt avg `-0.0096` n `230`; crypto_major avg `-0.0997` n `8`; equity avg `0.1098` n `114`; fx avg `-0.0115` n `6`; index avg `0.0077` n `25`; metal avg `-0.0324` n `20`; unknown avg `16.3666` n `792`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `0.5373` n `230`; crypto_major avg `0.5584` n `8`; equity avg `0.5621` n `114`; fx avg `0.0408` n `6`; index avg `0.0559` n `25`; metal avg `-0.0843` n `20`; unknown avg `0.1586` n `792`
- 24h: commodity avg `-0.1501` n `12`; crypto_alt avg `0.4432` n `230`; crypto_major avg `0.6508` n `8`; equity avg `0.8877` n `114`; fx avg `-0.0279` n `6`; index avg `0.0943` n `25`; metal avg `0.1805` n `20`; unknown avg `0.0172` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
