# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T08:22:30.324031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0622` n `12`; crypto_alt avg `-0.1573` n `232`; crypto_major avg `-0.2231` n `8`; equity avg `-0.1249` n `132`; fx avg `-0.0185` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.3564` n `792`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.11` n `232`; crypto_major avg `-0.3675` n `8`; equity avg `-0.2598` n `132`; fx avg `-0.0207` n `6`; index avg `-0.032` n `26`; metal avg `-0.0263` n `20`; unknown avg `-0.0127` n `790`
- 4h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.2739` n `232`; crypto_major avg `-0.1327` n `8`; equity avg `-0.0148` n `132`; fx avg `-0.1158` n `6`; index avg `0.01` n `26`; metal avg `0.1637` n `20`; unknown avg `0.0904` n `770`
- 24h: commodity avg `0.5502` n `12`; crypto_alt avg `-0.0434` n `232`; crypto_major avg `-1.3972` n `8`; equity avg `-1.9008` n `130`; fx avg `-0.1944` n `6`; index avg `-0.3357` n `26`; metal avg `-0.6392` n `20`; unknown avg `-0.1994` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
