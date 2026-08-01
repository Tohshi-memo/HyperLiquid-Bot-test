# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T18:37:30.099415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.036` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.4346` n `230`; crypto_major avg `-0.3508` n `8`; equity avg `-0.0447` n `102`; fx avg `0.0079` n `6`; index avg `-0.0156` n `25`; metal avg `0.0042` n `20`; unknown avg `0.8402` n `782`
- 1h: commodity avg `-0.0726` n `12`; crypto_alt avg `-0.5804` n `230`; crypto_major avg `-0.4605` n `8`; equity avg `-0.1778` n `102`; fx avg `-0.0077` n `6`; index avg `-0.0318` n `25`; metal avg `-0.0134` n `20`; unknown avg `1.7718` n `782`
- 4h: commodity avg `0.0757` n `12`; crypto_alt avg `-1.1292` n `230`; crypto_major avg `-1.1004` n `8`; equity avg `-0.2957` n `102`; fx avg `-0.0098` n `6`; index avg `-0.0644` n `25`; metal avg `-0.0101` n `20`; unknown avg `2.2033` n `782`
- 24h: commodity avg `0.5966` n `12`; crypto_alt avg `-0.8996` n `230`; crypto_major avg `-1.3363` n `8`; equity avg `-1.288` n `102`; fx avg `-0.1474` n `6`; index avg `-0.1638` n `25`; metal avg `-0.1181` n `20`; unknown avg `4.2666` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
