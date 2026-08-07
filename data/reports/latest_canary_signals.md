# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T20:07:26.938774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.0658` n `230`; crypto_major avg `0.007` n `8`; equity avg `0.111` n `112`; fx avg `0.0119` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0496` n `20`; unknown avg `-0.0555` n `782`
- 1h: commodity avg `-0.0834` n `12`; crypto_alt avg `-0.0407` n `230`; crypto_major avg `0.2461` n `8`; equity avg `0.1199` n `112`; fx avg `-0.0065` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0746` n `20`; unknown avg `-0.0586` n `782`
- 4h: commodity avg `-0.2731` n `12`; crypto_alt avg `-0.2953` n `230`; crypto_major avg `-0.3713` n `8`; equity avg `-0.1489` n `112`; fx avg `-0.0108` n `6`; index avg `0.0077` n `25`; metal avg `-0.048` n `20`; unknown avg `-0.1885` n `782`
- 24h: commodity avg `-0.0637` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `0.0752` n `8`; equity avg `2.0789` n `112`; fx avg `-0.1516` n `6`; index avg `0.1065` n `25`; metal avg `0.3488` n `20`; unknown avg `-0.0184` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
