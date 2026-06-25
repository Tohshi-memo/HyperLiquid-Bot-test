# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T13:07:31.730404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5165` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.0752` n `228`; crypto_major avg `-0.1612` n `8`; equity avg `-0.1837` n `86`; fx avg `0.0042` n `6`; index avg `-0.0157` n `23`; metal avg `0.2681` n `20`; unknown avg `-0.0167` n `765`
- 1h: commodity avg `0.0732` n `12`; crypto_alt avg `0.0197` n `228`; crypto_major avg `0.1568` n `8`; equity avg `0.0886` n `86`; fx avg `0.0321` n `6`; index avg `0.0394` n `23`; metal avg `0.6261` n `20`; unknown avg `-0.0426` n `765`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.8049` n `228`; crypto_major avg `-0.8982` n `8`; equity avg `0.0356` n `86`; fx avg `-0.0138` n `6`; index avg `0.0473` n `23`; metal avg `0.6183` n `20`; unknown avg `-0.1947` n `765`
- 24h: commodity avg `0.1591` n `12`; crypto_alt avg `-1.2944` n `228`; crypto_major avg `-0.984` n `8`; equity avg `0.5606` n `86`; fx avg `0.0364` n `6`; index avg `0.5686` n `23`; metal avg `0.454` n `20`; unknown avg `-0.5725` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
