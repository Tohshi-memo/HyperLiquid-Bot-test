# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T15:07:25.877167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `-0.0443` n `8`; equity avg `-0.0161` n `96`; fx avg `0.0104` n `6`; index avg `0.0074` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0271` n `770`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.3152` n `230`; crypto_major avg `0.2933` n `8`; equity avg `0.0109` n `96`; fx avg `0.004` n `6`; index avg `0.0016` n `25`; metal avg `-0.0215` n `20`; unknown avg `0.0139` n `770`
- 4h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.051` n `230`; crypto_major avg `0.1506` n `8`; equity avg `-0.0988` n `96`; fx avg `0.0045` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0405` n `20`; unknown avg `-0.0465` n `770`
- 24h: commodity avg `0.5944` n `12`; crypto_alt avg `-0.0053` n `230`; crypto_major avg `0.9561` n `8`; equity avg `0.4906` n `96`; fx avg `-0.0066` n `6`; index avg `0.1538` n `25`; metal avg `0.1052` n `20`; unknown avg `0.1358` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
