# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T05:52:25.189521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.023` n `12`; crypto_alt avg `0.0509` n `230`; crypto_major avg `0.1172` n `8`; equity avg `0.1348` n `93`; fx avg `-0.0281` n `6`; index avg `0.0154` n `25`; metal avg `0.0428` n `20`; unknown avg `0.7499` n `767`
- 1h: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.0667` n `230`; crypto_major avg `0.0154` n `8`; equity avg `-0.1048` n `93`; fx avg `-0.0499` n `6`; index avg `-0.0358` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.3711` n `767`
- 4h: commodity avg `-0.101` n `12`; crypto_alt avg `-0.0795` n `230`; crypto_major avg `0.6669` n `8`; equity avg `0.684` n `93`; fx avg `-0.0168` n `6`; index avg `0.1113` n `25`; metal avg `-0.0158` n `20`; unknown avg `-0.2049` n `767`
- 24h: commodity avg `0.1708` n `12`; crypto_alt avg `1.5009` n `230`; crypto_major avg `3.0623` n `8`; equity avg `1.8403` n `92`; fx avg `0.0589` n `6`; index avg `0.4893` n `25`; metal avg `0.2023` n `20`; unknown avg `0.3142` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
