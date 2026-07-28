# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T08:03:38.430510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.1083` n `230`; crypto_major avg `0.0402` n `8`; equity avg `-0.015` n `102`; fx avg `0.0035` n `6`; index avg `0.0211` n `25`; metal avg `0.0228` n `20`; unknown avg `0.0057` n `774`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.2816` n `230`; crypto_major avg `-0.1042` n `8`; equity avg `-0.0517` n `102`; fx avg `-0.0061` n `6`; index avg `-0.0263` n `25`; metal avg `0.014` n `20`; unknown avg `0.0228` n `774`
- 4h: commodity avg `-0.2366` n `12`; crypto_alt avg `-0.0553` n `230`; crypto_major avg `-0.1597` n `8`; equity avg `-0.3841` n `102`; fx avg `-0.0559` n `6`; index avg `-0.0661` n `25`; metal avg `0.0307` n `20`; unknown avg `-0.0218` n `758`
- 24h: commodity avg `-0.704` n `12`; crypto_alt avg `-3.7152` n `230`; crypto_major avg `-3.5352` n `8`; equity avg `-4.117` n `102`; fx avg `-0.1773` n `6`; index avg `-0.8421` n `25`; metal avg `-0.3704` n `20`; unknown avg `1158.5929` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
