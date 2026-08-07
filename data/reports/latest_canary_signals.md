# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T20:03:22.695293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.0248` n `230`; crypto_major avg `0.002` n `8`; equity avg `0.1331` n `112`; fx avg `0.0083` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0427` n `20`; unknown avg `-0.0892` n `782`
- 1h: commodity avg `-0.1077` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.241` n `8`; equity avg `0.1423` n `112`; fx avg `-0.0101` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0677` n `20`; unknown avg `-0.1117` n `782`
- 4h: commodity avg `-0.2972` n `12`; crypto_alt avg `-0.2535` n `230`; crypto_major avg `-0.376` n `8`; equity avg `-0.1263` n `112`; fx avg `-0.0144` n `6`; index avg `0.0142` n `25`; metal avg `-0.0411` n `20`; unknown avg `-0.2277` n `782`
- 24h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.0328` n `230`; crypto_major avg `0.0707` n `8`; equity avg `2.1029` n `112`; fx avg `-0.1552` n `6`; index avg `0.113` n `25`; metal avg `0.3559` n `20`; unknown avg `-0.0031` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
