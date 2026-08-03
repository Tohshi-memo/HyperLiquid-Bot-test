# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T13:52:37.099019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `12`; crypto_alt avg `0.3047` n `230`; crypto_major avg `0.3376` n `8`; equity avg `0.0062` n `102`; fx avg `-0.0151` n `6`; index avg `-0.0877` n `25`; metal avg `0.0427` n `20`; unknown avg `0.037` n `785`
- 1h: commodity avg `-0.1748` n `12`; crypto_alt avg `0.6727` n `230`; crypto_major avg `0.5833` n `8`; equity avg `0.1781` n `102`; fx avg `-0.0573` n `6`; index avg `-0.0732` n `25`; metal avg `-0.1322` n `20`; unknown avg `0.1434` n `785`
- 4h: commodity avg `-0.2469` n `12`; crypto_alt avg `0.5835` n `230`; crypto_major avg `0.5419` n `8`; equity avg `-0.5857` n `102`; fx avg `-0.0944` n `6`; index avg `-0.1888` n `25`; metal avg `-0.4305` n `20`; unknown avg `0.3267` n `784`
- 24h: commodity avg `-0.5117` n `12`; crypto_alt avg `0.0656` n `230`; crypto_major avg `0.4636` n `8`; equity avg `-0.5967` n `102`; fx avg `-0.2218` n `6`; index avg `-0.2714` n `25`; metal avg `-0.5653` n `20`; unknown avg `1.4215` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
