# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T23:37:24.990398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.542` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `0.278` n `231`; crypto_major avg `0.2651` n `8`; equity avg `0.0308` n `124`; fx avg `-0.0008` n `6`; index avg `0.0027` n `25`; metal avg `0.0029` n `20`; unknown avg `0.0552` n `795`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `0.4065` n `231`; crypto_major avg `0.4879` n `8`; equity avg `0.0158` n `124`; fx avg `0.0066` n `6`; index avg `-0.0215` n `25`; metal avg `0.0477` n `20`; unknown avg `0.0559` n `795`
- 4h: commodity avg `0.0139` n `12`; crypto_alt avg `2.0576` n `231`; crypto_major avg `1.7135` n `8`; equity avg `1.6707` n `124`; fx avg `-0.0025` n `6`; index avg `0.2782` n `25`; metal avg `0.1715` n `20`; unknown avg `0.6406` n `795`
- 24h: commodity avg `0.3113` n `12`; crypto_alt avg `1.7467` n `231`; crypto_major avg `1.3918` n `8`; equity avg `1.6293` n `124`; fx avg `-0.0519` n `6`; index avg `0.3203` n `25`; metal avg `-0.2096` n `20`; unknown avg `1.0036` n `778`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
