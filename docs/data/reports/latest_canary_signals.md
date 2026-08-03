# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T05:37:26.778233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.0374` n `230`; crypto_major avg `-0.0103` n `8`; equity avg `0.0909` n `102`; fx avg `-0.0188` n `6`; index avg `0.024` n `25`; metal avg `-0.0279` n `20`; unknown avg `0.0822` n `784`
- 1h: commodity avg `-0.0513` n `12`; crypto_alt avg `-0.094` n `230`; crypto_major avg `-0.2489` n `8`; equity avg `-0.1273` n `102`; fx avg `-0.002` n `6`; index avg `-0.0223` n `25`; metal avg `-0.1046` n `20`; unknown avg `0.4134` n `784`
- 4h: commodity avg `-0.1374` n `12`; crypto_alt avg `-0.1806` n `230`; crypto_major avg `-0.3808` n `8`; equity avg `0.2307` n `102`; fx avg `-0.0218` n `6`; index avg `0.1019` n `25`; metal avg `-0.0382` n `20`; unknown avg `0.1413` n `784`
- 24h: commodity avg `-0.3167` n `12`; crypto_alt avg `-0.8991` n `230`; crypto_major avg `-0.6984` n `8`; equity avg `0.8459` n `102`; fx avg `-0.2283` n `6`; index avg `0.0252` n `25`; metal avg `-0.1153` n `20`; unknown avg `1.0084` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
