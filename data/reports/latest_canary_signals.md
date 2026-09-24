# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T03:07:33.674045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.0558` n `234`; crypto_major avg `-0.0486` n `8`; equity avg `-0.0644` n `141`; fx avg `0.0104` n `6`; index avg `-0.014` n `26`; metal avg `-0.0022` n `20`; unknown avg `1.6793` n `943`
- 1h: commodity avg `-0.1201` n `12`; crypto_alt avg `1.5243` n `234`; crypto_major avg `0.9364` n `8`; equity avg `0.0706` n `141`; fx avg `0.0234` n `6`; index avg `0.0045` n `26`; metal avg `0.1149` n `20`; unknown avg `3.0423` n `943`
- 4h: commodity avg `-0.1` n `12`; crypto_alt avg `1.0885` n `234`; crypto_major avg `0.0611` n `8`; equity avg `-0.2788` n `141`; fx avg `0.0368` n `6`; index avg `-0.058` n `26`; metal avg `-0.0684` n `20`; unknown avg `1.6562` n `937`
- 24h: commodity avg `0.3991` n `12`; crypto_alt avg `-3.8057` n `234`; crypto_major avg `-3.6293` n `8`; equity avg `-1.528` n `140`; fx avg `0.1002` n `6`; index avg `-0.3141` n `26`; metal avg `-0.6004` n `20`; unknown avg `585.1975` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
