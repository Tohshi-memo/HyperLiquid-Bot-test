# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T09:37:26.007438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `12`; crypto_alt avg `-0.0301` n `229`; crypto_major avg `-0.0608` n `8`; equity avg `-0.1191` n `91`; fx avg `-0.0157` n `6`; index avg `-0.0026` n `25`; metal avg `0.0409` n `20`; unknown avg `-0.0454` n `763`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `0.0475` n `229`; crypto_major avg `0.1226` n `8`; equity avg `-0.2262` n `91`; fx avg `-0.0333` n `6`; index avg `-0.0236` n `25`; metal avg `0.0273` n `20`; unknown avg `0.0691` n `759`
- 4h: commodity avg `0.1951` n `12`; crypto_alt avg `0.1168` n `229`; crypto_major avg `0.2167` n `8`; equity avg `0.0478` n `91`; fx avg `-0.0516` n `6`; index avg `0.0612` n `25`; metal avg `0.2584` n `20`; unknown avg `6.1652` n `743`
- 24h: commodity avg `0.3967` n `12`; crypto_alt avg `0.7417` n `229`; crypto_major avg `0.2233` n `8`; equity avg `-1.5588` n `90`; fx avg `-0.0887` n `6`; index avg `-0.3577` n `25`; metal avg `-0.1747` n `20`; unknown avg `-0.4166` n `741`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
