# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T08:07:27.656755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0577` n `12`; crypto_alt avg `0.1257` n `232`; crypto_major avg `0.0053` n `8`; equity avg `-0.0267` n `132`; fx avg `0.0072` n `6`; index avg `0.0164` n `26`; metal avg `0.0169` n `20`; unknown avg `-0.0153` n `790`
- 1h: commodity avg `-0.043` n `12`; crypto_alt avg `-0.0703` n `232`; crypto_major avg `-0.2081` n `8`; equity avg `-0.092` n `132`; fx avg `-0.0047` n `6`; index avg `-0.0226` n `26`; metal avg `-0.0238` n `20`; unknown avg `0.2298` n `790`
- 4h: commodity avg `-0.1504` n `12`; crypto_alt avg `0.3921` n `232`; crypto_major avg `0.0633` n `8`; equity avg `0.0968` n `132`; fx avg `-0.0988` n `6`; index avg `0.0223` n `26`; metal avg `0.1749` n `20`; unknown avg `0.1943` n `770`
- 24h: commodity avg `0.4647` n `12`; crypto_alt avg `-0.2442` n `232`; crypto_major avg `-1.3367` n `8`; equity avg `-1.9614` n `130`; fx avg `-0.1763` n `6`; index avg `-0.3555` n `26`; metal avg `-0.7289` n `20`; unknown avg `-0.5119` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
