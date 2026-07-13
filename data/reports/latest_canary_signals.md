# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T13:10:02.436291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0513` n `230`; crypto_major avg `-0.072` n `8`; equity avg `0.0246` n `92`; fx avg `0.0034` n `6`; index avg `0.0365` n `25`; metal avg `0.0091` n `20`; unknown avg `-0.0208` n `766`
- 1h: commodity avg `-0.063` n `12`; crypto_alt avg `-0.2792` n `230`; crypto_major avg `-0.4781` n `8`; equity avg `-0.0032` n `92`; fx avg `0.0034` n `6`; index avg `0.0605` n `25`; metal avg `0.082` n `20`; unknown avg `0.0148` n `766`
- 4h: commodity avg `0.233` n `12`; crypto_alt avg `-0.4032` n `230`; crypto_major avg `-0.8239` n `8`; equity avg `-0.0672` n `92`; fx avg `-0.0221` n `6`; index avg `0.0239` n `25`; metal avg `-0.041` n `20`; unknown avg `0.0227` n `766`
- 24h: commodity avg `-0.0746` n `12`; crypto_alt avg `-1.5029` n `230`; crypto_major avg `-2.1755` n `8`; equity avg `-2.147` n `92`; fx avg `-0.0522` n `6`; index avg `-0.4039` n `25`; metal avg `-0.1924` n `20`; unknown avg `-0.214` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
