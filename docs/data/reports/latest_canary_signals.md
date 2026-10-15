# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T16:22:27.818390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8272` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0551` n `13`; crypto_alt avg `-0.3856` n `236`; crypto_major avg `-0.3321` n `8`; equity avg `-0.2375` n `151`; fx avg `0.0067` n `6`; index avg `-0.0353` n `26`; metal avg `-0.0183` n `20`; unknown avg `0.5916` n `1136`
- 1h: commodity avg `0.0674` n `13`; crypto_alt avg `0.647` n `236`; crypto_major avg `0.2357` n `8`; equity avg `-0.3562` n `151`; fx avg `0.0063` n `6`; index avg `-0.0525` n `26`; metal avg `-0.0806` n `20`; unknown avg `-0.45` n `1128`
- 4h: commodity avg `0.2217` n `13`; crypto_alt avg `3.4035` n `236`; crypto_major avg `1.8572` n `8`; equity avg `1.32` n `151`; fx avg `-0.0057` n `6`; index avg `0.2149` n `26`; metal avg `0.03` n `20`; unknown avg `2.235` n `1082`
- 24h: commodity avg `0.0853` n `13`; crypto_alt avg `0.9914` n `236`; crypto_major avg `0.575` n `8`; equity avg `-1.8476` n `151`; fx avg `0.2172` n `6`; index avg `-0.3049` n `26`; metal avg `0.3522` n `20`; unknown avg `0.0979` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0953`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0879`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0819`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0632`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
