# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T18:37:26.764098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `-0.0274` n `230`; crypto_major avg `-0.0826` n `8`; equity avg `-0.1412` n `108`; fx avg `-0.0015` n `6`; index avg `-0.013` n `25`; metal avg `-0.0717` n `20`; unknown avg `0.0428` n `782`
- 1h: commodity avg `0.1094` n `12`; crypto_alt avg `0.019` n `230`; crypto_major avg `0.1259` n `8`; equity avg `-0.2` n `108`; fx avg `-0.0018` n `6`; index avg `-0.0077` n `25`; metal avg `0.0283` n `20`; unknown avg `0.0072` n `782`
- 4h: commodity avg `0.068` n `12`; crypto_alt avg `0.3261` n `230`; crypto_major avg `0.6496` n `8`; equity avg `0.0716` n `108`; fx avg `-0.0114` n `6`; index avg `-0.0526` n `25`; metal avg `0.0757` n `20`; unknown avg `-0.1019` n `782`
- 24h: commodity avg `-0.0758` n `12`; crypto_alt avg `0.6875` n `230`; crypto_major avg `0.8997` n `8`; equity avg `-0.3705` n `108`; fx avg `-0.0222` n `6`; index avg `-0.0718` n `25`; metal avg `0.783` n `20`; unknown avg `0.7637` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
