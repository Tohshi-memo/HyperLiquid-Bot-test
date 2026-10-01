# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T01:37:34.235090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `-0.4056` n `234`; crypto_major avg `-0.1809` n `8`; equity avg `-0.0174` n `142`; fx avg `0.0226` n `6`; index avg `0.0007` n `26`; metal avg `-0.0124` n `20`; unknown avg `0.3683` n `974`
- 1h: commodity avg `-0.4229` n `13`; crypto_alt avg `0.0384` n `234`; crypto_major avg `0.0682` n `8`; equity avg `0.3172` n `142`; fx avg `0.0243` n `6`; index avg `0.0925` n `26`; metal avg `0.1877` n `20`; unknown avg `0.1247` n `972`
- 4h: commodity avg `-0.3756` n `13`; crypto_alt avg `0.4309` n `234`; crypto_major avg `-0.1494` n `8`; equity avg `0.3959` n `142`; fx avg `0.1191` n `6`; index avg `0.1371` n `26`; metal avg `0.0149` n `20`; unknown avg `0.8052` n `942`
- 24h: commodity avg `-0.288` n `13`; crypto_alt avg `0.342` n `234`; crypto_major avg `0.7733` n `8`; equity avg `-0.1308` n `142`; fx avg `0.2004` n `6`; index avg `0.0678` n `26`; metal avg `-0.1009` n `20`; unknown avg `777.9611` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
