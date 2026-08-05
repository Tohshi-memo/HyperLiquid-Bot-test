# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T14:44:00.428501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0522` n `12`; crypto_alt avg `-0.0215` n `230`; crypto_major avg `0.0438` n `8`; equity avg `-0.5333` n `108`; fx avg `-0.0045` n `6`; index avg `-0.0625` n `25`; metal avg `0.005` n `20`; unknown avg `0.0205` n `782`
- 1h: commodity avg `-0.165` n `12`; crypto_alt avg `0.3751` n `230`; crypto_major avg `0.6377` n `8`; equity avg `-0.158` n `108`; fx avg `-0.0083` n `6`; index avg `-0.0655` n `25`; metal avg `0.2522` n `20`; unknown avg `0.2228` n `782`
- 4h: commodity avg `-0.3353` n `12`; crypto_alt avg `-0.1015` n `230`; crypto_major avg `0.1434` n `8`; equity avg `-0.3266` n `108`; fx avg `-0.022` n `6`; index avg `0.0254` n `25`; metal avg `0.3259` n `20`; unknown avg `-0.0295` n `782`
- 24h: commodity avg `-0.273` n `12`; crypto_alt avg `0.914` n `230`; crypto_major avg `0.6921` n `8`; equity avg `0.8705` n `108`; fx avg `0.0319` n `6`; index avg `0.2865` n `25`; metal avg `0.8655` n `20`; unknown avg `0.7576` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
