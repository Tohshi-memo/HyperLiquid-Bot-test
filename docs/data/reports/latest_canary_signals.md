# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T13:07:26.301376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.0966` n `235`; crypto_major avg `0.0081` n `8`; equity avg `-0.0048` n `150`; fx avg `0.0` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.5816` n `1115`
- 1h: commodity avg `0.1007` n `13`; crypto_alt avg `-0.076` n `235`; crypto_major avg `0.0382` n `8`; equity avg `0.0069` n `150`; fx avg `0.002` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0073` n `20`; unknown avg `0.6991` n `1115`
- 4h: commodity avg `-0.1517` n `13`; crypto_alt avg `-0.1926` n `235`; crypto_major avg `-0.1675` n `8`; equity avg `0.026` n `150`; fx avg `0.0083` n `6`; index avg `0.0057` n `26`; metal avg `-0.0093` n `20`; unknown avg `0.911` n `1109`
- 24h: commodity avg `-0.156` n `13`; crypto_alt avg `1.5343` n `235`; crypto_major avg `-0.0606` n `8`; equity avg `-0.2568` n `150`; fx avg `0.0212` n `6`; index avg `-0.023` n `26`; metal avg `0.1` n `20`; unknown avg `632.2224` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
