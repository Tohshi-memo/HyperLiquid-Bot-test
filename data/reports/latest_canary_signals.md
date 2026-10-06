# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T04:07:28.706149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0324` n `13`; crypto_alt avg `0.1673` n `235`; crypto_major avg `0.1466` n `8`; equity avg `0.02` n `149`; fx avg `0.0168` n `6`; index avg `0.0102` n `26`; metal avg `0.0002` n `20`; unknown avg `0.2146` n `1066`
- 1h: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.0213` n `235`; crypto_major avg `0.0122` n `8`; equity avg `0.0745` n `149`; fx avg `0.0082` n `6`; index avg `0.0209` n `26`; metal avg `-0.0204` n `20`; unknown avg `0.1774` n `1066`
- 4h: commodity avg `0.059` n `13`; crypto_alt avg `-1.4348` n `235`; crypto_major avg `-0.4574` n `8`; equity avg `-0.0939` n `149`; fx avg `-0.0022` n `6`; index avg `-0.0158` n `26`; metal avg `-0.0419` n `20`; unknown avg `0.1219` n `1066`
- 24h: commodity avg `0.0125` n `13`; crypto_alt avg `-0.727` n `235`; crypto_major avg `-0.039` n `8`; equity avg `0.1327` n `149`; fx avg `0.0796` n `6`; index avg `0.1247` n `26`; metal avg `0.0068` n `20`; unknown avg `591.744` n `846`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
