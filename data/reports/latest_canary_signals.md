# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T22:34:09.898703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.0095` n `230`; crypto_major avg `0.0445` n `8`; equity avg `0.1417` n `108`; fx avg `0.0037` n `6`; index avg `0.0286` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.041` n `782`
- 1h: commodity avg `-0.0725` n `12`; crypto_alt avg `0.1461` n `230`; crypto_major avg `0.0564` n `8`; equity avg `0.4007` n `108`; fx avg `0.0021` n `6`; index avg `0.0728` n `25`; metal avg `0.0223` n `20`; unknown avg `-0.1019` n `782`
- 4h: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.1889` n `230`; crypto_major avg `-0.4807` n `8`; equity avg `-0.6898` n `108`; fx avg `0.0057` n `6`; index avg `-0.0414` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0586` n `782`
- 24h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.4277` n `230`; crypto_major avg `0.5849` n `8`; equity avg `-0.6553` n `108`; fx avg `-0.0405` n `6`; index avg `-0.0706` n `25`; metal avg `0.7795` n `20`; unknown avg `0.7693` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
