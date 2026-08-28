# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T15:52:25.413653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.061` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.9943` n `231`; crypto_major avg `-0.9177` n `8`; equity avg `-0.6634` n `127`; fx avg `0.0017` n `6`; index avg `-0.1075` n `26`; metal avg `-0.1145` n `20`; unknown avg `3.2883` n `793`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `-1.1027` n `231`; crypto_major avg `-1.1927` n `8`; equity avg `-0.8261` n `127`; fx avg `0.0135` n `6`; index avg `-0.1317` n `26`; metal avg `-0.1546` n `20`; unknown avg `3.2874` n `793`
- 4h: commodity avg `0.0151` n `12`; crypto_alt avg `-1.1369` n `231`; crypto_major avg `-0.9358` n `8`; equity avg `-0.9633` n `127`; fx avg `-0.0214` n `6`; index avg `-0.0296` n `26`; metal avg `-0.1752` n `20`; unknown avg `-0.3826` n `792`
- 24h: commodity avg `-0.0353` n `12`; crypto_alt avg `-2.3825` n `231`; crypto_major avg `-2.2918` n `8`; equity avg `-1.47` n `127`; fx avg `-0.0631` n `6`; index avg `-0.0341` n `26`; metal avg `0.3508` n `20`; unknown avg `-0.0049` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
