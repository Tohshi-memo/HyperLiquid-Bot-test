# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T20:52:31.419705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0684` n `12`; crypto_alt avg `-0.058` n `230`; crypto_major avg `-0.0215` n `8`; equity avg `0.0694` n `94`; fx avg `0.0027` n `6`; index avg `0.0101` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.0637` n `768`
- 1h: commodity avg `0.1001` n `12`; crypto_alt avg `-0.0298` n `230`; crypto_major avg `-0.0479` n `8`; equity avg `0.0635` n `94`; fx avg `-0.0133` n `6`; index avg `0.0369` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.138` n `768`
- 4h: commodity avg `0.1803` n `12`; crypto_alt avg `-0.5865` n `230`; crypto_major avg `-0.7891` n `8`; equity avg `-0.4658` n `94`; fx avg `-0.0151` n `6`; index avg `-0.1167` n `25`; metal avg `-0.2698` n `20`; unknown avg `-0.4747` n `768`
- 24h: commodity avg `-0.2282` n `12`; crypto_alt avg `-1.1336` n `230`; crypto_major avg `-2.0664` n `8`; equity avg `-3.7965` n `94`; fx avg `-0.1536` n `6`; index avg `-0.5349` n `25`; metal avg `-0.8754` n `20`; unknown avg `-0.4179` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
