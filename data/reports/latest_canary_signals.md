# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T23:37:50.087861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `0.0085` n `230`; crypto_major avg `0.0419` n `8`; equity avg `0.0898` n `92`; fx avg `-0.02` n `6`; index avg `0.0011` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.0838` n `768`
- 1h: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.1279` n `230`; crypto_major avg `-0.1864` n `8`; equity avg `0.3236` n `92`; fx avg `-0.037` n `6`; index avg `0.0684` n `25`; metal avg `0.0455` n `20`; unknown avg `0.1629` n `766`
- 4h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.3613` n `230`; crypto_major avg `0.3107` n `8`; equity avg `0.4333` n `92`; fx avg `-0.0286` n `6`; index avg `0.0662` n `25`; metal avg `0.0293` n `20`; unknown avg `-0.2806` n `766`
- 24h: commodity avg `0.0835` n `12`; crypto_alt avg `2.3687` n `230`; crypto_major avg `3.6915` n `8`; equity avg `2.329` n `92`; fx avg `-0.0239` n `6`; index avg `0.5639` n `25`; metal avg `0.6599` n `20`; unknown avg `0.2076` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
