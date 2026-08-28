# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T14:07:29.350707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.7752` n `231`; crypto_major avg `-0.7534` n `8`; equity avg `-0.5001` n `127`; fx avg `-0.0285` n `6`; index avg `-0.0509` n `26`; metal avg `-0.4265` n `20`; unknown avg `-0.166` n `793`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `-1.0474` n `231`; crypto_major avg `-0.7186` n `8`; equity avg `-0.7622` n `127`; fx avg `-0.0351` n `6`; index avg `-0.0678` n `26`; metal avg `-0.369` n `20`; unknown avg `-0.2231` n `793`
- 4h: commodity avg `-0.1693` n `12`; crypto_alt avg `-0.296` n `231`; crypto_major avg `-0.0226` n `8`; equity avg `-0.5762` n `127`; fx avg `-0.0032` n `6`; index avg `-0.0268` n `26`; metal avg `-0.2352` n `20`; unknown avg `-0.1702` n `792`
- 24h: commodity avg `-0.3182` n `12`; crypto_alt avg `-1.9723` n `231`; crypto_major avg `-1.123` n `8`; equity avg `-1.1088` n `127`; fx avg `-0.1413` n `6`; index avg `0.0534` n `26`; metal avg `0.5568` n `20`; unknown avg `0.2001` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
