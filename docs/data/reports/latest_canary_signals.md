# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T22:52:25.054646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.1197` n `231`; crypto_major avg `-0.161` n `8`; equity avg `-0.0406` n `124`; fx avg `-0.0063` n `6`; index avg `-0.0099` n `25`; metal avg `-0.0156` n `20`; unknown avg `0.0068` n `795`
- 1h: commodity avg `0.0055` n `12`; crypto_alt avg `0.4389` n `231`; crypto_major avg `0.1419` n `8`; equity avg `0.076` n `124`; fx avg `-0.0144` n `6`; index avg `0.0581` n `25`; metal avg `0.1068` n `20`; unknown avg `-0.0741` n `795`
- 4h: commodity avg `0.0313` n `12`; crypto_alt avg `1.4822` n `231`; crypto_major avg `1.1136` n `8`; equity avg `1.7164` n `124`; fx avg `-0.0233` n `6`; index avg `0.295` n `25`; metal avg `0.0969` n `20`; unknown avg `0.3708` n `795`
- 24h: commodity avg `0.3297` n `12`; crypto_alt avg `0.8452` n `231`; crypto_major avg `0.3902` n `8`; equity avg `1.4196` n `124`; fx avg `-0.072` n `6`; index avg `0.3089` n `25`; metal avg `-0.3388` n `20`; unknown avg `0.8871` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
