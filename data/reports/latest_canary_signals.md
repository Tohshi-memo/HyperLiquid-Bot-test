# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T17:22:30.986288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `13`; crypto_alt avg `-0.0948` n `235`; crypto_major avg `-0.0364` n `8`; equity avg `-0.0225` n `151`; fx avg `0.0117` n `6`; index avg `0.0006` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.6267` n `1134`
- 1h: commodity avg `0.0051` n `13`; crypto_alt avg `-0.8434` n `235`; crypto_major avg `-0.6735` n `8`; equity avg `-0.2821` n `151`; fx avg `0.0076` n `6`; index avg `-0.0392` n `26`; metal avg `-0.0213` n `20`; unknown avg `0.096` n `1132`
- 4h: commodity avg `0.2412` n `13`; crypto_alt avg `-1.7369` n `235`; crypto_major avg `-0.9991` n `8`; equity avg `-1.7531` n `151`; fx avg `-0.0373` n `6`; index avg `-0.1201` n `26`; metal avg `-0.0979` n `20`; unknown avg `0.0355` n `1074`
- 24h: commodity avg `0.5039` n `13`; crypto_alt avg `-3.3495` n `235`; crypto_major avg `-2.363` n `8`; equity avg `-3.4177` n `151`; fx avg `-0.1506` n `6`; index avg `-0.3242` n `26`; metal avg `-0.1831` n `20`; unknown avg `-0.1905` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.209`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.193`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1492`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0918`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0893`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0871`, n `666`, weak_sample_signal
