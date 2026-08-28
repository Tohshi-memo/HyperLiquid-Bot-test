# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T10:52:28.887811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.1028` n `231`; crypto_major avg `0.0717` n `8`; equity avg `0.0349` n `127`; fx avg `0.0258` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0528` n `20`; unknown avg `0.0728` n `792`
- 1h: commodity avg `0.0997` n `12`; crypto_alt avg `0.2539` n `231`; crypto_major avg `0.1579` n `8`; equity avg `0.0767` n `127`; fx avg `0.0562` n `6`; index avg `-0.0208` n `26`; metal avg `-0.076` n `20`; unknown avg `0.1222` n `792`
- 4h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.5404` n `231`; crypto_major avg `-0.8526` n `8`; equity avg `-0.0865` n `127`; fx avg `0.0431` n `6`; index avg `-0.0261` n `26`; metal avg `0.0773` n `20`; unknown avg `0.0548` n `792`
- 24h: commodity avg `0.1977` n `12`; crypto_alt avg `-0.2315` n `231`; crypto_major avg `0.0293` n `8`; equity avg `-0.9595` n `127`; fx avg `-0.0317` n `6`; index avg `-0.0133` n `26`; metal avg `0.6707` n `20`; unknown avg `0.3917` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
