# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T21:52:29.209066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.0971` n `229`; crypto_major avg `-0.0509` n `8`; equity avg `-0.0076` n `88`; fx avg `-0.0004` n `6`; index avg `0.0055` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.021` n `765`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `0.0194` n `229`; crypto_major avg `-0.1241` n `8`; equity avg `-0.0217` n `88`; fx avg `-0.0118` n `6`; index avg `0.0251` n `25`; metal avg `0.0472` n `20`; unknown avg `-0.4389` n `765`
- 4h: commodity avg `0.026` n `12`; crypto_alt avg `0.025` n `229`; crypto_major avg `-0.1816` n `8`; equity avg `0.8233` n `88`; fx avg `0.0335` n `6`; index avg `0.2303` n `25`; metal avg `0.1807` n `20`; unknown avg `-0.3559` n `765`
- 24h: commodity avg `0.0957` n `12`; crypto_alt avg `1.0726` n `228`; crypto_major avg `1.7956` n `8`; equity avg `-2.4568` n `88`; fx avg `-0.0965` n `6`; index avg `-0.4569` n `25`; metal avg `0.9895` n `20`; unknown avg `0.6984` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
