# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T12:22:30.319501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0909` n `12`; crypto_alt avg `0.3444` n `232`; crypto_major avg `0.3032` n `8`; equity avg `0.2226` n `132`; fx avg `-0.0034` n `6`; index avg `0.0285` n `26`; metal avg `0.0313` n `20`; unknown avg `0.6096` n `792`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.6024` n `232`; crypto_major avg `0.6339` n `8`; equity avg `0.5972` n `132`; fx avg `-0.0213` n `6`; index avg `0.1087` n `26`; metal avg `0.1527` n `20`; unknown avg `0.3239` n `790`
- 4h: commodity avg `-0.1798` n `12`; crypto_alt avg `-0.8779` n `232`; crypto_major avg `-0.6603` n `8`; equity avg `0.2322` n `132`; fx avg `-0.0674` n `6`; index avg `0.0602` n `26`; metal avg `0.2185` n `20`; unknown avg `0.5814` n `790`
- 24h: commodity avg `0.491` n `12`; crypto_alt avg `-1.0561` n `232`; crypto_major avg `-2.0501` n `8`; equity avg `-0.7371` n `130`; fx avg `-0.288` n `6`; index avg `-0.0917` n `26`; metal avg `-0.1635` n `20`; unknown avg `0.0008` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
