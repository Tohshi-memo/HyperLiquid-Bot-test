# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T05:07:29.339544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2304` n `12`; crypto_alt avg `0.1031` n `228`; crypto_major avg `0.0312` n `8`; equity avg `0.1417` n `74`; fx avg `0.005` n `6`; index avg `0.0348` n `23`; metal avg `0.1353` n `18`; unknown avg `-0.1379` n `547`
- 1h: commodity avg `-0.3393` n `12`; crypto_alt avg `-0.2938` n `228`; crypto_major avg `-0.3405` n `8`; equity avg `-0.2455` n `74`; fx avg `0.005` n `6`; index avg `-0.3063` n `23`; metal avg `-0.2854` n `18`; unknown avg `-0.5768` n `547`
- 4h: commodity avg `-0.3084` n `12`; crypto_alt avg `-1.1164` n `228`; crypto_major avg `-1.0899` n `8`; equity avg `-1.0922` n `74`; fx avg `0.1047` n `6`; index avg `-0.5412` n `23`; metal avg `-0.4268` n `18`; unknown avg `-0.8109` n `547`
- 24h: commodity avg `-0.8285` n `12`; crypto_alt avg `-1.5319` n `228`; crypto_major avg `-3.7114` n `8`; equity avg `-3.8439` n `74`; fx avg `0.1551` n `6`; index avg `-1.8366` n `23`; metal avg `-3.2814` n `18`; unknown avg `0.5837` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
