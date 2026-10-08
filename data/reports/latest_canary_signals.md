# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T10:37:26.600706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `13`; crypto_alt avg `-0.476` n `235`; crypto_major avg `-0.3693` n `8`; equity avg `-0.3231` n `150`; fx avg `0.017` n `6`; index avg `-0.0608` n `26`; metal avg `-0.1219` n `20`; unknown avg `1.378` n `1077`
- 1h: commodity avg `0.234` n `13`; crypto_alt avg `-0.5565` n `235`; crypto_major avg `-0.5222` n `8`; equity avg `-0.5337` n `150`; fx avg `0.0117` n `6`; index avg `-0.1087` n `26`; metal avg `-0.1524` n `20`; unknown avg `0.9962` n `1075`
- 4h: commodity avg `0.323` n `13`; crypto_alt avg `0.5278` n `235`; crypto_major avg `-0.02` n `8`; equity avg `-0.5871` n `150`; fx avg `0.0685` n `6`; index avg `-0.1237` n `26`; metal avg `-0.1543` n `20`; unknown avg `1.4761` n `1059`
- 24h: commodity avg `0.9152` n `13`; crypto_alt avg `0.2905` n `235`; crypto_major avg `-1.5632` n `8`; equity avg `-1.7631` n `150`; fx avg `0.0173` n `6`; index avg `-0.3338` n `26`; metal avg `-0.2073` n `20`; unknown avg `416.7056` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
