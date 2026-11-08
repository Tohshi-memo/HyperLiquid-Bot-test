# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T00:37:27.976884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0656` n `13`; crypto_alt avg `-0.1046` n `239`; crypto_major avg `-0.1559` n `8`; equity avg `0.0187` n `158`; fx avg `-0.0055` n `6`; index avg `0.0035` n `27`; metal avg `-0.0016` n `20`; unknown avg `0.0872` n `1262`
- 1h: commodity avg `-0.1508` n `13`; crypto_alt avg `-0.1425` n `239`; crypto_major avg `-0.0244` n `8`; equity avg `0.0325` n `158`; fx avg `0.019` n `6`; index avg `0.0169` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.1463` n `1250`
- 4h: commodity avg `-0.1506` n `13`; crypto_alt avg `-0.2015` n `239`; crypto_major avg `0.0639` n `8`; equity avg `-0.0123` n `158`; fx avg `0.0186` n `6`; index avg `0.0077` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.4542` n `1208`
- 24h: commodity avg `-0.0945` n `13`; crypto_alt avg `-1.4934` n `239`; crypto_major avg `-0.7151` n `8`; equity avg `0.0149` n `158`; fx avg `0.004` n `6`; index avg `0.0651` n `27`; metal avg `-0.0247` n `20`; unknown avg `160.9525` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
