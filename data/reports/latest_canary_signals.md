# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T08:37:19.371754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.133` n `12`; crypto_alt avg `0.1215` n `228`; crypto_major avg `0.1427` n `8`; equity avg `0.1236` n `66`; fx avg `-0.0119` n `6`; index avg `0.0936` n `23`; metal avg `0.0047` n `18`; unknown avg `0.0232` n `384`
- 1h: commodity avg `-0.1414` n `12`; crypto_alt avg `-0.0706` n `228`; crypto_major avg `0.0279` n `8`; equity avg `0.2147` n `66`; fx avg `-0.0176` n `6`; index avg `0.2235` n `23`; metal avg `0.1062` n `18`; unknown avg `-0.1109` n `384`
- 4h: commodity avg `-0.3533` n `12`; crypto_alt avg `1.2099` n `228`; crypto_major avg `0.9227` n `8`; equity avg `0.7825` n `66`; fx avg `-0.0452` n `6`; index avg `0.4931` n `23`; metal avg `0.9491` n `18`; unknown avg `0.3129` n `374`
- 24h: commodity avg `-0.027` n `12`; crypto_alt avg `0.0338` n `228`; crypto_major avg `0.0073` n `8`; equity avg `0.7873` n `66`; fx avg `-0.1768` n `6`; index avg `-0.1272` n `23`; metal avg `-1.059` n `18`; unknown avg `0.1768` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
