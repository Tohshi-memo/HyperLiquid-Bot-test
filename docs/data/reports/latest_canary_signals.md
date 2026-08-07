# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T02:37:25.264408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.0295` n `230`; crypto_major avg `-0.0605` n `8`; equity avg `0.0127` n `112`; fx avg `0.0095` n `6`; index avg `-0.0236` n `25`; metal avg `-0.03` n `20`; unknown avg `-0.0075` n `782`
- 1h: commodity avg `0.0773` n `12`; crypto_alt avg `0.0101` n `230`; crypto_major avg `-0.2358` n `8`; equity avg `0.4245` n `112`; fx avg `0.0012` n `6`; index avg `-0.0028` n `25`; metal avg `0.0835` n `20`; unknown avg `0.1221` n `782`
- 4h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.2865` n `230`; crypto_major avg `-0.2056` n `8`; equity avg `0.0261` n `112`; fx avg `-0.053` n `6`; index avg `-0.1478` n `25`; metal avg `0.1324` n `20`; unknown avg `-0.0195` n `782`
- 24h: commodity avg `0.4819` n `12`; crypto_alt avg `0.883` n `230`; crypto_major avg `-0.4679` n `8`; equity avg `0.5891` n `109`; fx avg `0.0115` n `6`; index avg `-0.1734` n `25`; metal avg `-0.1998` n `20`; unknown avg `113.1868` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
