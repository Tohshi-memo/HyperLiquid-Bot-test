# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T13:22:25.149920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1184` n `232`; crypto_major avg `-0.015` n `8`; equity avg `0.1062` n `132`; fx avg `0.0054` n `6`; index avg `0.0134` n `26`; metal avg `0.0439` n `20`; unknown avg `-0.0272` n `792`
- 1h: commodity avg `0.0766` n `12`; crypto_alt avg `-0.3503` n `232`; crypto_major avg `-0.2329` n `8`; equity avg `-0.07` n `132`; fx avg `0.0048` n `6`; index avg `-0.0437` n `26`; metal avg `0.0726` n `20`; unknown avg `-0.0494` n `790`
- 4h: commodity avg `-0.1301` n `12`; crypto_alt avg `-0.6579` n `232`; crypto_major avg `-0.2564` n `8`; equity avg `0.5228` n `132`; fx avg `-0.0651` n `6`; index avg `0.1067` n `26`; metal avg `0.3776` n `20`; unknown avg `-0.0986` n `790`
- 24h: commodity avg `0.549` n `12`; crypto_alt avg `-1.0855` n `232`; crypto_major avg `-1.9005` n `8`; equity avg `-0.8974` n `131`; fx avg `-0.268` n `6`; index avg `-0.1225` n `26`; metal avg `0.1051` n `20`; unknown avg `-0.0019` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
