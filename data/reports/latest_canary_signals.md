# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T05:22:28.673314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.045` n `13`; crypto_alt avg `-0.0534` n `235`; crypto_major avg `-0.0657` n `8`; equity avg `-0.0616` n `151`; fx avg `-0.0051` n `6`; index avg `-0.0166` n `26`; metal avg `-0.0511` n `20`; unknown avg `-0.1519` n `1133`
- 1h: commodity avg `0.0535` n `13`; crypto_alt avg `0.8832` n `235`; crypto_major avg `0.7287` n `8`; equity avg `0.1056` n `151`; fx avg `0.0128` n `6`; index avg `0.0023` n `26`; metal avg `-0.0879` n `20`; unknown avg `0.2312` n `1077`
- 4h: commodity avg `0.0772` n `13`; crypto_alt avg `1.1054` n `235`; crypto_major avg `0.6983` n `8`; equity avg `-0.6588` n `151`; fx avg `0.0114` n `6`; index avg `-0.0066` n `26`; metal avg `-0.1564` n `20`; unknown avg `0.4975` n `1051`
- 24h: commodity avg `0.0` n `5`; crypto_alt avg `3.4055` n `235`; crypto_major avg `1.9445` n `8`; equity avg `0.448` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `-0.003` n `12`; unknown avg `0.9554` n `845`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
