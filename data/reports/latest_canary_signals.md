# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T00:52:27.527706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5955` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.458` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0411` n `13`; crypto_alt avg `0.6828` n `238`; crypto_major avg `0.4215` n `8`; equity avg `-0.277` n `156`; fx avg `0.0027` n `6`; index avg `-0.0465` n `27`; metal avg `0.0416` n `20`; unknown avg `4.6187` n `1260`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `-1.3998` n `238`; crypto_major avg `-0.5126` n `8`; equity avg `-0.3905` n `156`; fx avg `0.0154` n `6`; index avg `-0.091` n `27`; metal avg `0.0457` n `20`; unknown avg `6.0831` n `1238`
- 4h: commodity avg `-0.0743` n `13`; crypto_alt avg `-2.6326` n `238`; crypto_major avg `-1.626` n `8`; equity avg `-1.4025` n `156`; fx avg `0.0204` n `6`; index avg `-0.168` n `27`; metal avg `-0.0305` n `20`; unknown avg `167.0379` n `1232`
- 24h: commodity avg `-0.2534` n `13`; crypto_alt avg `-7.4834` n `238`; crypto_major avg `-3.2526` n `8`; equity avg `-4.1785` n `155`; fx avg `0.1887` n `6`; index avg `-0.4188` n `27`; metal avg `-0.4907` n `20`; unknown avg `33.8275` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
