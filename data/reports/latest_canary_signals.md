# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T02:22:10.879896+00:00`
- Correlation status: `ready`
- Asset price records: `605`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0531` n `12`; crypto_alt avg `-0.0048` n `228`; crypto_major avg `-0.1` n `8`; equity avg `0.0402` n `65`; fx avg `0.0032` n `5`; index avg `-0.0637` n `23`; metal avg `-0.1835` n `18`; unknown avg `1.5801` n `365`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.4046` n `228`; crypto_major avg `-0.3527` n `8`; equity avg `-0.1379` n `65`; fx avg `0.0236` n `5`; index avg `-0.0346` n `23`; metal avg `-0.0255` n `18`; unknown avg `0.4828` n `365`
- 4h: commodity avg `-0.2038` n `12`; crypto_alt avg `-0.3848` n `228`; crypto_major avg `-0.5621` n `8`; equity avg `0.7219` n `65`; fx avg `0.0985` n `5`; index avg `0.3157` n `23`; metal avg `0.7109` n `18`; unknown avg `0.6266` n `365`
- 24h: commodity avg `0.557` n `12`; crypto_alt avg `1.8393` n `228`; crypto_major avg `-1.4709` n `8`; equity avg `-0.8093` n `65`; fx avg `0.2002` n `5`; index avg `-0.5932` n `23`; metal avg `0.3224` n `18`; unknown avg `0.8163` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `601`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `601`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `601`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `601`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `597`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1083`, n `597`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `597`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.09`, n `597`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.078`, n `597`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `601`, weak_sample_signal
