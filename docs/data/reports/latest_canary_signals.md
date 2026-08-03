# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T06:37:40.533598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.1353` n `230`; crypto_major avg `-0.1555` n `8`; equity avg `-0.0288` n `102`; fx avg `0.0566` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0807` n `20`; unknown avg `-0.0238` n `784`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.0805` n `230`; crypto_major avg `-0.1006` n `8`; equity avg `-0.0599` n `102`; fx avg `0.0547` n `6`; index avg `-0.02` n `25`; metal avg `0.0875` n `20`; unknown avg `-0.015` n `768`
- 4h: commodity avg `-0.1709` n `12`; crypto_alt avg `-0.3035` n `230`; crypto_major avg `-0.4705` n `8`; equity avg `-0.2655` n `102`; fx avg `0.0766` n `6`; index avg `-0.0356` n `25`; metal avg `0.0833` n `20`; unknown avg `0.0261` n `768`
- 24h: commodity avg `-0.2775` n `12`; crypto_alt avg `-1.0032` n `230`; crypto_major avg `-0.7596` n `8`; equity avg `0.6783` n `102`; fx avg `-0.1669` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0209` n `20`; unknown avg `0.9728` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
