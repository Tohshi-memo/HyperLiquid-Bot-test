# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T06:22:30.185286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.2878` n `232`; crypto_major avg `-0.2321` n `8`; equity avg `-0.1114` n `132`; fx avg `0.0239` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0157` n `20`; unknown avg `0.8482` n `790`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `-0.367` n `232`; crypto_major avg `-0.2287` n `8`; equity avg `-0.0964` n `132`; fx avg `-0.0369` n `6`; index avg `-0.0406` n `26`; metal avg `0.0731` n `20`; unknown avg `0.2995` n `772`
- 4h: commodity avg `-0.067` n `12`; crypto_alt avg `0.6634` n `232`; crypto_major avg `0.4264` n `8`; equity avg `-0.0337` n `132`; fx avg `-0.1051` n `6`; index avg `-0.0697` n `26`; metal avg `0.159` n `20`; unknown avg `0.1427` n `772`
- 24h: commodity avg `0.8287` n `12`; crypto_alt avg `-0.9273` n `232`; crypto_major avg `-1.8654` n `8`; equity avg `-2.7023` n `130`; fx avg `-0.1463` n `6`; index avg `-0.514` n `26`; metal avg `-0.9352` n `20`; unknown avg `-0.3453` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
