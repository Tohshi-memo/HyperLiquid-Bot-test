# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T02:52:28.777255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `13`; crypto_alt avg `-0.2418` n `236`; crypto_major avg `-0.181` n `8`; equity avg `-0.1436` n `151`; fx avg `-0.0007` n `6`; index avg `-0.0224` n `26`; metal avg `0.0317` n `20`; unknown avg `0.2957` n `1136`
- 1h: commodity avg `-0.09` n `13`; crypto_alt avg `-0.1108` n `236`; crypto_major avg `0.0004` n `8`; equity avg `0.1124` n `151`; fx avg `-0.0214` n `6`; index avg `0.0159` n `26`; metal avg `0.1824` n `20`; unknown avg `-0.2432` n `1134`
- 4h: commodity avg `-0.0927` n `13`; crypto_alt avg `-0.4215` n `236`; crypto_major avg `-0.4747` n `8`; equity avg `-0.0018` n `151`; fx avg `0.035` n `6`; index avg `0.0012` n `26`; metal avg `0.1254` n `20`; unknown avg `0.3251` n `1128`
- 24h: commodity avg `-0.0801` n `13`; crypto_alt avg `3.0833` n `236`; crypto_major avg `1.6571` n `8`; equity avg `1.9018` n `151`; fx avg `-0.0429` n `6`; index avg `0.3539` n `26`; metal avg `0.3824` n `20`; unknown avg `25.5956` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0931`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0877`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0761`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
