# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T18:52:35.340941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.0624` n `230`; crypto_major avg `0.0053` n `8`; equity avg `0.0598` n `103`; fx avg `0.0001` n `6`; index avg `0.0051` n `25`; metal avg `0.0344` n `20`; unknown avg `-0.051` n `784`
- 1h: commodity avg `0.0758` n `12`; crypto_alt avg `0.1777` n `230`; crypto_major avg `0.009` n `8`; equity avg `0.0127` n `103`; fx avg `-0.0158` n `6`; index avg `-0.0165` n `25`; metal avg `0.0844` n `20`; unknown avg `0.2652` n `784`
- 4h: commodity avg `0.1304` n `12`; crypto_alt avg `0.4951` n `230`; crypto_major avg `0.3067` n `8`; equity avg `0.6471` n `103`; fx avg `0.0022` n `6`; index avg `0.1096` n `25`; metal avg `0.1122` n `20`; unknown avg `-0.1009` n `784`
- 24h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.3378` n `230`; crypto_major avg `0.492` n `8`; equity avg `1.8567` n `102`; fx avg `-0.209` n `6`; index avg `0.0481` n `25`; metal avg `-0.4371` n `20`; unknown avg `0.0174` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
