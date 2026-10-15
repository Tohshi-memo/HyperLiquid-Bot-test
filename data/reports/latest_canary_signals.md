# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T10:07:26.858204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0475` n `13`; crypto_alt avg `-0.2341` n `236`; crypto_major avg `-0.2881` n `8`; equity avg `-0.1277` n `151`; fx avg `-0.0078` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0083` n `20`; unknown avg `-0.1344` n `1110`
- 1h: commodity avg `-0.0767` n `13`; crypto_alt avg `-0.3594` n `236`; crypto_major avg `-0.2922` n `8`; equity avg `-0.2939` n `151`; fx avg `-0.0196` n `6`; index avg `-0.0419` n `26`; metal avg `0.0783` n `20`; unknown avg `-0.3762` n `1102`
- 4h: commodity avg `0.0144` n `13`; crypto_alt avg `0.8104` n `236`; crypto_major avg `0.5913` n `8`; equity avg `-0.5363` n `151`; fx avg `-0.0384` n `6`; index avg `0.0083` n `26`; metal avg `0.2826` n `20`; unknown avg `4.274` n `1086`
- 24h: commodity avg `-0.4877` n `13`; crypto_alt avg `-4.2135` n `236`; crypto_major avg `-2.9092` n `8`; equity avg `-5.8893` n `151`; fx avg `0.0641` n `6`; index avg `-0.9649` n `26`; metal avg `-0.3594` n `20`; unknown avg `2.0664` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1198`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0884`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
