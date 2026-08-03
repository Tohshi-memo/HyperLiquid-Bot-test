# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T04:52:29.392575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `-0.1079` n `230`; crypto_major avg `-0.1537` n `8`; equity avg `-0.0822` n `102`; fx avg `0.0122` n `6`; index avg `-0.0188` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.0637` n `784`
- 1h: commodity avg `-0.046` n `12`; crypto_alt avg `0.019` n `230`; crypto_major avg `-0.0395` n `8`; equity avg `-0.1484` n `102`; fx avg `0.0013` n `6`; index avg `-0.0225` n `25`; metal avg `0.0685` n `20`; unknown avg `-0.0485` n `784`
- 4h: commodity avg `-0.1709` n `12`; crypto_alt avg `-0.4711` n `230`; crypto_major avg `-0.5102` n `8`; equity avg `0.1172` n `102`; fx avg `0.0115` n `6`; index avg `0.0692` n `25`; metal avg `0.0929` n `20`; unknown avg `-0.063` n `784`
- 24h: commodity avg `-0.2586` n `12`; crypto_alt avg `-0.8615` n `230`; crypto_major avg `-0.615` n `8`; equity avg `0.8176` n `102`; fx avg `-0.2379` n `6`; index avg `0.0432` n `25`; metal avg `0.0059` n `20`; unknown avg `1.3173` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
