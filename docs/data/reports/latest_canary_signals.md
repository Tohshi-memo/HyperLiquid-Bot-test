# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T22:22:26.672540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4637` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1234` n `12`; crypto_alt avg `-0.5542` n `231`; crypto_major avg `-0.5569` n `8`; equity avg `-0.044` n `128`; fx avg `0.0033` n `6`; index avg `0.019` n `26`; metal avg `0.1045` n `20`; unknown avg `7.1809` n `793`
- 1h: commodity avg `-0.1426` n `12`; crypto_alt avg `-0.0875` n `231`; crypto_major avg `-0.3074` n `8`; equity avg `-0.1267` n `128`; fx avg `-0.0053` n `6`; index avg `-0.0531` n `26`; metal avg `-0.0977` n `20`; unknown avg `6.9165` n `791`
- 4h: commodity avg `0.3043` n `12`; crypto_alt avg `-1.0271` n `231`; crypto_major avg `-1.5698` n `8`; equity avg `-0.3153` n `128`; fx avg `-0.0109` n `6`; index avg `-0.1061` n `26`; metal avg `-0.1708` n `20`; unknown avg `1.2033` n `791`
- 24h: commodity avg `0.3532` n `12`; crypto_alt avg `0.7697` n `231`; crypto_major avg `-0.4409` n `8`; equity avg `-0.1349` n `128`; fx avg `0.0224` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0702` n `20`; unknown avg `0.0718` n `755`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
