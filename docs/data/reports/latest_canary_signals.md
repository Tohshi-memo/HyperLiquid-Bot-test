# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T08:52:36.184863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.0539` n `230`; crypto_major avg `-0.0804` n `8`; equity avg `-0.1097` n `92`; fx avg `0.0236` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.0315` n `766`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `0.002` n `230`; crypto_major avg `0.1479` n `8`; equity avg `0.1149` n `92`; fx avg `0.037` n `6`; index avg `0.012` n `25`; metal avg `-0.0265` n `20`; unknown avg `0.0305` n `766`
- 4h: commodity avg `0.1476` n `12`; crypto_alt avg `0.1631` n `230`; crypto_major avg `0.1189` n `8`; equity avg `0.7402` n `92`; fx avg `0.1109` n `6`; index avg `0.1174` n `25`; metal avg `0.0369` n `20`; unknown avg `0.0696` n `750`
- 24h: commodity avg `1.5513` n `12`; crypto_alt avg `-0.9857` n `230`; crypto_major avg `-1.0035` n `8`; equity avg `-0.5257` n `92`; fx avg `-0.0446` n `6`; index avg `-0.137` n `25`; metal avg `-0.2126` n `20`; unknown avg `-0.2826` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
