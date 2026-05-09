# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T18:39:08.096986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.43` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.1311` n `228`; crypto_major avg `0.128` n `8`; equity avg `0.039` n `65`; fx avg `-0.0017` n `5`; index avg `-0.0197` n `23`; metal avg `0.0165` n `18`; unknown avg `-0.0473` n `376`
- 1h: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.0349` n `228`; crypto_major avg `0.0674` n `8`; equity avg `-0.003` n `65`; fx avg `-0.0051` n `5`; index avg `-0.0365` n `23`; metal avg `0.0492` n `18`; unknown avg `-0.0355` n `376`
- 4h: commodity avg `0.1303` n `12`; crypto_alt avg `0.7981` n `228`; crypto_major avg `0.5504` n `8`; equity avg `0.1922` n `65`; fx avg `-0.0236` n `5`; index avg `0.0566` n `23`; metal avg `0.0604` n `18`; unknown avg `0.272` n `376`
- 24h: commodity avg `0.2172` n `12`; crypto_alt avg `0.4855` n `228`; crypto_major avg `0.4502` n `8`; equity avg `1.1778` n `65`; fx avg `-0.0147` n `5`; index avg `0.3469` n `23`; metal avg `-0.2115` n `18`; unknown avg `-0.1066` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
