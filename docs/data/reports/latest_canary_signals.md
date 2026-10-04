# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T23:22:35.793739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0154` n `13`; crypto_alt avg `0.1073` n `235`; crypto_major avg `0.0826` n `8`; equity avg `0.0404` n `144`; fx avg `-0.0186` n `6`; index avg `0.0004` n `26`; metal avg `0.0106` n `20`; unknown avg `0.6644` n `1078`
- 1h: commodity avg `-0.0696` n `13`; crypto_alt avg `0.0483` n `235`; crypto_major avg `-0.2036` n `8`; equity avg `0.0828` n `144`; fx avg `-0.0242` n `6`; index avg `0.0125` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.2109` n `1076`
- 4h: commodity avg `-0.195` n `13`; crypto_alt avg `0.3439` n `235`; crypto_major avg `0.6532` n `8`; equity avg `0.2706` n `144`; fx avg `-0.0123` n `6`; index avg `0.0254` n `26`; metal avg `0.0725` n `20`; unknown avg `0.079` n `1012`
- 24h: commodity avg `-0.2456` n `13`; crypto_alt avg `0.9444` n `235`; crypto_major avg `1.6859` n `8`; equity avg `0.3454` n `144`; fx avg `-0.0008` n `6`; index avg `0.0042` n `26`; metal avg `0.073` n `20`; unknown avg `0.3333` n `976`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
