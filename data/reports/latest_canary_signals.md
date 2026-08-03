# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T20:07:32.673871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.0331` n `230`; crypto_major avg `-0.0587` n `8`; equity avg `-0.0587` n `103`; fx avg `0.0047` n `6`; index avg `0.001` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.0261` n `784`
- 1h: commodity avg `-0.0627` n `12`; crypto_alt avg `-0.165` n `230`; crypto_major avg `-0.0209` n `8`; equity avg `0.1272` n `103`; fx avg `0.0185` n `6`; index avg `0.0112` n `25`; metal avg `0.0264` n `20`; unknown avg `0.0084` n `784`
- 4h: commodity avg `0.0159` n `12`; crypto_alt avg `0.1501` n `230`; crypto_major avg `0.0342` n `8`; equity avg `0.7911` n `103`; fx avg `-0.0132` n `6`; index avg `0.1321` n `25`; metal avg `0.1475` n `20`; unknown avg `-0.2267` n `784`
- 24h: commodity avg `-0.0768` n `12`; crypto_alt avg `0.2537` n `230`; crypto_major avg `0.4522` n `8`; equity avg `1.9306` n `103`; fx avg `-0.278` n `6`; index avg `0.0625` n `25`; metal avg `-0.4049` n `20`; unknown avg `0.0491` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
