# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T20:07:40.093657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.0472` n `230`; crypto_major avg `-0.0844` n `8`; equity avg `0.0142` n `102`; fx avg `0.0275` n `6`; index avg `0.0155` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0508` n `783`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.0503` n `230`; crypto_major avg `0.053` n `8`; equity avg `0.0743` n `102`; fx avg `0.0798` n `6`; index avg `0.0254` n `25`; metal avg `0.024` n `20`; unknown avg `-0.0883` n `782`
- 4h: commodity avg `-0.1361` n `12`; crypto_alt avg `0.2441` n `230`; crypto_major avg `0.816` n `8`; equity avg `0.4493` n `102`; fx avg `0.1076` n `6`; index avg `0.0671` n `25`; metal avg `0.0942` n `20`; unknown avg `0.4903` n `782`
- 24h: commodity avg `-1.3618` n `12`; crypto_alt avg `1.3909` n `230`; crypto_major avg `2.0188` n `8`; equity avg `1.7416` n `102`; fx avg `-0.0464` n `6`; index avg `0.3475` n `25`; metal avg `0.3478` n `20`; unknown avg `1.5914` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
