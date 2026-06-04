# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T18:37:27.291448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3481` n `12`; crypto_alt avg `0.7319` n `228`; crypto_major avg `0.7804` n `8`; equity avg `0.0901` n `74`; fx avg `0.0015` n `6`; index avg `0.0164` n `23`; metal avg `-0.1208` n `18`; unknown avg `0.596` n `424`
- 1h: commodity avg `0.3171` n `12`; crypto_alt avg `0.5657` n `228`; crypto_major avg `0.923` n `8`; equity avg `0.0455` n `74`; fx avg `0.0012` n `6`; index avg `0.0909` n `23`; metal avg `-0.1125` n `18`; unknown avg `0.5276` n `424`
- 4h: commodity avg `0.2114` n `12`; crypto_alt avg `0.9178` n `228`; crypto_major avg `0.4649` n `8`; equity avg `0.5621` n `74`; fx avg `-0.0402` n `6`; index avg `0.6664` n `23`; metal avg `0.0573` n `18`; unknown avg `1.3772` n `424`
- 24h: commodity avg `-0.7147` n `12`; crypto_alt avg `-4.7325` n `228`; crypto_major avg `-3.3811` n `8`; equity avg `-1.1184` n `73`; fx avg `0.079` n `6`; index avg `-0.0062` n `23`; metal avg `0.7813` n `18`; unknown avg `0.28` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
