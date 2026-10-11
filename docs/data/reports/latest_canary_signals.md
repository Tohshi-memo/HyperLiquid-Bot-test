# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T15:07:28.720952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.092` n `13`; crypto_alt avg `0.0072` n `235`; crypto_major avg `0.0246` n `8`; equity avg `-0.0036` n `150`; fx avg `0.0044` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.2142` n `1132`
- 1h: commodity avg `-0.0478` n `13`; crypto_alt avg `0.7939` n `235`; crypto_major avg `0.2999` n `8`; equity avg `0.0306` n `150`; fx avg `0.0168` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0028` n `20`; unknown avg `21.5096` n `1132`
- 4h: commodity avg `-0.1138` n `13`; crypto_alt avg `1.2842` n `235`; crypto_major avg `0.4137` n `8`; equity avg `0.107` n `150`; fx avg `0.001` n `6`; index avg `0.0057` n `26`; metal avg `0.0078` n `20`; unknown avg `1.1878` n `1053`
- 24h: commodity avg `0.2254` n `13`; crypto_alt avg `1.205` n `235`; crypto_major avg `-0.3528` n `8`; equity avg `0.0559` n `150`; fx avg `0.0169` n `6`; index avg `-0.0108` n `26`; metal avg `0.005` n `20`; unknown avg `1.589` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
