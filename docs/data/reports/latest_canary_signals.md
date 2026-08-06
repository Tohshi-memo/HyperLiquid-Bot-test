# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T23:07:28.395679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0436` n `230`; crypto_major avg `0.0101` n `8`; equity avg `-0.0547` n `112`; fx avg `-0.0063` n `6`; index avg `-0.0061` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.0073` n `782`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.2256` n `230`; crypto_major avg `-0.0144` n `8`; equity avg `0.0085` n `112`; fx avg `-0.0068` n `6`; index avg `0.005` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.0293` n `782`
- 4h: commodity avg `0.2514` n `12`; crypto_alt avg `-0.3434` n `230`; crypto_major avg `-0.3948` n `8`; equity avg `-0.6587` n `112`; fx avg `-0.0014` n `6`; index avg `-0.0711` n `25`; metal avg `-0.0841` n `20`; unknown avg `-0.2207` n `781`
- 24h: commodity avg `0.6243` n `12`; crypto_alt avg `0.2046` n `230`; crypto_major avg `-0.8636` n `8`; equity avg `0.3886` n `109`; fx avg `0.0259` n `6`; index avg `-0.1633` n `25`; metal avg `-0.0976` n `20`; unknown avg `113.2767` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
