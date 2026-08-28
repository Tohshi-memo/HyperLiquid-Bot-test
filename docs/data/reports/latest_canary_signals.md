# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T07:52:24.771539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `0.0606` n `231`; crypto_major avg `0.0245` n `8`; equity avg `-0.056` n `127`; fx avg `0.0085` n `6`; index avg `-0.0` n `26`; metal avg `-0.0416` n `20`; unknown avg `0.1008` n `792`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `-0.4865` n `231`; crypto_major avg `-0.3874` n `8`; equity avg `-0.0355` n `127`; fx avg `-0.017` n `6`; index avg `0.0043` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.0568` n `792`
- 4h: commodity avg `-0.1296` n `12`; crypto_alt avg `0.006` n `231`; crypto_major avg `-0.0838` n `8`; equity avg `-0.3968` n `127`; fx avg `-0.0523` n `6`; index avg `-0.0335` n `26`; metal avg `0.3904` n `20`; unknown avg `0.0069` n `760`
- 24h: commodity avg `0.3586` n `12`; crypto_alt avg `0.1043` n `231`; crypto_major avg `1.2371` n `8`; equity avg `-0.605` n `127`; fx avg `-0.0903` n `6`; index avg `0.0309` n `26`; metal avg `0.5405` n `20`; unknown avg `0.4671` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
