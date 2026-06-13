# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T03:37:34.959957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0913` n `12`; crypto_alt avg `0.0941` n `228`; crypto_major avg `-0.0499` n `8`; equity avg `-0.066` n `74`; fx avg `-0.009` n `6`; index avg `0.0032` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.0687` n `643`
- 1h: commodity avg `-0.1571` n `12`; crypto_alt avg `-0.3184` n `228`; crypto_major avg `-0.539` n `8`; equity avg `-0.2498` n `74`; fx avg `0.0146` n `6`; index avg `-0.0511` n `23`; metal avg `-0.0351` n `18`; unknown avg `0.6817` n `643`
- 4h: commodity avg `-0.0536` n `12`; crypto_alt avg `0.8048` n `228`; crypto_major avg `-0.0679` n `8`; equity avg `-0.0554` n `74`; fx avg `0.0064` n `6`; index avg `0.175` n `23`; metal avg `0.032` n `18`; unknown avg `-0.4211` n `643`
- 24h: commodity avg `-0.9498` n `12`; crypto_alt avg `-0.0053` n `228`; crypto_major avg `-0.4078` n `8`; equity avg `-0.7526` n `74`; fx avg `-0.0041` n `6`; index avg `0.6713` n `23`; metal avg `0.1987` n `18`; unknown avg `40.1619` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
