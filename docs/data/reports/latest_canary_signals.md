# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T07:52:31.094340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.0798` n `233`; crypto_major avg `0.27` n `8`; equity avg `0.0198` n `134`; fx avg `0.0093` n `6`; index avg `0.0016` n `26`; metal avg `0.0342` n `20`; unknown avg `0.2432` n `797`
- 1h: commodity avg `0.0852` n `12`; crypto_alt avg `-0.76` n `233`; crypto_major avg `-0.4754` n `8`; equity avg `-0.1425` n `134`; fx avg `-0.0076` n `6`; index avg `-0.0388` n `26`; metal avg `-0.1131` n `20`; unknown avg `0.2732` n `795`
- 4h: commodity avg `0.0405` n `12`; crypto_alt avg `-0.5321` n `233`; crypto_major avg `-0.4448` n `8`; equity avg `0.0625` n `134`; fx avg `0.0488` n `6`; index avg `0.0379` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.3367` n `765`
- 24h: commodity avg `-0.0595` n `12`; crypto_alt avg `-4.518` n `233`; crypto_major avg `-3.1338` n `8`; equity avg `-1.1667` n `134`; fx avg `0.0927` n `6`; index avg `-0.1344` n `26`; metal avg `0.0761` n `20`; unknown avg `0.5427` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
