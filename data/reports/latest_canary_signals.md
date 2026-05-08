# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T00:37:17.361425+00:00`
- Correlation status: `ready`
- Asset price records: `598`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.1156` n `228`; crypto_major avg `-0.0784` n `8`; equity avg `0.1454` n `65`; fx avg `-0.0027` n `5`; index avg `0.023` n `23`; metal avg `0.04` n `18`; unknown avg `-0.0001` n `365`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `0.0408` n `228`; crypto_major avg `0.0818` n `8`; equity avg `0.363` n `65`; fx avg `0.0958` n `5`; index avg `0.1805` n `23`; metal avg `0.076` n `18`; unknown avg `-0.0176` n `365`
- 4h: commodity avg `0.1066` n `12`; crypto_alt avg `0.2454` n `228`; crypto_major avg `0.0049` n `8`; equity avg `0.0939` n `65`; fx avg `0.0519` n `5`; index avg `0.1516` n `23`; metal avg `-0.1482` n `18`; unknown avg `-0.3186` n `365`
- 24h: commodity avg `0.7137` n `12`; crypto_alt avg `1.81` n `228`; crypto_major avg `-1.441` n `8`; equity avg `-0.7428` n `65`; fx avg `0.1852` n `5`; index avg `-0.6223` n `23`; metal avg `-0.0482` n `18`; unknown avg `-0.323` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `594`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `594`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `594`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `594`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0952`, n `590`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `590`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0924`, n `590`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `590`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `590`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `594`, weak_sample_signal
