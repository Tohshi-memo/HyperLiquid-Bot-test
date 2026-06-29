# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T20:52:30.342249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.2018` n `228`; crypto_major avg `-0.0758` n `8`; equity avg `0.0482` n `88`; fx avg `0.0023` n `6`; index avg `0.0136` n `23`; metal avg `0.0045` n `20`; unknown avg `0.0428` n `765`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.3147` n `228`; crypto_major avg `-0.4571` n `8`; equity avg `0.1379` n `88`; fx avg `0.0084` n `6`; index avg `0.0145` n `23`; metal avg `0.0394` n `20`; unknown avg `0.3367` n `765`
- 4h: commodity avg `-0.1146` n `12`; crypto_alt avg `0.3841` n `228`; crypto_major avg `1.3925` n `8`; equity avg `0.869` n `88`; fx avg `-0.0093` n `6`; index avg `0.1223` n `23`; metal avg `0.2251` n `20`; unknown avg `-0.0523` n `765`
- 24h: commodity avg `-0.3509` n `12`; crypto_alt avg `1.4953` n `228`; crypto_major avg `2.8429` n `8`; equity avg `1.6433` n `88`; fx avg `0.1797` n `6`; index avg `0.1587` n `23`; metal avg `-0.5049` n `20`; unknown avg `0.345` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
