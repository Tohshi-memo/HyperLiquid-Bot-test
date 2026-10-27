# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T06:07:27.791104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `13`; crypto_alt avg `-0.0892` n `237`; crypto_major avg `-0.1044` n `8`; equity avg `0.0701` n `154`; fx avg `-0.0051` n `6`; index avg `0.0022` n `27`; metal avg `-0.0437` n `20`; unknown avg `-0.1218` n `1220`
- 1h: commodity avg `0.0564` n `13`; crypto_alt avg `0.0172` n `237`; crypto_major avg `-0.027` n `8`; equity avg `-0.2574` n `154`; fx avg `-0.0064` n `6`; index avg `-0.0959` n `27`; metal avg `-0.0788` n `20`; unknown avg `0.0436` n `1218`
- 4h: commodity avg `0.0281` n `13`; crypto_alt avg `-0.1394` n `237`; crypto_major avg `-0.3139` n `8`; equity avg `-1.0229` n `154`; fx avg `-0.0073` n `6`; index avg `-0.0358` n `27`; metal avg `-0.141` n `20`; unknown avg `198.1676` n `1198`
- 24h: commodity avg `0.108` n `13`; crypto_alt avg `0.0639` n `237`; crypto_major avg `0.1269` n `8`; equity avg `0.7627` n `153`; fx avg `-0.0495` n `6`; index avg `0.0731` n `27`; metal avg `-0.2264` n `20`; unknown avg `1113.7332` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
