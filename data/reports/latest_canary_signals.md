# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T06:22:27.547008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.1545` n `231`; crypto_major avg `0.052` n `8`; equity avg `0.085` n `127`; fx avg `-0.0128` n `6`; index avg `0.021` n `26`; metal avg `0.1043` n `20`; unknown avg `0.0072` n `792`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `0.5815` n `231`; crypto_major avg `0.4987` n `8`; equity avg `-0.0045` n `127`; fx avg `-0.0534` n `6`; index avg `0.0039` n `26`; metal avg `0.1081` n `20`; unknown avg `-0.0057` n `760`
- 4h: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.3199` n `231`; crypto_major avg `-0.0862` n `8`; equity avg `-0.532` n `127`; fx avg `-0.0706` n `6`; index avg `-0.0667` n `26`; metal avg `0.1568` n `20`; unknown avg `-0.1487` n `760`
- 24h: commodity avg `0.3462` n `12`; crypto_alt avg `0.8798` n `231`; crypto_major avg `1.8901` n `8`; equity avg `-0.1838` n `127`; fx avg `-0.0991` n `6`; index avg `0.0689` n `26`; metal avg `0.1613` n `20`; unknown avg `0.4748` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
