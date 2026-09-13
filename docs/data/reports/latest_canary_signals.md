# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T17:22:34.848845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `0.1919` n `233`; crypto_major avg `0.088` n `8`; equity avg `0.0452` n `136`; fx avg `-0.0063` n `6`; index avg `-0.0005` n `27`; metal avg `0.002` n `20`; unknown avg `-0.1151` n `818`
- 1h: commodity avg `-0.0163` n `12`; crypto_alt avg `0.5364` n `233`; crypto_major avg `0.2939` n `8`; equity avg `0.0844` n `136`; fx avg `-0.0062` n `6`; index avg `-0.0123` n `27`; metal avg `0.0228` n `20`; unknown avg `5.4472` n `790`
- 4h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.9303` n `233`; crypto_major avg `1.1682` n `8`; equity avg `0.5248` n `136`; fx avg `0.0021` n `6`; index avg `0.051` n `27`; metal avg `0.0276` n `20`; unknown avg `4.3987` n `790`
- 24h: commodity avg `0.2522` n `12`; crypto_alt avg `-0.0227` n `233`; crypto_major avg `-0.859` n `8`; equity avg `-1.4385` n `136`; fx avg `0.0036` n `6`; index avg `-0.2608` n `26`; metal avg `-0.0726` n `20`; unknown avg `1.7928` n `704`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
