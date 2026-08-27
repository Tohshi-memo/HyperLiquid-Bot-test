# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T18:22:26.940684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0844` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1791` n `12`; crypto_alt avg `-0.7276` n `231`; crypto_major avg `-0.7267` n `8`; equity avg `-0.0327` n `127`; fx avg `-0.0031` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0196` n `20`; unknown avg `0.3083` n `792`
- 1h: commodity avg `0.0717` n `12`; crypto_alt avg `-1.1454` n `231`; crypto_major avg `-1.179` n `8`; equity avg `-0.273` n `127`; fx avg `0.0157` n `6`; index avg `-0.0946` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.4705` n `792`
- 4h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.3081` n `231`; crypto_major avg `-0.0021` n `8`; equity avg `-0.3149` n `127`; fx avg `-0.0071` n `6`; index avg `-0.0369` n `26`; metal avg `0.2515` n `20`; unknown avg `0.1882` n `792`
- 24h: commodity avg `0.4393` n `12`; crypto_alt avg `2.6652` n `231`; crypto_major avg `3.4083` n `8`; equity avg `1.4204` n `127`; fx avg `-0.0502` n `6`; index avg `0.1396` n `26`; metal avg `0.1691` n `20`; unknown avg `0.8517` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
