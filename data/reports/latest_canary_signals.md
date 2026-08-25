# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T07:07:28.834506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0427` n `12`; crypto_alt avg `0.2942` n `231`; crypto_major avg `0.4055` n `8`; equity avg `0.0978` n `122`; fx avg `0.0131` n `6`; index avg `0.0057` n `25`; metal avg `-0.03` n `20`; unknown avg `0.0196` n `794`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.3811` n `231`; crypto_major avg `-0.1264` n `8`; equity avg `0.0675` n `122`; fx avg `0.0464` n `6`; index avg `0.0397` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.0789` n `794`
- 4h: commodity avg `-0.2552` n `12`; crypto_alt avg `-0.2819` n `231`; crypto_major avg `-0.2711` n `8`; equity avg `0.9334` n `122`; fx avg `0.0324` n `6`; index avg `0.172` n `25`; metal avg `0.0413` n `20`; unknown avg `-0.1574` n `778`
- 24h: commodity avg `-0.1725` n `12`; crypto_alt avg `1.7087` n `231`; crypto_major avg `2.3675` n `8`; equity avg `0.3363` n `122`; fx avg `0.0194` n `6`; index avg `0.0717` n `25`; metal avg `-0.2084` n `20`; unknown avg `0.4916` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
