# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T11:12:32.119113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `0.1342` n `230`; crypto_major avg `0.0998` n `8`; equity avg `0.2335` n `114`; fx avg `-0.0107` n `6`; index avg `0.025` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.0308` n `795`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `0.1303` n `230`; crypto_major avg `0.1686` n `8`; equity avg `0.3714` n `114`; fx avg `-0.0095` n `6`; index avg `0.0402` n `25`; metal avg `0.0229` n `20`; unknown avg `0.3312` n `795`
- 4h: commodity avg `-0.0665` n `12`; crypto_alt avg `0.2825` n `230`; crypto_major avg `-0.0997` n `8`; equity avg `-0.8466` n `114`; fx avg `-0.0157` n `6`; index avg `-0.1127` n `25`; metal avg `-0.0936` n `20`; unknown avg `0.0046` n `794`
- 24h: commodity avg `0.4981` n `12`; crypto_alt avg `-0.8129` n `230`; crypto_major avg `-0.0904` n `8`; equity avg `-2.4661` n `114`; fx avg `-0.0453` n `6`; index avg `-0.5098` n `25`; metal avg `-0.2337` n `20`; unknown avg `-0.0296` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
