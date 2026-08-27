# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T02:52:25.144680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.0858` n `231`; crypto_major avg `-0.0094` n `8`; equity avg `0.1544` n `126`; fx avg `0.0076` n `6`; index avg `0.0157` n `25`; metal avg `0.0334` n `20`; unknown avg `-0.0502` n `793`
- 1h: commodity avg `-0.0249` n `12`; crypto_alt avg `-0.6106` n `231`; crypto_major avg `-0.5027` n `8`; equity avg `0.1919` n `126`; fx avg `0.0281` n `6`; index avg `0.0375` n `25`; metal avg `-0.035` n `20`; unknown avg `-0.0861` n `793`
- 4h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.163` n `231`; crypto_major avg `0.2235` n `8`; equity avg `-0.1594` n `126`; fx avg `-0.0408` n `6`; index avg `-0.086` n `25`; metal avg `0.1321` n `20`; unknown avg `-0.0093` n `793`
- 24h: commodity avg `0.4121` n `12`; crypto_alt avg `-0.1785` n `231`; crypto_major avg `0.2594` n `8`; equity avg `1.3245` n `126`; fx avg `-0.1192` n `6`; index avg `0.2025` n `25`; metal avg `-0.3151` n `20`; unknown avg `0.3747` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
