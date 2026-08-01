# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T20:37:30.577393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1127` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1491` n `230`; crypto_major avg `-0.0547` n `8`; equity avg `-0.036` n `102`; fx avg `-0.0291` n `6`; index avg `0.0101` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0202` n `782`
- 1h: commodity avg `-0.0659` n `12`; crypto_alt avg `0.0071` n `230`; crypto_major avg `0.1376` n `8`; equity avg `0.0006` n `102`; fx avg `-0.0222` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0208` n `20`; unknown avg `-0.0108` n `782`
- 4h: commodity avg `0.056` n `12`; crypto_alt avg `-1.2602` n `230`; crypto_major avg `-1.1491` n `8`; equity avg `-0.2834` n `102`; fx avg `-0.0297` n `6`; index avg `-0.0364` n `25`; metal avg `-0.0061` n `20`; unknown avg `2.9529` n `782`
- 24h: commodity avg `0.6022` n `12`; crypto_alt avg `-0.9001` n `230`; crypto_major avg `-1.3352` n `8`; equity avg `-0.7284` n `102`; fx avg `-0.0943` n `6`; index avg `-0.1192` n `25`; metal avg `-0.053` n `20`; unknown avg `4.3109` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
