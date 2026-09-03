# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T20:07:25.115034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0166` n `232`; crypto_major avg `0.024` n `8`; equity avg `0.06` n `133`; fx avg `0.0016` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.9192` n `780`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.2304` n `232`; crypto_major avg `0.3034` n `8`; equity avg `0.0603` n `133`; fx avg `-0.0046` n `6`; index avg `-0.0155` n `26`; metal avg `-0.012` n `20`; unknown avg `0.2279` n `780`
- 4h: commodity avg `0.0851` n `12`; crypto_alt avg `0.5622` n `232`; crypto_major avg `0.8193` n `8`; equity avg `0.3497` n `133`; fx avg `0.0344` n `6`; index avg `0.0373` n `26`; metal avg `-0.0584` n `20`; unknown avg `42.528` n `780`
- 24h: commodity avg `-0.0447` n `12`; crypto_alt avg `4.3362` n `232`; crypto_major avg `5.6438` n `8`; equity avg `1.4227` n `133`; fx avg `-0.2379` n `6`; index avg `0.1796` n `26`; metal avg `0.7643` n `20`; unknown avg `529.5621` n `742`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
