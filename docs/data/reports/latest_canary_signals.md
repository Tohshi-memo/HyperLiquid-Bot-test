# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T18:22:23.914890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.1967` n `231`; crypto_major avg `0.0406` n `8`; equity avg `-0.0174` n `128`; fx avg `-0.0018` n `6`; index avg `-0.0047` n `26`; metal avg `0.007` n `20`; unknown avg `0.0067` n `792`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `0.0808` n `231`; crypto_major avg `0.0647` n `8`; equity avg `-0.0077` n `128`; fx avg `0.0083` n `6`; index avg `-0.0091` n `26`; metal avg `0.0109` n `20`; unknown avg `-0.0058` n `792`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.1463` n `231`; crypto_major avg `0.4303` n `8`; equity avg `0.0046` n `128`; fx avg `0.0094` n `6`; index avg `0.0009` n `26`; metal avg `0.0612` n `20`; unknown avg `0.0167` n `778`
- 24h: commodity avg `0.0155` n `12`; crypto_alt avg `1.1736` n `231`; crypto_major avg `1.1133` n `8`; equity avg `0.1183` n `128`; fx avg `-0.0384` n `6`; index avg `0.01` n `26`; metal avg `0.0961` n `20`; unknown avg `0.1098` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
