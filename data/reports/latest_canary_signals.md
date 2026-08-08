# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T02:22:32.400212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.0118` n `230`; crypto_major avg `-0.0645` n `8`; equity avg `-0.0458` n `112`; fx avg `0.0005` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.0624` n `783`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.1417` n `230`; crypto_major avg `0.0271` n `8`; equity avg `0.0732` n `112`; fx avg `0.0014` n `6`; index avg `0.0245` n `25`; metal avg `-0.0623` n `20`; unknown avg `-0.1844` n `783`
- 4h: commodity avg `0.0284` n `12`; crypto_alt avg `0.1971` n `230`; crypto_major avg `0.1126` n `8`; equity avg `0.1877` n `112`; fx avg `0.0053` n `6`; index avg `-0.0024` n `25`; metal avg `0.006` n `20`; unknown avg `-0.2376` n `782`
- 24h: commodity avg `-0.1794` n `12`; crypto_alt avg `-0.4874` n `230`; crypto_major avg `0.0974` n `8`; equity avg `1.888` n `112`; fx avg `-0.0577` n `6`; index avg `0.22` n `25`; metal avg `0.3209` n `20`; unknown avg `-0.0628` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
