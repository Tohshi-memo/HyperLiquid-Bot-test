# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T13:18:41.595459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.05` n `12`; crypto_alt avg `0.2828` n `229`; crypto_major avg `0.1502` n `8`; equity avg `0.1724` n `91`; fx avg `0.0076` n `6`; index avg `0.0197` n `25`; metal avg `0.0387` n `20`; unknown avg `0.0473` n `764`
- 1h: commodity avg `0.0432` n `12`; crypto_alt avg `-0.3458` n `229`; crypto_major avg `-0.4736` n `8`; equity avg `0.2476` n `91`; fx avg `-0.0034` n `6`; index avg `0.0695` n `25`; metal avg `0.0622` n `20`; unknown avg `-0.0768` n `763`
- 4h: commodity avg `-0.3433` n `12`; crypto_alt avg `0.5529` n `229`; crypto_major avg `0.2984` n `8`; equity avg `1.5038` n `91`; fx avg `-0.0358` n `6`; index avg `0.3008` n `25`; metal avg `0.1241` n `20`; unknown avg `0.1989` n `757`
- 24h: commodity avg `1.1487` n `12`; crypto_alt avg `-3.366` n `229`; crypto_major avg `-2.9645` n `8`; equity avg `-1.8494` n `91`; fx avg `-0.0934` n `6`; index avg `-0.4584` n `25`; metal avg `-1.2579` n `20`; unknown avg `-0.4705` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
