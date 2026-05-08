# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T22:07:20.835933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.055` n `12`; crypto_alt avg `0.2208` n `228`; crypto_major avg `0.1783` n `8`; equity avg `0.0566` n `65`; fx avg `0.0068` n `5`; index avg `0.0121` n `23`; metal avg `0.0018` n `18`; unknown avg `0.0843` n `375`
- 1h: commodity avg `-0.0723` n `12`; crypto_alt avg `0.5485` n `228`; crypto_major avg `0.4093` n `8`; equity avg `0.2167` n `65`; fx avg `-0.0227` n `5`; index avg `0.1061` n `23`; metal avg `-0.0318` n `18`; unknown avg `-0.2904` n `375`
- 4h: commodity avg `-0.12` n `12`; crypto_alt avg `0.9322` n `228`; crypto_major avg `0.5164` n `8`; equity avg `0.9155` n `65`; fx avg `0.0126` n `5`; index avg `-0.0201` n `23`; metal avg `-0.2541` n `18`; unknown avg `-0.3636` n `375`
- 24h: commodity avg `-0.7818` n `12`; crypto_alt avg `4.3482` n `228`; crypto_major avg `2.1366` n `8`; equity avg `4.5346` n `65`; fx avg `0.2184` n `5`; index avg `1.7036` n `23`; metal avg `1.3152` n `18`; unknown avg `1.0625` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
