# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T11:06:20.551263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `-0.0056` n `8`; equity avg `-0.0705` n `102`; fx avg `-0.0208` n `6`; index avg `0.0062` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.0104` n `782`
- 1h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.2468` n `230`; crypto_major avg `-0.1531` n `8`; equity avg `-0.0663` n `102`; fx avg `-0.0504` n `6`; index avg `-0.0026` n `25`; metal avg `0.002` n `20`; unknown avg `-0.067` n `782`
- 4h: commodity avg `0.1144` n `12`; crypto_alt avg `-0.2046` n `230`; crypto_major avg `-0.3813` n `8`; equity avg `0.1084` n `102`; fx avg `-0.0554` n `6`; index avg `0.0016` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.1251` n `782`
- 24h: commodity avg `-1.0216` n `12`; crypto_alt avg `0.3641` n `230`; crypto_major avg `0.3124` n `8`; equity avg `0.9247` n `102`; fx avg `-0.1645` n `6`; index avg `0.2291` n `25`; metal avg `0.2478` n `20`; unknown avg `0.2663` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
