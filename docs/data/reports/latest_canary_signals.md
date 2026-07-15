# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T08:07:26.170763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0577` n `12`; crypto_alt avg `-0.1205` n `230`; crypto_major avg `-0.0633` n `8`; equity avg `-0.2135` n `93`; fx avg `0.0033` n `6`; index avg `-0.0405` n `25`; metal avg `0.0193` n `20`; unknown avg `-0.0287` n `767`
- 1h: commodity avg `0.066` n `12`; crypto_alt avg `-0.3804` n `230`; crypto_major avg `-0.3622` n `8`; equity avg `-0.3267` n `93`; fx avg `0.0098` n `6`; index avg `-0.0646` n `25`; metal avg `-0.0643` n `20`; unknown avg `-0.0413` n `765`
- 4h: commodity avg `0.0778` n `12`; crypto_alt avg `-0.5028` n `230`; crypto_major avg `-0.3084` n `8`; equity avg `-0.5404` n `93`; fx avg `-0.0005` n `6`; index avg `-0.1256` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0854` n `747`
- 24h: commodity avg `-0.0378` n `12`; crypto_alt avg `1.3304` n `230`; crypto_major avg `3.0028` n `8`; equity avg `1.3545` n `92`; fx avg `0.0637` n `6`; index avg `0.4317` n `25`; metal avg `0.2639` n `20`; unknown avg `0.2392` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
