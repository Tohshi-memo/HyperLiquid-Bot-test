# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T21:22:34.214583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.2558` n `228`; crypto_major avg `0.1756` n `8`; equity avg `0.0064` n `86`; fx avg `0.0005` n `6`; index avg `-0.0136` n `23`; metal avg `0.0118` n `20`; unknown avg `0.2895` n `765`
- 1h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.074` n `228`; crypto_major avg `-0.2465` n `8`; equity avg `-0.2255` n `86`; fx avg `-0.009` n `6`; index avg `-0.0505` n `23`; metal avg `-0.0471` n `20`; unknown avg `0.4587` n `765`
- 4h: commodity avg `-0.1015` n `12`; crypto_alt avg `-0.0265` n `228`; crypto_major avg `-0.1027` n `8`; equity avg `0.2178` n `86`; fx avg `0.007` n `6`; index avg `0.0215` n `23`; metal avg `-0.1525` n `20`; unknown avg `0.5352` n `765`
- 24h: commodity avg `0.3279` n `12`; crypto_alt avg `-1.0925` n `228`; crypto_major avg `-1.4191` n `8`; equity avg `-1.7799` n `86`; fx avg `0.0772` n `6`; index avg `-0.1176` n `23`; metal avg `0.309` n `20`; unknown avg `0.8891` n `700`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
