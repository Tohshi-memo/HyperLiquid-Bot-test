# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T01:52:26.815193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0704` n `12`; crypto_alt avg `0.1728` n `228`; crypto_major avg `0.1585` n `8`; equity avg `0.0709` n `74`; fx avg `0.0` n `6`; index avg `0.0529` n `23`; metal avg `0.0315` n `18`; unknown avg `-0.5201` n `643`
- 1h: commodity avg `0.1156` n `12`; crypto_alt avg `0.834` n `228`; crypto_major avg `0.3913` n `8`; equity avg `-0.1154` n `74`; fx avg `0.0185` n `6`; index avg `-0.0329` n `23`; metal avg `0.0177` n `18`; unknown avg `-0.3534` n `643`
- 4h: commodity avg `-0.0197` n `12`; crypto_alt avg `1.0998` n `228`; crypto_major avg `0.1578` n `8`; equity avg `0.1384` n `74`; fx avg `0.0449` n `6`; index avg `0.1595` n `23`; metal avg `0.084` n `18`; unknown avg `-0.3718` n `643`
- 24h: commodity avg `-0.7724` n `12`; crypto_alt avg `0.8467` n `228`; crypto_major avg `0.689` n `8`; equity avg `-0.5255` n `74`; fx avg `0.0128` n `6`; index avg `0.5753` n `23`; metal avg `0.5634` n `18`; unknown avg `40.6132` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
