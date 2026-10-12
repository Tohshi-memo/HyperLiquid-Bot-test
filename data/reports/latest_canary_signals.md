# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T06:52:27.186754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `13`; crypto_alt avg `-0.0755` n `235`; crypto_major avg `0.0122` n `8`; equity avg `-0.056` n `151`; fx avg `-0.0022` n `6`; index avg `0.0065` n `26`; metal avg `0.0297` n `20`; unknown avg `0.0508` n `1133`
- 1h: commodity avg `0.0975` n `13`; crypto_alt avg `-0.3171` n `235`; crypto_major avg `-0.0913` n `8`; equity avg `-0.2718` n `151`; fx avg `-0.0107` n `6`; index avg `-0.0448` n `26`; metal avg `-0.009` n `20`; unknown avg `0.0964` n `1111`
- 4h: commodity avg `0.2598` n `13`; crypto_alt avg `0.1622` n `235`; crypto_major avg `0.38` n `8`; equity avg `-0.4843` n `151`; fx avg `-0.0026` n `6`; index avg `-0.0991` n `26`; metal avg `-0.1031` n `20`; unknown avg `0.0493` n `1043`
- 24h: commodity avg `-0.2704` n `13`; crypto_alt avg `2.3076` n `235`; crypto_major avg `1.6317` n `8`; equity avg `-0.6231` n `151`; fx avg `-0.0599` n `6`; index avg `-0.0616` n `26`; metal avg `0.0678` n `20`; unknown avg `0.525` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
