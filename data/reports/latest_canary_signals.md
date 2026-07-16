# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T20:07:26.655658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `-0.0242` n `230`; crypto_major avg `-0.0603` n `8`; equity avg `0.0658` n `94`; fx avg `-0.0182` n `6`; index avg `0.0246` n `25`; metal avg `-0.0318` n `20`; unknown avg `-0.0588` n `768`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.0035` n `230`; crypto_major avg `-0.0386` n `8`; equity avg `0.0265` n `94`; fx avg `-0.0149` n `6`; index avg `0.0111` n `25`; metal avg `-0.0426` n `20`; unknown avg `-0.1331` n `768`
- 4h: commodity avg `-0.0537` n `12`; crypto_alt avg `-0.6009` n `230`; crypto_major avg `-0.9567` n `8`; equity avg `-0.6656` n `94`; fx avg `-0.0113` n `6`; index avg `-0.1863` n `25`; metal avg `-0.2816` n `20`; unknown avg `-0.1178` n `768`
- 24h: commodity avg `-0.379` n `12`; crypto_alt avg `-0.9286` n `230`; crypto_major avg `-1.9054` n `8`; equity avg `-3.7689` n `94`; fx avg `-0.1699` n `6`; index avg `-0.5535` n `25`; metal avg `-0.8385` n `20`; unknown avg `-0.3209` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
