# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T17:07:30.485272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0908` n `12`; crypto_alt avg `-0.0859` n `234`; crypto_major avg `0.0929` n `8`; equity avg `0.0163` n `140`; fx avg `0.0027` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.4181` n `940`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.1308` n `234`; crypto_major avg `0.1387` n `8`; equity avg `0.0715` n `140`; fx avg `-0.0158` n `6`; index avg `0.0242` n `26`; metal avg `-0.0796` n `20`; unknown avg `0.2307` n `940`
- 4h: commodity avg `-0.2441` n `12`; crypto_alt avg `-0.6096` n `234`; crypto_major avg `0.4846` n `8`; equity avg `0.851` n `140`; fx avg `-0.0141` n `6`; index avg `0.2365` n `26`; metal avg `-0.2611` n `20`; unknown avg `11.8242` n `870`
- 24h: commodity avg `-1.0664` n `12`; crypto_alt avg `4.1344` n `234`; crypto_major avg `4.9718` n `8`; equity avg `2.6448` n `140`; fx avg `-0.0952` n `6`; index avg `0.5678` n `26`; metal avg `-0.0256` n `20`; unknown avg `7.5404` n `731`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
