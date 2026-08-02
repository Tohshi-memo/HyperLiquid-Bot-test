# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T23:22:34.935146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0511` n `12`; crypto_alt avg `0.0885` n `230`; crypto_major avg `0.0822` n `8`; equity avg `-0.0509` n `102`; fx avg `0.0706` n `6`; index avg `-0.022` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.0253` n `784`
- 1h: commodity avg `0.0941` n `12`; crypto_alt avg `-0.3466` n `230`; crypto_major avg `-0.4336` n `8`; equity avg `0.0726` n `102`; fx avg `0.0217` n `6`; index avg `0.0316` n `25`; metal avg `-0.0273` n `20`; unknown avg `0.1089` n `783`
- 4h: commodity avg `-0.029` n `12`; crypto_alt avg `-0.0689` n `230`; crypto_major avg `0.1002` n `8`; equity avg `0.2554` n `102`; fx avg `0.1459` n `6`; index avg `0.0535` n `25`; metal avg `-0.0949` n `20`; unknown avg `1.1632` n `783`
- 24h: commodity avg `-1.2551` n `12`; crypto_alt avg `1.1864` n `230`; crypto_major avg `1.656` n `8`; equity avg `1.6349` n `102`; fx avg `0.0653` n `6`; index avg `0.3452` n `25`; metal avg `0.1906` n `20`; unknown avg `1.6064` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
