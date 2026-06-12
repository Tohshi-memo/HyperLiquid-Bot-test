# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T19:37:29.048879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2746` n `12`; crypto_alt avg `0.173` n `228`; crypto_major avg `0.0137` n `8`; equity avg `-0.1145` n `74`; fx avg `-0.001` n `6`; index avg `-0.0877` n `23`; metal avg `-0.0772` n `18`; unknown avg `-0.1792` n `643`
- 1h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.2001` n `228`; crypto_major avg `-0.1973` n `8`; equity avg `-0.167` n `74`; fx avg `-0.0104` n `6`; index avg `-0.1104` n `23`; metal avg `-0.2839` n `18`; unknown avg `-0.1913` n `643`
- 4h: commodity avg `0.0301` n `12`; crypto_alt avg `-0.3957` n `228`; crypto_major avg `-0.317` n `8`; equity avg `-0.2669` n `74`; fx avg `-0.0051` n `6`; index avg `-0.1135` n `23`; metal avg `0.0657` n `18`; unknown avg `-0.3296` n `643`
- 24h: commodity avg `-0.541` n `12`; crypto_alt avg `0.0155` n `228`; crypto_major avg `0.2505` n `8`; equity avg `-0.2975` n `74`; fx avg `0.0386` n `6`; index avg `0.3957` n `23`; metal avg `0.1124` n `18`; unknown avg `41.1753` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
