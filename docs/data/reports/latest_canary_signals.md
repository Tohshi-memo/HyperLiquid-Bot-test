# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T19:22:35.013581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0393` n `12`; crypto_alt avg `-0.1068` n `230`; crypto_major avg `-0.0955` n `8`; equity avg `-0.1497` n `113`; fx avg `0.0088` n `6`; index avg `-0.0106` n `25`; metal avg `-0.0897` n `20`; unknown avg `-0.0327` n `787`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `0.0845` n `230`; crypto_major avg `0.2422` n `8`; equity avg `0.0725` n `113`; fx avg `0.0036` n `6`; index avg `0.021` n `25`; metal avg `-0.1235` n `20`; unknown avg `0.1078` n `787`
- 4h: commodity avg `-0.1956` n `12`; crypto_alt avg `-0.7542` n `230`; crypto_major avg `-0.352` n `8`; equity avg `-0.0327` n `113`; fx avg `0.0032` n `6`; index avg `-0.0127` n `25`; metal avg `-0.131` n `20`; unknown avg `-0.077` n `787`
- 24h: commodity avg `-0.5126` n `12`; crypto_alt avg `-0.3104` n `230`; crypto_major avg `0.2503` n `8`; equity avg `1.431` n `113`; fx avg `0.01` n `6`; index avg `0.3231` n `25`; metal avg `-0.5989` n `20`; unknown avg `0.0292` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.232`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
