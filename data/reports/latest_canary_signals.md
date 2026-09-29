# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T22:07:34.714736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1115` n `12`; crypto_alt avg `-0.0304` n `234`; crypto_major avg `0.0849` n `8`; equity avg `0.0665` n `142`; fx avg `-0.0015` n `6`; index avg `0.0312` n `26`; metal avg `0.0311` n `20`; unknown avg `0.132` n `942`
- 1h: commodity avg `-0.0672` n `12`; crypto_alt avg `-0.0833` n `234`; crypto_major avg `0.0067` n `8`; equity avg `0.0882` n `142`; fx avg `-0.0031` n `6`; index avg `0.0342` n `26`; metal avg `0.0288` n `20`; unknown avg `0.7241` n `934`
- 4h: commodity avg `-0.2075` n `12`; crypto_alt avg `0.7052` n `234`; crypto_major avg `0.4475` n `8`; equity avg `0.206` n `142`; fx avg `0.003` n `6`; index avg `0.0964` n `26`; metal avg `0.2107` n `20`; unknown avg `1.4997` n `872`
- 24h: commodity avg `-1.0505` n `12`; crypto_alt avg `1.8947` n `234`; crypto_major avg `0.6004` n `8`; equity avg `0.8473` n `142`; fx avg `-0.1765` n `6`; index avg `0.0988` n `26`; metal avg `0.263` n `20`; unknown avg `3099.5664` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1936`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
