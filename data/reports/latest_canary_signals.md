# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T21:52:33.046870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0056` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `-0.1159` n `231`; crypto_major avg `-0.1119` n `8`; equity avg `0.0079` n `128`; fx avg `0.0064` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0223` n `20`; unknown avg `0.0264` n `793`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.2451` n `231`; crypto_major avg `-0.4765` n `8`; equity avg `-0.0503` n `128`; fx avg `0.0124` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0674` n `20`; unknown avg `0.1604` n `789`
- 4h: commodity avg `0.4542` n `12`; crypto_alt avg `-0.7196` n `231`; crypto_major avg `-1.07` n `8`; equity avg `-0.1889` n `128`; fx avg `0.002` n `6`; index avg `-0.0644` n `26`; metal avg `-0.1286` n `20`; unknown avg `0.2065` n `791`
- 24h: commodity avg `0.5016` n `12`; crypto_alt avg `0.8625` n `231`; crypto_major avg `-0.1074` n `8`; equity avg `0.0047` n `128`; fx avg `0.0401` n `6`; index avg `0.0107` n `26`; metal avg `-0.0211` n `20`; unknown avg `0.061` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
