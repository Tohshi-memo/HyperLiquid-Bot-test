# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T03:52:32.330830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `13`; crypto_alt avg `0.0566` n `235`; crypto_major avg `0.0188` n `8`; equity avg `0.0736` n `150`; fx avg `0.0018` n `6`; index avg `0.0086` n `26`; metal avg `0.0217` n `20`; unknown avg `0.3377` n `1078`
- 1h: commodity avg `-0.0951` n `13`; crypto_alt avg `0.3622` n `235`; crypto_major avg `0.0295` n `8`; equity avg `0.0448` n `150`; fx avg `-0.003` n `6`; index avg `0.012` n `26`; metal avg `0.0121` n `20`; unknown avg `1.5917` n `1076`
- 4h: commodity avg `-0.2839` n `13`; crypto_alt avg `1.4113` n `235`; crypto_major avg `0.809` n `8`; equity avg `0.6178` n `150`; fx avg `0.0057` n `6`; index avg `0.1136` n `26`; metal avg `0.3415` n `20`; unknown avg `1.3276` n `1069`
- 24h: commodity avg `0.1143` n `13`; crypto_alt avg `-1.8441` n `235`; crypto_major avg `-2.5362` n `8`; equity avg `-1.7309` n `150`; fx avg `0.1063` n `6`; index avg `-0.1539` n `26`; metal avg `0.1142` n `20`; unknown avg `6.3859` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
