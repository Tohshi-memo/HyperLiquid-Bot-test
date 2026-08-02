# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T06:07:28.735481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.0049` n `230`; crypto_major avg `-0.0663` n `8`; equity avg `0.0866` n `102`; fx avg `0.0019` n `6`; index avg `0.0167` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.015` n `766`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.1121` n `230`; crypto_major avg `-0.038` n `8`; equity avg `0.0472` n `102`; fx avg `-0.005` n `6`; index avg `0.0111` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.3303` n `766`
- 4h: commodity avg `-0.4359` n `12`; crypto_alt avg `0.2824` n `230`; crypto_major avg `0.2332` n `8`; equity avg `0.545` n `102`; fx avg `-0.0534` n `6`; index avg `0.1798` n `25`; metal avg `0.141` n `20`; unknown avg `0.4627` n `766`
- 24h: commodity avg `-1.0686` n `12`; crypto_alt avg `0.3602` n `230`; crypto_major avg `0.5547` n `8`; equity avg `0.9716` n `102`; fx avg `-0.1242` n `6`; index avg `0.2671` n `25`; metal avg `0.2472` n `20`; unknown avg `0.3692` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
