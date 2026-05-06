# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T18:52:21.744224+00:00`
- Correlation status: `ready`
- Asset price records: `479`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.96` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.0409` n `228`; crypto_major avg `-0.0403` n `8`; equity avg `-0.1782` n `65`; fx avg `0.0011` n `4`; index avg `-0.0589` n `23`; metal avg `-0.0828` n `18`; unknown avg `0.0504` n `356`
- 1h: commodity avg `-0.1555` n `12`; crypto_alt avg `-0.0084` n `228`; crypto_major avg `-0.0288` n `8`; equity avg `0.2049` n `65`; fx avg `-0.0412` n `4`; index avg `0.1215` n `23`; metal avg `0.0947` n `18`; unknown avg `0.0082` n `356`
- 4h: commodity avg `-0.0945` n `12`; crypto_alt avg `0.2356` n `228`; crypto_major avg `-0.2804` n `8`; equity avg `0.486` n `65`; fx avg `-0.0152` n `4`; index avg `0.2572` n `23`; metal avg `-0.2482` n `18`; unknown avg `-0.154` n `356`
- 24h: commodity avg `-2.4638` n `7`; crypto_alt avg `2.5827` n `223`; crypto_major avg `0.3658` n `7`; equity avg `2.5457` n `47`; fx avg `-0.4881` n `4`; index avg `1.8169` n `6`; metal avg `2.9767` n `7`; unknown avg `3.9274` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1531`, n `471`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1386`, n `471`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `475`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1263`, n `471`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1144`, n `471`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `475`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.087`, n `475`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `471`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `471`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `475`, weak_sample_signal
