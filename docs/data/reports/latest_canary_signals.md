# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T03:52:30.536071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.0245` n `233`; crypto_major avg `-0.0249` n `8`; equity avg `0.0371` n `134`; fx avg `-0.017` n `6`; index avg `0.0087` n `26`; metal avg `-0.0221` n `20`; unknown avg `-0.0215` n `797`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `0.0415` n `233`; crypto_major avg `-0.0389` n `8`; equity avg `-0.0219` n `134`; fx avg `-0.0011` n `6`; index avg `0.0139` n `26`; metal avg `-0.0926` n `20`; unknown avg `119.3543` n `795`
- 4h: commodity avg `-0.2197` n `12`; crypto_alt avg `-0.4704` n `233`; crypto_major avg `0.0377` n `8`; equity avg `-0.2598` n `134`; fx avg `-0.0248` n `6`; index avg `0.0212` n `26`; metal avg `0.0082` n `20`; unknown avg `8.1657` n `789`
- 24h: commodity avg `-0.0247` n `12`; crypto_alt avg `-2.5858` n `233`; crypto_major avg `-1.6266` n `8`; equity avg `-1.0211` n `134`; fx avg `0.0035` n `6`; index avg `-0.1632` n `26`; metal avg `0.3812` n `20`; unknown avg `1.2991` n `667`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
