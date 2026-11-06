# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T23:52:28.793411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `13`; crypto_alt avg `0.0792` n `239`; crypto_major avg `0.0372` n `8`; equity avg `0.0715` n `158`; fx avg `0.004` n `6`; index avg `0.0123` n `27`; metal avg `0.0076` n `20`; unknown avg `-0.0884` n `1261`
- 1h: commodity avg `0.0142` n `13`; crypto_alt avg `-0.109` n `239`; crypto_major avg `0.0212` n `8`; equity avg `-0.0716` n `158`; fx avg `0.0048` n `6`; index avg `-0.0036` n `27`; metal avg `0.0007` n `20`; unknown avg `-0.2409` n `1239`
- 4h: commodity avg `-0.0435` n `13`; crypto_alt avg `-0.2968` n `239`; crypto_major avg `0.0783` n `8`; equity avg `0.2194` n `158`; fx avg `0.0249` n `6`; index avg `-0.0176` n `27`; metal avg `0.0611` n `20`; unknown avg `-0.3418` n `1165`
- 24h: commodity avg `0.0616` n `13`; crypto_alt avg `2.1657` n `239`; crypto_major avg `0.5039` n `8`; equity avg `4.0087` n `158`; fx avg `-0.0576` n `6`; index avg `0.5062` n `27`; metal avg `0.0679` n `20`; unknown avg `8.7597` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
