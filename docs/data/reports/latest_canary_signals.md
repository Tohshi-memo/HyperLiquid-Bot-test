# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T13:52:33.785372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.169` n `12`; crypto_alt avg `0.1853` n `229`; crypto_major avg `0.3016` n `8`; equity avg `0.0415` n `91`; fx avg `-0.0231` n `6`; index avg `0.0543` n `25`; metal avg `0.1165` n `20`; unknown avg `0.0564` n `766`
- 1h: commodity avg `-0.2842` n `12`; crypto_alt avg `0.255` n `229`; crypto_major avg `0.4752` n `8`; equity avg `-0.2026` n `91`; fx avg `-0.0471` n `6`; index avg `0.0474` n `25`; metal avg `0.1088` n `20`; unknown avg `-0.0634` n `766`
- 4h: commodity avg `-0.2855` n `12`; crypto_alt avg `0.2466` n `229`; crypto_major avg `0.1287` n `8`; equity avg `0.0564` n `91`; fx avg `-0.0453` n `6`; index avg `0.0601` n `25`; metal avg `0.1215` n `20`; unknown avg `-0.0633` n `766`
- 24h: commodity avg `-0.8638` n `12`; crypto_alt avg `1.1805` n `229`; crypto_major avg `1.6769` n `8`; equity avg `-0.6587` n `91`; fx avg `-0.1458` n `6`; index avg `-0.002` n `25`; metal avg `-0.1235` n `20`; unknown avg `-0.118` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
