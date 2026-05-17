# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T19:37:14.076686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.052` n `228`; crypto_major avg `0.1303` n `8`; equity avg `0.0084` n `65`; fx avg `0.0` n `5`; index avg `0.0195` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.0628` n `384`
- 1h: commodity avg `0.0352` n `12`; crypto_alt avg `0.4307` n `228`; crypto_major avg `0.7739` n `8`; equity avg `0.1916` n `65`; fx avg `0.0006` n `5`; index avg `0.0331` n `23`; metal avg `-0.0566` n `18`; unknown avg `0.9667` n `384`
- 4h: commodity avg `0.1426` n `12`; crypto_alt avg `0.0305` n `228`; crypto_major avg `0.9759` n `8`; equity avg `0.1883` n `65`; fx avg `0.011` n `5`; index avg `0.0275` n `23`; metal avg `-0.1206` n `18`; unknown avg `1.0014` n `384`
- 24h: commodity avg `1.8786` n `12`; crypto_alt avg `-9.2499` n `228`; crypto_major avg `-1.4814` n `8`; equity avg `-2.4146` n `65`; fx avg `-0.1549` n `5`; index avg `-1.5667` n `23`; metal avg `-5.9462` n `18`; unknown avg `550.9466` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
