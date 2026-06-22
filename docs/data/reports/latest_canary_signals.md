# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T16:52:36.188584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2138` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.0283` n `228`; crypto_major avg `0.0469` n `8`; equity avg `0.2149` n `85`; fx avg `0.0016` n `6`; index avg `0.0277` n `23`; metal avg `0.026` n `20`; unknown avg `-0.1121` n `717`
- 1h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.1464` n `228`; crypto_major avg `-0.2013` n `8`; equity avg `-0.1842` n `85`; fx avg `-0.0048` n `6`; index avg `0.0233` n `23`; metal avg `0.1117` n `20`; unknown avg `-0.0796` n `717`
- 4h: commodity avg `-0.14` n `12`; crypto_alt avg `-1.1004` n `228`; crypto_major avg `-1.2404` n `8`; equity avg `-0.8884` n `85`; fx avg `-0.0775` n `6`; index avg `-0.0266` n `23`; metal avg `-0.1925` n `20`; unknown avg `0.2445` n `716`
- 24h: commodity avg `-0.7633` n `12`; crypto_alt avg `-0.4254` n `228`; crypto_major avg `-0.3045` n `8`; equity avg `-0.6386` n `85`; fx avg `0.0267` n `6`; index avg `0.1288` n `23`; metal avg `0.2173` n `18`; unknown avg `0.9423` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
