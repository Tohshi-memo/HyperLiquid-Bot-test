# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T18:58:25.008719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `12`; crypto_alt avg `-0.0037` n `230`; crypto_major avg `-0.0427` n `8`; equity avg `-0.2097` n `98`; fx avg `0.0101` n `6`; index avg `-0.005` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.0003` n `771`
- 1h: commodity avg `0.0873` n `12`; crypto_alt avg `0.3132` n `230`; crypto_major avg `0.0536` n `8`; equity avg `-0.3829` n `98`; fx avg `0.0037` n `6`; index avg `-0.0184` n `25`; metal avg `0.0733` n `20`; unknown avg `0.0022` n `771`
- 4h: commodity avg `0.0515` n `12`; crypto_alt avg `-0.0407` n `230`; crypto_major avg `-0.5251` n `8`; equity avg `0.3922` n `98`; fx avg `0.0171` n `6`; index avg `0.1149` n `25`; metal avg `0.064` n `20`; unknown avg `0.1067` n `771`
- 24h: commodity avg `0.2931` n `12`; crypto_alt avg `0.7806` n `230`; crypto_major avg `0.6419` n `8`; equity avg `3.1124` n `98`; fx avg `0.0439` n `6`; index avg `0.5691` n `25`; metal avg `0.7317` n `20`; unknown avg `0.1848` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0899`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0598`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0539`, n `666`, weak_sample_signal
