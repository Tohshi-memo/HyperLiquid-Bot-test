# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T14:22:25.831783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `-0.1768` n `228`; crypto_major avg `-0.1269` n `8`; equity avg `-0.6287` n `66`; fx avg `-0.0055` n `6`; index avg `-0.3112` n `23`; metal avg `0.0013` n `18`; unknown avg `0.4953` n `386`
- 1h: commodity avg `-0.5215` n `12`; crypto_alt avg `-0.2312` n `228`; crypto_major avg `-0.2221` n `8`; equity avg `-0.1313` n `66`; fx avg `-0.0287` n `6`; index avg `-0.0486` n `23`; metal avg `0.1114` n `18`; unknown avg `0.9977` n `386`
- 4h: commodity avg `0.9454` n `12`; crypto_alt avg `-0.5898` n `228`; crypto_major avg `-0.4647` n `8`; equity avg `-0.6011` n `66`; fx avg `-0.0582` n `6`; index avg `-0.3959` n `23`; metal avg `-0.5574` n `18`; unknown avg `1.9265` n `386`
- 24h: commodity avg `-0.1749` n `12`; crypto_alt avg `1.1293` n `228`; crypto_major avg `1.8101` n `8`; equity avg `0.6979` n `66`; fx avg `-0.002` n `6`; index avg `0.2528` n `23`; metal avg `-0.4695` n `18`; unknown avg `6.8238` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
