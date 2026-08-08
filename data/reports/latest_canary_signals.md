# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T02:37:30.531778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0148` n `230`; crypto_major avg `0.0295` n `8`; equity avg `-0.0588` n `112`; fx avg `-0.0055` n `6`; index avg `0.0013` n `25`; metal avg `0.016` n `20`; unknown avg `0.0232` n `783`
- 1h: commodity avg `-0.0297` n `12`; crypto_alt avg `0.0159` n `230`; crypto_major avg `-0.0035` n `8`; equity avg `-0.017` n `112`; fx avg `-0.0088` n `6`; index avg `0.0248` n `25`; metal avg `-0.0307` n `20`; unknown avg `-0.1376` n `783`
- 4h: commodity avg `0.0276` n `12`; crypto_alt avg `0.3106` n `230`; crypto_major avg `0.2324` n `8`; equity avg `0.1166` n `112`; fx avg `-0.0036` n `6`; index avg `-0.0025` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.3434` n `782`
- 24h: commodity avg `-0.1726` n `12`; crypto_alt avg `-0.5285` n `230`; crypto_major avg `0.1875` n `8`; equity avg `1.815` n `112`; fx avg `-0.0726` n `6`; index avg `0.2451` n `25`; metal avg `0.3674` n `20`; unknown avg `-0.0648` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
