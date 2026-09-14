# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T22:07:32.220023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.0297` n `233`; crypto_major avg `-0.0248` n `8`; equity avg `0.0005` n `136`; fx avg `-0.0101` n `6`; index avg `-0.0112` n `27`; metal avg `0.002` n `20`; unknown avg `0.2732` n `898`
- 1h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.4708` n `233`; crypto_major avg `-0.5443` n `8`; equity avg `-0.0344` n `136`; fx avg `0.0047` n `6`; index avg `-0.014` n `27`; metal avg `0.0055` n `20`; unknown avg `0.7848` n `898`
- 4h: commodity avg `0.0507` n `12`; crypto_alt avg `-0.4563` n `233`; crypto_major avg `-0.2271` n `8`; equity avg `-0.5611` n `136`; fx avg `-0.0019` n `6`; index avg `-0.0963` n `27`; metal avg `-0.0967` n `20`; unknown avg `0.2718` n `866`
- 24h: commodity avg `-0.1038` n `12`; crypto_alt avg `0.8804` n `233`; crypto_major avg `2.4091` n `8`; equity avg `-0.4847` n `136`; fx avg `0.029` n `6`; index avg `-0.141` n `27`; metal avg `-0.3321` n `20`; unknown avg `0.8483` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
