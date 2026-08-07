# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T00:34:20.759139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `0.0966` n `230`; crypto_major avg `0.1048` n `8`; equity avg `0.2231` n `112`; fx avg `-0.0155` n `6`; index avg `0.0496` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0116` n `782`
- 1h: commodity avg `0.0463` n `12`; crypto_alt avg `0.3101` n `230`; crypto_major avg `0.1808` n `8`; equity avg `-0.1018` n `112`; fx avg `-0.0086` n `6`; index avg `-0.0307` n `25`; metal avg `-0.0491` n `20`; unknown avg `-0.0885` n `782`
- 4h: commodity avg `0.1348` n `12`; crypto_alt avg `0.2632` n `230`; crypto_major avg `-0.065` n `8`; equity avg `0.4067` n `112`; fx avg `-0.0186` n `6`; index avg `0.0001` n `25`; metal avg `-0.0473` n `20`; unknown avg `-0.1678` n `782`
- 24h: commodity avg `0.6887` n `12`; crypto_alt avg `0.1461` n `230`; crypto_major avg `-1.1848` n `8`; equity avg `0.7778` n `109`; fx avg `0.0258` n `6`; index avg `-0.083` n `25`; metal avg `-0.2923` n `20`; unknown avg `112.8804` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
