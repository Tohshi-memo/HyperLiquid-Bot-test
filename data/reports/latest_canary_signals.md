# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T12:37:32.879920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0643` n `12`; crypto_alt avg `-0.0423` n `230`; crypto_major avg `-0.003` n `8`; equity avg `0.0538` n `102`; fx avg `0.0105` n `6`; index avg `0.0014` n `25`; metal avg `-0.0488` n `20`; unknown avg `-0.001` n `785`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0544` n `230`; crypto_major avg `-0.1834` n `8`; equity avg `-0.1525` n `102`; fx avg `-0.0178` n `6`; index avg `-0.0528` n `25`; metal avg `-0.1545` n `20`; unknown avg `-0.0007` n `785`
- 4h: commodity avg `-0.161` n `12`; crypto_alt avg `0.3382` n `230`; crypto_major avg `0.453` n `8`; equity avg `-0.9025` n `102`; fx avg `-0.0282` n `6`; index avg `-0.1695` n `25`; metal avg `-0.3149` n `20`; unknown avg `0.3323` n `784`
- 24h: commodity avg `-0.3384` n `12`; crypto_alt avg `-0.7381` n `230`; crypto_major avg `-0.1085` n `8`; equity avg `-0.8083` n `102`; fx avg `-0.2099` n `6`; index avg `-0.1847` n `25`; metal avg `-0.3916` n `20`; unknown avg `1.2952` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
