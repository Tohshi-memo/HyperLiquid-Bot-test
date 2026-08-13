# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T09:52:28.270756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `0.1677` n `230`; crypto_major avg `0.2235` n `8`; equity avg `0.0582` n `113`; fx avg `0.0101` n `6`; index avg `0.0176` n `25`; metal avg `0.0057` n `20`; unknown avg `0.0513` n `787`
- 1h: commodity avg `-0.0341` n `12`; crypto_alt avg `0.1831` n `230`; crypto_major avg `0.1029` n `8`; equity avg `-0.0091` n `113`; fx avg `0.0072` n `6`; index avg `0.0089` n `25`; metal avg `0.0586` n `20`; unknown avg `-0.0465` n `787`
- 4h: commodity avg `-0.292` n `12`; crypto_alt avg `0.0585` n `230`; crypto_major avg `-0.1344` n `8`; equity avg `-0.644` n `113`; fx avg `0.0863` n `6`; index avg `-0.0498` n `25`; metal avg `-0.157` n `20`; unknown avg `-0.1112` n `755`
- 24h: commodity avg `-0.2912` n `12`; crypto_alt avg `-0.4764` n `230`; crypto_major avg `-0.1511` n `8`; equity avg `1.2605` n `113`; fx avg `0.0587` n `6`; index avg `0.1485` n `25`; metal avg `-0.557` n `20`; unknown avg `0.1339` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
