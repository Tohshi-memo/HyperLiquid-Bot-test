# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T23:37:26.360518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0081` n `228`; crypto_major avg `0.0689` n `8`; equity avg `-0.014` n `88`; fx avg `0.0114` n `6`; index avg `0.0014` n `23`; metal avg `-0.0134` n `20`; unknown avg `-0.0627` n `765`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `-0.0574` n `228`; crypto_major avg `0.1465` n `8`; equity avg `0.0847` n `88`; fx avg `0.0011` n `6`; index avg `-0.0061` n `23`; metal avg `-0.0952` n `20`; unknown avg `-0.4409` n `765`
- 4h: commodity avg `0.0039` n `12`; crypto_alt avg `-0.5264` n `228`; crypto_major avg `-0.4264` n `8`; equity avg `0.2643` n `88`; fx avg `-0.0094` n `6`; index avg `-0.0153` n `23`; metal avg `-0.2391` n `20`; unknown avg `0.5427` n `763`
- 24h: commodity avg `0.1933` n `12`; crypto_alt avg `-2.2121` n `228`; crypto_major avg `-2.1041` n `8`; equity avg `1.19` n `88`; fx avg `0.11` n `6`; index avg `0.2436` n `23`; metal avg `-0.1621` n `20`; unknown avg `7.5993` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
