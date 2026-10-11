# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T10:07:32.058075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `0.0833` n `235`; crypto_major avg `0.0355` n `8`; equity avg `0.0099` n `150`; fx avg `0.0103` n `6`; index avg `0.0017` n `26`; metal avg `-0.0006` n `20`; unknown avg `5.5836` n `1115`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `-0.0501` n `235`; crypto_major avg `-0.0156` n `8`; equity avg `0.0114` n `150`; fx avg `0.0108` n `6`; index avg `0.0021` n `26`; metal avg `-0.006` n `20`; unknown avg `5.5983` n `1115`
- 4h: commodity avg `0.0412` n `13`; crypto_alt avg `0.4064` n `235`; crypto_major avg `0.0795` n `8`; equity avg `0.0773` n `150`; fx avg `0.0109` n `6`; index avg `0.0088` n `26`; metal avg `0.0118` n `20`; unknown avg `0.6309` n `1099`
- 24h: commodity avg `0.4302` n `13`; crypto_alt avg `1.2849` n `235`; crypto_major avg `-0.0584` n `8`; equity avg `0.0984` n `150`; fx avg `0.0097` n `6`; index avg `-0.0066` n `26`; metal avg `0.0032` n `20`; unknown avg `0.7673` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
