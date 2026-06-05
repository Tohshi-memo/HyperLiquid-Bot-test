# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T01:56:27.011687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0551` n `12`; crypto_alt avg `-0.0615` n `228`; crypto_major avg `-0.0135` n `8`; equity avg `0.2786` n `74`; fx avg `0.0168` n `6`; index avg `0.0352` n `23`; metal avg `-0.1054` n `18`; unknown avg `0.9378` n `424`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `-0.1539` n `228`; crypto_major avg `0.0607` n `8`; equity avg `0.3224` n `74`; fx avg `0.0849` n `6`; index avg `0.0915` n `23`; metal avg `-0.4284` n `18`; unknown avg `1.1794` n `424`
- 4h: commodity avg `-0.018` n `12`; crypto_alt avg `0.1363` n `228`; crypto_major avg `0.3239` n `8`; equity avg `-0.8971` n `74`; fx avg `0.1557` n `6`; index avg `-0.9093` n `23`; metal avg `-0.9077` n `18`; unknown avg `-0.2797` n `424`
- 24h: commodity avg `-0.1876` n `12`; crypto_alt avg `-3.1423` n `228`; crypto_major avg `-1.2011` n `8`; equity avg `-0.562` n `73`; fx avg `0.2239` n `6`; index avg `-0.4153` n `23`; metal avg `-0.1508` n `18`; unknown avg `-0.4547` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
