# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T06:37:20.850422+00:00`
- Correlation status: `ready`
- Asset price records: `526`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `0.4344` n `228`; crypto_major avg `0.3586` n `8`; equity avg `0.1009` n `65`; fx avg `-0.0401` n `4`; index avg `0.0482` n `23`; metal avg `0.3438` n `18`; unknown avg `0.1407` n `358`
- 1h: commodity avg `-0.0803` n `12`; crypto_alt avg `0.0205` n `228`; crypto_major avg `0.1515` n `8`; equity avg `0.0807` n `65`; fx avg `0.0387` n `4`; index avg `0.0635` n `23`; metal avg `0.5654` n `18`; unknown avg `0.0554` n `356`
- 4h: commodity avg `-0.0393` n `12`; crypto_alt avg `1.3555` n `228`; crypto_major avg `0.561` n `8`; equity avg `0.5287` n `65`; fx avg `0.0513` n `4`; index avg `0.2107` n `23`; metal avg `0.6414` n `18`; unknown avg `0.3483` n `356`
- 24h: commodity avg `-1.8464` n `7`; crypto_alt avg `1.3727` n `223`; crypto_major avg `-0.5915` n `7`; equity avg `1.5642` n `47`; fx avg `-0.0099` n `4`; index avg `1.1991` n `6`; metal avg `1.9368` n `7`; unknown avg `1.4181` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `522`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `522`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0845`, n `518`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `518`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0765`, n `518`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0762`, n `518`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `522`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0744`, n `518`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0713`, n `518`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0696`, n `518`, weak_sample_signal
