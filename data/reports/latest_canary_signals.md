# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T18:37:28.030106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `13`; crypto_alt avg `0.2659` n `239`; crypto_major avg `0.1982` n `8`; equity avg `0.0274` n `166`; fx avg `0.0138` n `6`; index avg `0.0626` n `27`; metal avg `0.0106` n `20`; unknown avg `187.3415` n `1262`
- 1h: commodity avg `0.018` n `13`; crypto_alt avg `0.1676` n `239`; crypto_major avg `0.1337` n `8`; equity avg `0.0763` n `166`; fx avg `0.0225` n `6`; index avg `-0.0055` n `27`; metal avg `0.0191` n `20`; unknown avg `-0.2192` n `1218`
- 4h: commodity avg `0.0171` n `13`; crypto_alt avg `-0.056` n `239`; crypto_major avg `0.2531` n `8`; equity avg `0.1658` n `166`; fx avg `0.019` n `6`; index avg `-0.0087` n `27`; metal avg `0.0305` n `20`; unknown avg `209.2639` n `1200`
- 24h: commodity avg `0.4931` n `13`; crypto_alt avg `0.6143` n `239`; crypto_major avg `1.4504` n `8`; equity avg `0.0273` n `166`; fx avg `-0.0986` n `6`; index avg `-0.0237` n `27`; metal avg `0.2187` n `20`; unknown avg `0.133` n `1094`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
