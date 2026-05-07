# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T11:52:10.573657+00:00`
- Correlation status: `ready`
- Asset price records: `547`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `12`; crypto_alt avg `-0.0998` n `228`; crypto_major avg `-0.0984` n `8`; equity avg `-0.1453` n `65`; fx avg `0.0113` n `4`; index avg `0.0047` n `23`; metal avg `0.059` n `18`; unknown avg `0.1042` n `366`
- 1h: commodity avg `-0.4914` n `12`; crypto_alt avg `0.0512` n `228`; crypto_major avg `0.0483` n `8`; equity avg `-0.1211` n `65`; fx avg `-0.0174` n `4`; index avg `-0.0597` n `23`; metal avg `0.1694` n `18`; unknown avg `0.1302` n `366`
- 4h: commodity avg `-0.4692` n `12`; crypto_alt avg `-0.2209` n `228`; crypto_major avg `-0.7245` n `8`; equity avg `-0.265` n `65`; fx avg `0.0902` n `4`; index avg `-0.1955` n `23`; metal avg `0.2215` n `18`; unknown avg `0.3509` n `358`
- 24h: commodity avg `-0.2008` n `7`; crypto_alt avg `0.0234` n `223`; crypto_major avg `-2.6368` n `7`; equity avg `0.0705` n `47`; fx avg `0.1445` n `4`; index avg `-0.1234` n `6`; metal avg `1.4563` n `7`; unknown avg `0.8316` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `543`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `543`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0949`, n `543`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.079`, n `539`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `539`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.076`, n `539`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `539`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.071`, n `539`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `543`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `539`, weak_sample_signal
