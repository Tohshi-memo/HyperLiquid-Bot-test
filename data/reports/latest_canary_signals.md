# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T22:18:31.052100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `-0.1678` n `228`; crypto_major avg `-0.1398` n `8`; equity avg `0.0187` n `88`; fx avg `-0.0017` n `6`; index avg `0.0024` n `23`; metal avg `0.0045` n `20`; unknown avg `-0.1193` n `763`
- 1h: commodity avg `-0.0393` n `12`; crypto_alt avg `-0.025` n `228`; crypto_major avg `0.0497` n `8`; equity avg `0.0284` n `88`; fx avg `0.017` n `6`; index avg `-0.0323` n `23`; metal avg `0.0202` n `20`; unknown avg `-0.1299` n `763`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `-0.6289` n `228`; crypto_major avg `-0.1599` n `8`; equity avg `0.3816` n `88`; fx avg `0.0327` n `6`; index avg `0.0267` n `23`; metal avg `-0.036` n `20`; unknown avg `0.0667` n `763`
- 24h: commodity avg `-0.2986` n `12`; crypto_alt avg `1.8938` n `228`; crypto_major avg `3.3601` n `8`; equity avg `1.6916` n `88`; fx avg `0.225` n `6`; index avg `0.0909` n `23`; metal avg `-0.2644` n `20`; unknown avg `1.6582` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
