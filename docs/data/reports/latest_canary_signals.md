# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T15:22:24.135254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `-0.045` n `235`; crypto_major avg `0.049` n `8`; equity avg `0.0105` n `143`; fx avg `0.0054` n `6`; index avg `0.003` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.186` n `1046`
- 1h: commodity avg `0.0111` n `13`; crypto_alt avg `0.2574` n `235`; crypto_major avg `0.2368` n `8`; equity avg `0.012` n `143`; fx avg `0.0043` n `6`; index avg `0.0033` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.0307` n `972`
- 4h: commodity avg `0.1964` n `13`; crypto_alt avg `0.634` n `235`; crypto_major avg `0.4902` n `8`; equity avg `0.0288` n `143`; fx avg `-0.0097` n `6`; index avg `0.0129` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.172` n `946`
- 24h: commodity avg `0.6495` n `13`; crypto_alt avg `-1.1008` n `235`; crypto_major avg `-0.6455` n `8`; equity avg `0.0983` n `143`; fx avg `-0.0416` n `6`; index avg `0.06` n `26`; metal avg `0.0457` n `20`; unknown avg `0.5193` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
