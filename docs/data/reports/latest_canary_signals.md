# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T23:22:36.671661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.2006` n `236`; crypto_major avg `-0.2441` n `8`; equity avg `-0.0603` n `151`; fx avg `-0.0089` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0153` n `20`; unknown avg `-0.0946` n `1136`
- 1h: commodity avg `-0.0602` n `13`; crypto_alt avg `-0.5467` n `236`; crypto_major avg `-0.6231` n `8`; equity avg `-0.352` n `151`; fx avg `-0.0093` n `6`; index avg `-0.0495` n `26`; metal avg `-0.0396` n `20`; unknown avg `0.4534` n `1134`
- 4h: commodity avg `-0.1134` n `13`; crypto_alt avg `-0.6924` n `236`; crypto_major avg `-0.6841` n `8`; equity avg `-0.1602` n `151`; fx avg `-0.021` n `6`; index avg `-0.0763` n `26`; metal avg `0.0234` n `20`; unknown avg `-0.4622` n `1020`
- 24h: commodity avg `-0.2453` n `13`; crypto_alt avg `0.0882` n `236`; crypto_major avg `0.1811` n `8`; equity avg `1.2593` n `151`; fx avg `0.1244` n `6`; index avg `0.0151` n `26`; metal avg `0.4591` n `20`; unknown avg `24.4637` n `910`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0946`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0898`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0775`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0711`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0524`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
