# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T02:37:28.083437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `-0.2702` n `231`; crypto_major avg `-0.1642` n `8`; equity avg `0.0227` n `126`; fx avg `0.0122` n `6`; index avg `0.007` n `25`; metal avg `-0.0904` n `20`; unknown avg `-0.0643` n `793`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.4236` n `231`; crypto_major avg `-0.3826` n `8`; equity avg `0.0101` n `126`; fx avg `0.0196` n `6`; index avg `0.0215` n `25`; metal avg `-0.0185` n `20`; unknown avg `-0.2222` n `793`
- 4h: commodity avg `0.0143` n `12`; crypto_alt avg `-0.1985` n `231`; crypto_major avg `0.0717` n `8`; equity avg `-0.3517` n `126`; fx avg `-0.0546` n `6`; index avg `-0.1114` n `25`; metal avg `0.083` n `20`; unknown avg `-0.055` n `793`
- 24h: commodity avg `0.3998` n `12`; crypto_alt avg `-0.1736` n `231`; crypto_major avg `0.2116` n `8`; equity avg `1.3281` n `126`; fx avg `-0.117` n `6`; index avg `0.2273` n `25`; metal avg `-0.3142` n `20`; unknown avg `0.6152` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
