# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T08:57:10.350219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.0676` n `228`; crypto_major avg `-0.0624` n `8`; equity avg `-0.0625` n `65`; fx avg `-0.0008` n `5`; index avg `-0.0133` n `23`; metal avg `-0.001` n `18`; unknown avg `0.2578` n `376`
- 1h: commodity avg `-0.0327` n `12`; crypto_alt avg `0.2818` n `228`; crypto_major avg `0.0762` n `8`; equity avg `0.1597` n `65`; fx avg `-0.0008` n `5`; index avg `0.0223` n `23`; metal avg `-0.0189` n `18`; unknown avg `0.0335` n `376`
- 4h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.1922` n `228`; crypto_major avg `-0.1069` n `8`; equity avg `0.0987` n `65`; fx avg `0.0195` n `5`; index avg `0.047` n `23`; metal avg `0.0157` n `18`; unknown avg `0.087` n `355`
- 24h: commodity avg `-0.0006` n `12`; crypto_alt avg `3.8232` n `228`; crypto_major avg `2.3421` n `8`; equity avg `2.8292` n `65`; fx avg `-0.0186` n `5`; index avg `1.2081` n `23`; metal avg `-0.0693` n `18`; unknown avg `0.706` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
