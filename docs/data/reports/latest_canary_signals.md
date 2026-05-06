# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T04:30:21.072678+00:00`
- Correlation status: `ready`
- Asset price records: `422`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0558` n `7`; crypto_alt avg `-0.3943` n `223`; crypto_major avg `-0.352` n `7`; equity avg `0.0907` n `47`; fx avg `-0.1711` n `4`; index avg `-0.0352` n `6`; metal avg `0.0335` n `7`; unknown avg `0.2436` n `313`
- 1h: commodity avg `-0.1087` n `7`; crypto_alt avg `-0.28` n `223`; crypto_major avg `-0.2886` n `7`; equity avg `0.349` n `47`; fx avg `-0.2012` n `4`; index avg `0.154` n `6`; metal avg `0.1475` n `7`; unknown avg `0.0977` n `313`
- 4h: commodity avg `-0.2509` n `7`; crypto_alt avg `1.0386` n `223`; crypto_major avg `0.5916` n `7`; equity avg `0.9212` n `47`; fx avg `-0.2004` n `4`; index avg `0.5575` n `6`; metal avg `1.2811` n `7`; unknown avg `0.2148` n `313`
- 24h: commodity avg `-1.4892` n `7`; crypto_alt avg `2.3253` n `223`; crypto_major avg `1.7053` n `7`; equity avg `3.2404` n `47`; fx avg `-0.3566` n `4`; index avg `2.1855` n `6`; metal avg `2.3871` n `7`; unknown avg `1.4005` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.181`, n `418`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1747`, n `418`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `418`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `418`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `418`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `418`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `414`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `418`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `414`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `418`, weak_sample_signal
