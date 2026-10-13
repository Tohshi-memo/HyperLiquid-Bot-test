# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T16:52:25.359310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `13`; crypto_alt avg `0.1765` n `235`; crypto_major avg `0.0712` n `8`; equity avg `-0.0462` n `151`; fx avg `0.0026` n `6`; index avg `-0.005` n `26`; metal avg `-0.0182` n `20`; unknown avg `-0.2742` n `1135`
- 1h: commodity avg `-0.0082` n `13`; crypto_alt avg `0.8501` n `235`; crypto_major avg `0.3514` n `8`; equity avg `0.6652` n `151`; fx avg `-0.0185` n `6`; index avg `0.0989` n `26`; metal avg `-0.0406` n `20`; unknown avg `0.5895` n `1127`
- 4h: commodity avg `0.79` n `13`; crypto_alt avg `0.4528` n `235`; crypto_major avg `0.426` n `8`; equity avg `0.7763` n `151`; fx avg `0.004` n `6`; index avg `0.0882` n `26`; metal avg `-0.2633` n `20`; unknown avg `0.5162` n `1091`
- 24h: commodity avg `0.4619` n `13`; crypto_alt avg `-1.3208` n `235`; crypto_major avg `-0.3513` n `8`; equity avg `-0.8083` n `151`; fx avg `0.1465` n `6`; index avg `-0.1834` n `26`; metal avg `-0.226` n `20`; unknown avg `0.3288` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1623`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1477`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1248`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0898`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
