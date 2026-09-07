# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T09:37:30.740534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0389` n `12`; crypto_alt avg `-0.2683` n `232`; crypto_major avg `-0.2421` n `8`; equity avg `-0.0364` n `134`; fx avg `-0.0235` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.0856` n `796`
- 1h: commodity avg `0.1212` n `12`; crypto_alt avg `0.303` n `232`; crypto_major avg `0.0775` n `8`; equity avg `-0.0409` n `134`; fx avg `-0.0108` n `6`; index avg `-0.017` n `26`; metal avg `-0.0839` n `20`; unknown avg `0.5195` n `790`
- 4h: commodity avg `-0.1258` n `12`; crypto_alt avg `-0.2168` n `232`; crypto_major avg `-0.5562` n `8`; equity avg `0.0003` n `134`; fx avg `-0.1417` n `6`; index avg `0.0212` n `26`; metal avg `0.0466` n `20`; unknown avg `1.7905` n `758`
- 24h: commodity avg `-0.0405` n `12`; crypto_alt avg `0.2597` n `232`; crypto_major avg `-1.0042` n `8`; equity avg `0.3383` n `134`; fx avg `-0.1444` n `6`; index avg `0.0304` n `26`; metal avg `-0.0936` n `20`; unknown avg `75.3391` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
