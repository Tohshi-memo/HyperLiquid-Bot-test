# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T23:52:26.397774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1015` n `13`; crypto_alt avg `-0.2926` n `235`; crypto_major avg `-0.1993` n `8`; equity avg `-0.0799` n `150`; fx avg `-0.0056` n `6`; index avg `-0.021` n `26`; metal avg `0.0128` n `20`; unknown avg `1.1809` n `1077`
- 1h: commodity avg `0.1159` n `13`; crypto_alt avg `-0.1788` n `235`; crypto_major avg `-0.1314` n `8`; equity avg `-0.2265` n `150`; fx avg `0.01` n `6`; index avg `-0.0414` n `26`; metal avg `0.0617` n `20`; unknown avg `1.0265` n `1075`
- 4h: commodity avg `0.0397` n `13`; crypto_alt avg `0.4602` n `235`; crypto_major avg `0.3125` n `8`; equity avg `0.1991` n `150`; fx avg `0.0096` n `6`; index avg `0.0284` n `26`; metal avg `0.1155` n `20`; unknown avg `-0.1356` n `1007`
- 24h: commodity avg `0.6192` n `13`; crypto_alt avg `-3.3322` n `235`; crypto_major avg `-3.6139` n `8`; equity avg `-2.9789` n `150`; fx avg `0.0597` n `6`; index avg `-0.4119` n `26`; metal avg `0.0895` n `20`; unknown avg `6.5673` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
