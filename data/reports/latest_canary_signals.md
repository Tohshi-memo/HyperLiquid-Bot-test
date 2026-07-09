# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T13:23:54.252309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3065` n `12`; crypto_alt avg `-0.0449` n `229`; crypto_major avg `0.1318` n `8`; equity avg `0.0655` n `91`; fx avg `-0.0043` n `6`; index avg `0.0211` n `25`; metal avg `0.0884` n `20`; unknown avg `-0.0539` n `765`
- 1h: commodity avg `-0.3206` n `12`; crypto_alt avg `-0.0568` n `229`; crypto_major avg `-0.001` n `8`; equity avg `0.2401` n `91`; fx avg `-0.0208` n `6`; index avg `0.0774` n `25`; metal avg `0.0846` n `20`; unknown avg `0.0748` n `765`
- 4h: commodity avg `-0.1249` n `12`; crypto_alt avg `-0.0446` n `229`; crypto_major avg `-0.2238` n `8`; equity avg `0.4903` n `91`; fx avg `-0.0311` n `6`; index avg `0.1805` n `25`; metal avg `0.184` n `20`; unknown avg `0.053` n `764`
- 24h: commodity avg `-0.5068` n `12`; crypto_alt avg `1.4891` n `229`; crypto_major avg `0.7126` n `8`; equity avg `3.1709` n `91`; fx avg `0.1246` n `6`; index avg `0.5085` n `25`; metal avg `0.7271` n `20`; unknown avg `0.773` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.097`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.067`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0611`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0588`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.058`, n `669`, weak_sample_signal
