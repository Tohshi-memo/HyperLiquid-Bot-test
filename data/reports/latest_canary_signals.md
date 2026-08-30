# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T21:22:21.933476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1164` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.1099` n `231`; crypto_major avg `0.0207` n `8`; equity avg `0.0085` n `128`; fx avg `-0.0069` n `6`; index avg `0.008` n `26`; metal avg `-0.0029` n `20`; unknown avg `1.0027` n `793`
- 1h: commodity avg `0.0633` n `12`; crypto_alt avg `-0.8277` n `231`; crypto_major avg `-0.9308` n `8`; equity avg `-0.1259` n `128`; fx avg `-0.0006` n `6`; index avg `-0.0364` n `26`; metal avg `-0.0259` n `20`; unknown avg `0.4328` n `789`
- 4h: commodity avg `0.4649` n `12`; crypto_alt avg `-0.9676` n `231`; crypto_major avg `-1.1678` n `8`; equity avg `-0.216` n `128`; fx avg `-0.0134` n `6`; index avg `-0.0514` n `26`; metal avg `-0.0848` n `20`; unknown avg `0.1556` n `791`
- 24h: commodity avg `0.4984` n `12`; crypto_alt avg `0.7231` n `231`; crypto_major avg `-0.2246` n `8`; equity avg `-0.001` n `128`; fx avg `0.0301` n `6`; index avg `0.0089` n `26`; metal avg `0.0193` n `20`; unknown avg `0.038` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
