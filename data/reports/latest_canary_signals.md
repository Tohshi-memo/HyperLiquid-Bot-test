# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T14:22:25.266030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.0842` n `232`; crypto_major avg `0.0671` n `8`; equity avg `0.004` n `128`; fx avg `0.0095` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0439` n `20`; unknown avg `0.0902` n `792`
- 1h: commodity avg `-0.054` n `12`; crypto_alt avg `-0.0446` n `232`; crypto_major avg `-0.1636` n `8`; equity avg `0.1475` n `128`; fx avg `-0.0027` n `6`; index avg `-0.04` n `26`; metal avg `-0.1694` n `20`; unknown avg `-0.0799` n `790`
- 4h: commodity avg `-0.1897` n `12`; crypto_alt avg `-0.2927` n `232`; crypto_major avg `-0.2584` n `8`; equity avg `-0.0772` n `128`; fx avg `0.007` n `6`; index avg `-0.0738` n `26`; metal avg `-0.2404` n `20`; unknown avg `0.2228` n `790`
- 24h: commodity avg `0.4947` n `12`; crypto_alt avg `-1.575` n `231`; crypto_major avg `-2.2618` n `8`; equity avg `-0.6004` n `128`; fx avg `-0.0971` n `6`; index avg `-0.1745` n `26`; metal avg `-0.5536` n `20`; unknown avg `0.1218` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
