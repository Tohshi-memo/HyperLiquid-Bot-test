# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T21:07:25.041835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4886` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.5378` n `231`; crypto_major avg `-0.5832` n `8`; equity avg `-0.0757` n `128`; fx avg `0.0094` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0233` n `20`; unknown avg `0.3491` n `789`
- 1h: commodity avg `0.0732` n `12`; crypto_alt avg `-0.9448` n `231`; crypto_major avg `-0.9946` n `8`; equity avg `-0.1408` n `128`; fx avg `0.0063` n `6`; index avg `-0.0483` n `26`; metal avg `-0.0485` n `20`; unknown avg `0.4948` n `789`
- 4h: commodity avg `0.4293` n `12`; crypto_alt avg `-1.2501` n `231`; crypto_major avg `-1.5471` n `8`; equity avg `-0.2313` n `128`; fx avg `-0.0039` n `6`; index avg `-0.0585` n `26`; metal avg `-0.0931` n `20`; unknown avg `0.6681` n `791`
- 24h: commodity avg `0.4741` n `12`; crypto_alt avg `0.6562` n `231`; crypto_major avg `-0.2195` n `8`; equity avg `-0.0076` n `128`; fx avg `0.0352` n `6`; index avg `0.0035` n `26`; metal avg `0.0254` n `20`; unknown avg `0.029` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
