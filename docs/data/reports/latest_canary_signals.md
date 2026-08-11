# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T12:02:46.280372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.0071` n `230`; crypto_major avg `0.037` n `8`; equity avg `0.0105` n `113`; fx avg `0.0077` n `6`; index avg `0.002` n `25`; metal avg `-0.0649` n `20`; unknown avg `-0.0335` n `785`
- 1h: commodity avg `0.0921` n `12`; crypto_alt avg `-0.0353` n `230`; crypto_major avg `0.0413` n `8`; equity avg `-0.1338` n `113`; fx avg `-0.0037` n `6`; index avg `-0.0348` n `25`; metal avg `-0.0914` n `20`; unknown avg `-0.1141` n `785`
- 4h: commodity avg `-0.4041` n `12`; crypto_alt avg `0.1628` n `230`; crypto_major avg `0.5389` n `8`; equity avg `0.3215` n `113`; fx avg `-0.0645` n `6`; index avg `0.079` n `25`; metal avg `0.1329` n `20`; unknown avg `-0.0699` n `785`
- 24h: commodity avg `0.5428` n `12`; crypto_alt avg `-1.3397` n `230`; crypto_major avg `-0.5956` n `8`; equity avg `-0.6799` n `113`; fx avg `-0.0143` n `6`; index avg `0.1023` n `25`; metal avg `0.3505` n `20`; unknown avg `0.0788` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
