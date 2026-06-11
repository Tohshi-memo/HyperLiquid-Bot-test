# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T23:52:33.405671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0757` n `228`; crypto_major avg `-0.1246` n `8`; equity avg `0.0508` n `74`; fx avg `0.0122` n `6`; index avg `0.1337` n `23`; metal avg `-0.0302` n `18`; unknown avg `0.0383` n `556`
- 1h: commodity avg `0.0623` n `12`; crypto_alt avg `-0.1242` n `228`; crypto_major avg `-0.0652` n `8`; equity avg `-0.0133` n `74`; fx avg `-0.0001` n `6`; index avg `0.059` n `23`; metal avg `-0.1801` n `18`; unknown avg `0.0982` n `556`
- 4h: commodity avg `-0.2793` n `12`; crypto_alt avg `-0.158` n `228`; crypto_major avg `-0.2147` n `8`; equity avg `0.4762` n `74`; fx avg `0.0343` n `6`; index avg `0.4258` n `23`; metal avg `0.0679` n `18`; unknown avg `-0.3022` n `556`
- 24h: commodity avg `-2.8981` n `12`; crypto_alt avg `4.0005` n `228`; crypto_major avg `4.148` n `8`; equity avg `5.0734` n `74`; fx avg `0.081` n `6`; index avg `2.7104` n `23`; metal avg `4.3162` n `18`; unknown avg `2.4996` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
