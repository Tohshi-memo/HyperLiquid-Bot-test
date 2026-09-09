# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T08:37:34.310333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `-0.0082` n `233`; crypto_major avg `-0.0387` n `8`; equity avg `-0.0091` n `134`; fx avg `0.0259` n `6`; index avg `-0.0074` n `26`; metal avg `-0.005` n `20`; unknown avg `0.0177` n `792`
- 1h: commodity avg `0.074` n `12`; crypto_alt avg `0.3291` n `233`; crypto_major avg `0.1255` n `8`; equity avg `0.1225` n `134`; fx avg `0.034` n `6`; index avg `-0.0189` n `26`; metal avg `-0.0916` n `20`; unknown avg `-0.035` n `790`
- 4h: commodity avg `0.1372` n `12`; crypto_alt avg `1.0443` n `233`; crypto_major avg `0.6202` n `8`; equity avg `0.225` n `134`; fx avg `0.0345` n `6`; index avg `-0.0153` n `26`; metal avg `0.1981` n `20`; unknown avg `1.0127` n `772`
- 24h: commodity avg `-0.1863` n `12`; crypto_alt avg `0.8825` n `232`; crypto_major avg `1.5675` n `8`; equity avg `1.7173` n `134`; fx avg `-0.076` n `6`; index avg `0.1127` n `26`; metal avg `0.0511` n `20`; unknown avg `0.521` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
