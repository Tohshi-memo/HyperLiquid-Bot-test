# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T19:37:18.474024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `0.0863` n `228`; crypto_major avg `0.0761` n `8`; equity avg `0.0033` n `66`; fx avg `0.0032` n `6`; index avg `0.0465` n `23`; metal avg `-0.0134` n `18`; unknown avg `0.029` n `384`
- 1h: commodity avg `0.1669` n `12`; crypto_alt avg `0.2611` n `228`; crypto_major avg `0.2071` n `8`; equity avg `-0.0685` n `66`; fx avg `0.0071` n `6`; index avg `0.2091` n `23`; metal avg `-0.0266` n `18`; unknown avg `0.0796` n `384`
- 4h: commodity avg `-0.1272` n `12`; crypto_alt avg `0.4337` n `228`; crypto_major avg `0.2504` n `8`; equity avg `0.0745` n `66`; fx avg `0.0302` n `6`; index avg `0.3044` n `23`; metal avg `0.1856` n `18`; unknown avg `0.4983` n `384`
- 24h: commodity avg `-2.5177` n `12`; crypto_alt avg `2.8409` n `228`; crypto_major avg `1.8768` n `8`; equity avg `1.5707` n `66`; fx avg `-0.0195` n `6`; index avg `1.2371` n `23`; metal avg `1.5839` n `18`; unknown avg `1.0192` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0449`, n `668`, weak_sample_signal
