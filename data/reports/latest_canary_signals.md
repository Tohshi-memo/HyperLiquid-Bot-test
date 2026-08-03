# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T20:41:13.662724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `-0.0169` n `230`; crypto_major avg `-0.0348` n `8`; equity avg `-0.0099` n `103`; fx avg `0.0095` n `6`; index avg `0.0166` n `25`; metal avg `0.0564` n `20`; unknown avg `0.7367` n `784`
- 1h: commodity avg `-0.074` n `12`; crypto_alt avg `-0.0045` n `230`; crypto_major avg `0.1238` n `8`; equity avg `0.1405` n `103`; fx avg `0.0256` n `6`; index avg `0.0513` n `25`; metal avg `0.0571` n `20`; unknown avg `0.2648` n `784`
- 4h: commodity avg `-0.0159` n `12`; crypto_alt avg `0.3164` n `230`; crypto_major avg `0.1535` n `8`; equity avg `0.843` n `103`; fx avg `0.0106` n `6`; index avg `0.1712` n `25`; metal avg `0.1657` n `20`; unknown avg `0.1839` n `784`
- 24h: commodity avg `-0.1696` n `12`; crypto_alt avg `0.4739` n `230`; crypto_major avg `0.7069` n `8`; equity avg `1.9728` n `103`; fx avg `-0.2488` n `6`; index avg `0.1071` n `25`; metal avg `-0.3584` n `20`; unknown avg `0.0519` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
