# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T11:52:30.604072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0377` n `13`; crypto_alt avg `0.0771` n `235`; crypto_major avg `0.0305` n `8`; equity avg `0.0661` n `150`; fx avg `0.0003` n `6`; index avg `0.0261` n `26`; metal avg `0.0251` n `20`; unknown avg `1.7756` n `1077`
- 1h: commodity avg `-0.1335` n `13`; crypto_alt avg `-0.1854` n `235`; crypto_major avg `-0.4299` n `8`; equity avg `0.091` n `150`; fx avg `-0.0261` n `6`; index avg `0.0456` n `26`; metal avg `-0.0063` n `20`; unknown avg `1.1532` n `1075`
- 4h: commodity avg `0.1294` n `13`; crypto_alt avg `-0.2765` n `235`; crypto_major avg `-0.9891` n `8`; equity avg `-0.3168` n `150`; fx avg `0.0206` n `6`; index avg `-0.0241` n `26`; metal avg `-0.0539` n `20`; unknown avg `2.8374` n `1059`
- 24h: commodity avg `0.6569` n `13`; crypto_alt avg `0.5456` n `235`; crypto_major avg `-1.8865` n `8`; equity avg `-1.2132` n `150`; fx avg `0.0269` n `6`; index avg `-0.1786` n `26`; metal avg `-0.0944` n `20`; unknown avg `416.5116` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
