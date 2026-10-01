# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T12:08:04.244676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.0852` n `234`; crypto_major avg `-0.0096` n `8`; equity avg `-0.0494` n `142`; fx avg `-0.0055` n `6`; index avg `-0.0106` n `26`; metal avg `0.0227` n `20`; unknown avg `0.0623` n `967`
- 1h: commodity avg `-0.0347` n `13`; crypto_alt avg `0.2596` n `234`; crypto_major avg `0.2842` n `8`; equity avg `-0.1512` n `142`; fx avg `-0.0112` n `6`; index avg `0.0028` n `26`; metal avg `0.1199` n `20`; unknown avg `0.1399` n `967`
- 4h: commodity avg `-0.2252` n `13`; crypto_alt avg `-0.0811` n `234`; crypto_major avg `0.7703` n `8`; equity avg `0.0252` n `142`; fx avg `-0.0497` n `6`; index avg `0.0771` n `26`; metal avg `0.1649` n `20`; unknown avg `5.6321` n `967`
- 24h: commodity avg `-0.2002` n `13`; crypto_alt avg `-0.6721` n `234`; crypto_major avg `0.3119` n `8`; equity avg `0.5389` n `142`; fx avg `0.0511` n `6`; index avg `0.2182` n `26`; metal avg `-0.0521` n `20`; unknown avg `776.6065` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
