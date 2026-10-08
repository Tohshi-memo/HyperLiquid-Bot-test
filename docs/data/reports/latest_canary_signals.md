# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T01:07:27.445592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0321` n `13`; crypto_alt avg `0.3651` n `235`; crypto_major avg `0.2499` n `8`; equity avg `0.0682` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0024` n `26`; metal avg `0.2228` n `20`; unknown avg `0.1103` n `1075`
- 1h: commodity avg `0.0447` n `13`; crypto_alt avg `0.6848` n `235`; crypto_major avg `0.4318` n `8`; equity avg `-0.0845` n `150`; fx avg `-0.0249` n `6`; index avg `-0.0546` n `26`; metal avg `0.2816` n `20`; unknown avg `0.1863` n `1075`
- 4h: commodity avg `0.141` n `13`; crypto_alt avg `1.2586` n `235`; crypto_major avg `0.5168` n `8`; equity avg `0.1019` n `150`; fx avg `-0.0636` n `6`; index avg `-0.0385` n `26`; metal avg `0.2676` n `20`; unknown avg `0.0839` n `1069`
- 24h: commodity avg `0.3251` n `13`; crypto_alt avg `-2.7411` n `235`; crypto_major avg `-2.7699` n `8`; equity avg `-1.3514` n `150`; fx avg `-0.2042` n `6`; index avg `-0.2736` n `26`; metal avg `-0.3714` n `20`; unknown avg `247.66` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
