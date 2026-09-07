# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T10:07:28.864134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0498` n `232`; crypto_major avg `0.0514` n `8`; equity avg `-0.0191` n `134`; fx avg `0.0137` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0442` n `20`; unknown avg `1.6765` n `794`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0979` n `232`; crypto_major avg `0.0325` n `8`; equity avg `-0.0673` n `134`; fx avg `0.0337` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0498` n `20`; unknown avg `0.0415` n `790`
- 4h: commodity avg `-0.2333` n `12`; crypto_alt avg `0.0815` n `232`; crypto_major avg `-0.3346` n `8`; equity avg `-0.0392` n `134`; fx avg `-0.0906` n `6`; index avg `0.03` n `26`; metal avg `0.1188` n `20`; unknown avg `2.9777` n `774`
- 24h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.1932` n `232`; crypto_major avg `-0.8562` n `8`; equity avg `0.3` n `134`; fx avg `-0.1213` n `6`; index avg `0.0173` n `26`; metal avg `-0.1166` n `20`; unknown avg `230.9239` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
