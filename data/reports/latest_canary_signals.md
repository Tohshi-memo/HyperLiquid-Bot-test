# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T06:52:28.734512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `0.2115` n `231`; crypto_major avg `0.13` n `8`; equity avg `-0.0239` n `127`; fx avg `0.0009` n `6`; index avg `0.022` n `26`; metal avg `0.2072` n `20`; unknown avg `0.0226` n `792`
- 1h: commodity avg `-0.0628` n `12`; crypto_alt avg `0.4403` n `231`; crypto_major avg `0.2985` n `8`; equity avg `0.0396` n `127`; fx avg `-0.025` n `6`; index avg `0.0273` n `26`; metal avg `0.3973` n `20`; unknown avg `0.0136` n `760`
- 4h: commodity avg `-0.0692` n `12`; crypto_alt avg `0.6988` n `231`; crypto_major avg `0.4524` n `8`; equity avg `-0.3676` n `127`; fx avg `-0.0686` n `6`; index avg `-0.0413` n `26`; metal avg `0.3771` n `20`; unknown avg `-0.0074` n `760`
- 24h: commodity avg `0.3681` n `12`; crypto_alt avg `0.7274` n `231`; crypto_major avg `1.8574` n `8`; equity avg `-0.3744` n `127`; fx avg `-0.09` n `6`; index avg `0.0461` n `26`; metal avg `0.4338` n `20`; unknown avg `0.4533` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
