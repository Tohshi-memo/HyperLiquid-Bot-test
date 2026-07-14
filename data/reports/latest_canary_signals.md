# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T01:06:05.769129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0909` n `12`; crypto_alt avg `0.1974` n `230`; crypto_major avg `0.086` n `8`; equity avg `0.2987` n `92`; fx avg `-0.0335` n `6`; index avg `0.1079` n `25`; metal avg `-0.0827` n `20`; unknown avg `0.1101` n `766`
- 1h: commodity avg `-0.0778` n `12`; crypto_alt avg `0.5473` n `230`; crypto_major avg `0.3464` n `8`; equity avg `1.086` n `92`; fx avg `-0.0407` n `6`; index avg `0.3039` n `25`; metal avg `0.004` n `20`; unknown avg `0.4389` n `766`
- 4h: commodity avg `0.2938` n `12`; crypto_alt avg `0.5438` n `230`; crypto_major avg `0.5478` n `8`; equity avg `0.4568` n `92`; fx avg `-0.0384` n `6`; index avg `0.1031` n `25`; metal avg `-0.1019` n `20`; unknown avg `0.1735` n `766`
- 24h: commodity avg `1.0166` n `12`; crypto_alt avg `-1.528` n `230`; crypto_major avg `-2.2852` n `8`; equity avg `-1.7884` n `92`; fx avg `-0.1332` n `6`; index avg `-0.3267` n `25`; metal avg `-0.4106` n `20`; unknown avg `-0.325` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
