# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T08:22:24.671330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3367` n `12`; crypto_alt avg `0.1202` n `228`; crypto_major avg `0.0891` n `8`; equity avg `0.1054` n `74`; fx avg `0.0247` n `6`; index avg `0.1256` n `23`; metal avg `0.3845` n `18`; unknown avg `0.0562` n `547`
- 1h: commodity avg `-0.1363` n `12`; crypto_alt avg `-0.4888` n `228`; crypto_major avg `-0.6195` n `8`; equity avg `-0.1677` n `74`; fx avg `0.0563` n `6`; index avg `0.0478` n `23`; metal avg `0.4043` n `18`; unknown avg `-0.0109` n `547`
- 4h: commodity avg `-0.1324` n `12`; crypto_alt avg `0.8846` n `228`; crypto_major avg `0.5372` n `8`; equity avg `0.1997` n `74`; fx avg `0.1042` n `6`; index avg `0.1773` n `23`; metal avg `0.6392` n `18`; unknown avg `0.4189` n `503`
- 24h: commodity avg `-1.3194` n `12`; crypto_alt avg `0.3286` n `228`; crypto_major avg `0.8963` n `8`; equity avg `2.1162` n `74`; fx avg `0.0122` n `6`; index avg `1.0942` n `23`; metal avg `1.1219` n `18`; unknown avg `-2.5828` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
