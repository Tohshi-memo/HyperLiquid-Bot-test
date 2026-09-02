# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T17:37:31.666189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1783` n `232`; crypto_major avg `0.2318` n `8`; equity avg `-0.0212` n `133`; fx avg `0.0045` n `6`; index avg `-0.0091` n `26`; metal avg `0.0189` n `20`; unknown avg `0.0654` n `792`
- 1h: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.354` n `232`; crypto_major avg `-0.3693` n `8`; equity avg `-0.0169` n `133`; fx avg `-0.0053` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.1621` n `790`
- 4h: commodity avg `0.3165` n `12`; crypto_alt avg `0.3876` n `232`; crypto_major avg `0.475` n `8`; equity avg `0.4456` n `133`; fx avg `-0.0267` n `6`; index avg `0.1031` n `26`; metal avg `-0.037` n `20`; unknown avg `0.4668` n `789`
- 24h: commodity avg `0.3288` n `12`; crypto_alt avg `-0.9713` n `232`; crypto_major avg `-1.3521` n `8`; equity avg `-0.0355` n `133`; fx avg `-0.3552` n `6`; index avg `0.0421` n `26`; metal avg `0.159` n `20`; unknown avg `0.0475` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0418`, n `668`, weak_sample_signal
