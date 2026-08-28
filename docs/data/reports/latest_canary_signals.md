# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T07:37:27.136444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `-0.0714` n `231`; crypto_major avg `0.0021` n `8`; equity avg `0.0097` n `127`; fx avg `-0.0022` n `6`; index avg `0.0015` n `26`; metal avg `0.0739` n `20`; unknown avg `-0.0704` n `792`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.3367` n `231`; crypto_major avg `-0.2829` n `8`; equity avg `-0.004` n `127`; fx avg `-0.0246` n `6`; index avg `0.0263` n `26`; metal avg `0.2409` n `20`; unknown avg `-0.0357` n `792`
- 4h: commodity avg `-0.1271` n `12`; crypto_alt avg `-0.0883` n `231`; crypto_major avg `-0.1788` n `8`; equity avg `-0.4117` n `127`; fx avg `-0.0738` n `6`; index avg `-0.0408` n `26`; metal avg `0.4093` n `20`; unknown avg `-0.1646` n `760`
- 24h: commodity avg `0.3335` n `12`; crypto_alt avg `0.1912` n `231`; crypto_major avg `1.3949` n `8`; equity avg `-0.4919` n `127`; fx avg `-0.1027` n `6`; index avg `0.04` n `26`; metal avg `0.5865` n `20`; unknown avg `0.3606` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
