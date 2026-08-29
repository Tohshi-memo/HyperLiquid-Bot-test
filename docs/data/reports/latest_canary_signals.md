# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T17:52:24.631864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0302` n `231`; crypto_major avg `0.1058` n `8`; equity avg `0.0113` n `128`; fx avg `0.0047` n `6`; index avg `-0.0006` n `26`; metal avg `0.0006` n `20`; unknown avg `-0.0525` n `792`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.4035` n `231`; crypto_major avg `-0.2421` n `8`; equity avg `-0.0046` n `128`; fx avg `0.0125` n `6`; index avg `0.0007` n `26`; metal avg `0.0079` n `20`; unknown avg `-0.0847` n `792`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `0.312` n `231`; crypto_major avg `0.5699` n `8`; equity avg `0.0372` n `128`; fx avg `0.0102` n `6`; index avg `0.0132` n `26`; metal avg `0.0606` n `20`; unknown avg `0.1459` n `778`
- 24h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.2085` n `231`; crypto_major avg `0.2859` n `8`; equity avg `0.0487` n `128`; fx avg `-0.0305` n `6`; index avg `0.0021` n `26`; metal avg `-0.0256` n `20`; unknown avg `-0.0245` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.225`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
