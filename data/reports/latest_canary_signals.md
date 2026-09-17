# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T18:07:39.458420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0699` n `12`; crypto_alt avg `0.0099` n `234`; crypto_major avg `-0.001` n `8`; equity avg `0.0231` n `138`; fx avg `0.005` n `6`; index avg `0.0034` n `26`; metal avg `0.0024` n `20`; unknown avg `0.2791` n `917`
- 1h: commodity avg `-0.0665` n `12`; crypto_alt avg `-0.1883` n `234`; crypto_major avg `-0.334` n `8`; equity avg `-0.1815` n `138`; fx avg `-0.0009` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0804` n `20`; unknown avg `0.8028` n `917`
- 4h: commodity avg `0.151` n `12`; crypto_alt avg `1.1662` n `234`; crypto_major avg `0.4724` n `8`; equity avg `0.52` n `138`; fx avg `-0.0173` n `6`; index avg `0.0789` n `26`; metal avg `-0.1156` n `20`; unknown avg `2.6845` n `909`
- 24h: commodity avg `-0.0196` n `12`; crypto_alt avg `3.9618` n `234`; crypto_major avg `1.5077` n `8`; equity avg `1.464` n `138`; fx avg `0.0878` n `6`; index avg `0.2362` n `26`; metal avg `0.2178` n `20`; unknown avg `0.3761` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
