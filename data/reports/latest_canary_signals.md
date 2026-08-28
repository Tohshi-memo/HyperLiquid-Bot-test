# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T02:37:26.854078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.002` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.3555` n `231`; crypto_major avg `0.0676` n `8`; equity avg `-0.1163` n `127`; fx avg `0.0193` n `6`; index avg `-0.0134` n `26`; metal avg `0.0399` n `20`; unknown avg `-0.0131` n `792`
- 1h: commodity avg `0.0595` n `12`; crypto_alt avg `-1.8673` n `231`; crypto_major avg `-0.9893` n `8`; equity avg `-0.1326` n `127`; fx avg `0.0336` n `6`; index avg `0.0127` n `26`; metal avg `0.0127` n `20`; unknown avg `0.4813` n `792`
- 4h: commodity avg `-0.0336` n `12`; crypto_alt avg `-1.1728` n `231`; crypto_major avg `-0.7125` n `8`; equity avg `0.0538` n `127`; fx avg `-0.0254` n `6`; index avg `0.0604` n `26`; metal avg `-0.1405` n `20`; unknown avg `-0.1962` n `792`
- 24h: commodity avg `0.3149` n `12`; crypto_alt avg `0.5742` n `231`; crypto_major avg `1.9703` n `8`; equity avg `0.0992` n `127`; fx avg `0.0056` n `6`; index avg `0.036` n `26`; metal avg `-0.0928` n `20`; unknown avg `0.6112` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
