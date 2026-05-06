# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T08:00:29.133870+00:00`
- Correlation status: `ready`
- Asset price records: `436`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.466` n `7`; crypto_alt avg `0.0147` n `223`; crypto_major avg `-0.1103` n `7`; equity avg `0.1012` n `47`; fx avg `-0.0917` n `4`; index avg `0.0129` n `6`; metal avg `0.2309` n `7`; unknown avg `-0.1649` n `313`
- 1h: commodity avg `-0.77` n `7`; crypto_alt avg `0.1322` n `223`; crypto_major avg `-0.0053` n `7`; equity avg `0.1624` n `47`; fx avg `-0.1463` n `4`; index avg `-0.0823` n `6`; metal avg `0.4436` n `7`; unknown avg `0.2209` n `313`
- 4h: commodity avg `-0.6725` n `7`; crypto_alt avg `0.5622` n `223`; crypto_major avg `0.2152` n `7`; equity avg `0.2528` n `47`; fx avg `-0.3162` n `4`; index avg `-0.0462` n `6`; metal avg `0.4624` n `7`; unknown avg `1.0125` n `311`
- 24h: commodity avg `-2.1171` n `7`; crypto_alt avg `2.8581` n `223`; crypto_major avg `1.8916` n `7`; equity avg `2.9256` n `47`; fx avg `-0.4937` n `4`; index avg `2.0197` n `6`; metal avg `2.273` n `7`; unknown avg `1.7328` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1795`, n `432`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1732`, n `432`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1298`, n `432`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `432`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `432`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `432`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0974`, n `428`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0938`, n `428`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `432`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0925`, n `428`, weak_sample_signal
