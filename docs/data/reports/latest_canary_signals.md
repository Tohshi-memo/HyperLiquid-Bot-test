# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T12:37:30.679794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.0243` n `233`; crypto_major avg `-0.0239` n `8`; equity avg `-0.0407` n `136`; fx avg `-0.0058` n `6`; index avg `-0.0073` n `27`; metal avg `0.0725` n `20`; unknown avg `0.3378` n `902`
- 1h: commodity avg `0.1531` n `12`; crypto_alt avg `0.5901` n `233`; crypto_major avg `0.3294` n `8`; equity avg `-0.0549` n `136`; fx avg `0.0231` n `6`; index avg `0.0011` n `27`; metal avg `0.0058` n `20`; unknown avg `0.1453` n `900`
- 4h: commodity avg `-0.1487` n `12`; crypto_alt avg `0.241` n `233`; crypto_major avg `0.4542` n `8`; equity avg `0.5946` n `136`; fx avg `-0.0111` n `6`; index avg `0.1536` n `27`; metal avg `0.199` n `20`; unknown avg `1.499` n `898`
- 24h: commodity avg `-0.34` n `12`; crypto_alt avg `-0.9311` n `233`; crypto_major avg `-0.6082` n `8`; equity avg `0.8456` n `136`; fx avg `0.1854` n `6`; index avg `0.142` n `27`; metal avg `0.0968` n `20`; unknown avg `-0.7695` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
