# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T16:07:27.869026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0671` n `12`; crypto_alt avg `0.1725` n `230`; crypto_major avg `0.2452` n `8`; equity avg `-0.0262` n `113`; fx avg `-0.0045` n `6`; index avg `0.0069` n `25`; metal avg `0.0099` n `20`; unknown avg `0.0833` n `785`
- 1h: commodity avg `0.0673` n `12`; crypto_alt avg `-0.6114` n `230`; crypto_major avg `-0.2247` n `8`; equity avg `-0.1708` n `113`; fx avg `0.01` n `6`; index avg `-0.0497` n `25`; metal avg `-0.092` n `20`; unknown avg `-0.1334` n `785`
- 4h: commodity avg `0.1206` n `12`; crypto_alt avg `-1.5502` n `230`; crypto_major avg `-1.0201` n `8`; equity avg `0.0715` n `113`; fx avg `0.0201` n `6`; index avg `-0.0519` n `25`; metal avg `-0.2039` n `20`; unknown avg `0.2602` n `785`
- 24h: commodity avg `0.2411` n `12`; crypto_alt avg `-2.1846` n `230`; crypto_major avg `-0.4678` n `8`; equity avg `-0.0673` n `113`; fx avg `-0.0513` n `6`; index avg `0.0623` n `25`; metal avg `-0.0314` n `20`; unknown avg `-0.3325` n `753`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
