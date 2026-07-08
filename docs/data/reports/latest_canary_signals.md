# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T16:37:31.143229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `12`; crypto_alt avg `-0.1241` n `229`; crypto_major avg `-0.0875` n `8`; equity avg `-0.1364` n `91`; fx avg `0.0153` n `6`; index avg `-0.0324` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.0979` n `764`
- 1h: commodity avg `-0.1766` n `12`; crypto_alt avg `0.121` n `229`; crypto_major avg `0.2884` n `8`; equity avg `0.2465` n `91`; fx avg `0.0236` n `6`; index avg `0.139` n `25`; metal avg `0.0779` n `20`; unknown avg `0.0161` n `764`
- 4h: commodity avg `0.2545` n `12`; crypto_alt avg `-0.3613` n `229`; crypto_major avg `-0.5703` n `8`; equity avg `0.5943` n `91`; fx avg `0.0823` n `6`; index avg `0.1509` n `25`; metal avg `-0.3309` n `20`; unknown avg `-0.2593` n `764`
- 24h: commodity avg `1.0221` n `12`; crypto_alt avg `-3.9509` n `229`; crypto_major avg `-4.0852` n `8`; equity avg `-0.6275` n `91`; fx avg `0.0323` n `6`; index avg `-0.2768` n `25`; metal avg `-1.5341` n `20`; unknown avg `-0.647` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
