# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T03:07:27.481545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0667` n `13`; crypto_alt avg `0.0083` n `239`; crypto_major avg `-0.0021` n `8`; equity avg `-0.0028` n `168`; fx avg `0.0186` n `6`; index avg `0.0058` n `27`; metal avg `-0.0695` n `20`; unknown avg `0.0698` n `1257`
- 1h: commodity avg `0.0247` n `13`; crypto_alt avg `0.051` n `239`; crypto_major avg `0.0167` n `8`; equity avg `0.0733` n `168`; fx avg `0.0331` n `6`; index avg `-0.0035` n `27`; metal avg `0.1301` n `20`; unknown avg `208.7939` n `1263`
- 4h: commodity avg `0.059` n `13`; crypto_alt avg `1.5283` n `239`; crypto_major avg `1.2662` n `8`; equity avg `1.4025` n `168`; fx avg `-0.0371` n `6`; index avg `0.1272` n `27`; metal avg `0.2709` n `20`; unknown avg `217.0247` n `1247`
- 24h: commodity avg `0.6607` n `13`; crypto_alt avg `4.1366` n `239`; crypto_major avg `3.0299` n `8`; equity avg `2.385` n `168`; fx avg `0.0148` n `6`; index avg `0.1935` n `27`; metal avg `0.551` n `20`; unknown avg `771.9052` n `1015`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
