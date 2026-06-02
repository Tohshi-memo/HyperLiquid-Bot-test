# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T12:37:22.800062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.68` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.073` n `12`; crypto_alt avg `0.054` n `228`; crypto_major avg `-0.01` n `8`; equity avg `-0.1238` n `69`; fx avg `-0.0026` n `6`; index avg `-0.0197` n `23`; metal avg `0.023` n `18`; unknown avg `-0.0141` n `422`
- 1h: commodity avg `-0.0288` n `12`; crypto_alt avg `0.1069` n `228`; crypto_major avg `-0.1338` n `8`; equity avg `-0.0784` n `69`; fx avg `-0.0027` n `6`; index avg `0.0364` n `23`; metal avg `0.0839` n `18`; unknown avg `-0.0179` n `422`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.0194` n `228`; crypto_major avg `-0.3629` n `8`; equity avg `-0.0871` n `69`; fx avg `-0.002` n `6`; index avg `-0.0141` n `23`; metal avg `-0.1831` n `18`; unknown avg `-0.2822` n `422`
- 24h: commodity avg `-0.2377` n `12`; crypto_alt avg `0.0324` n `228`; crypto_major avg `-1.9341` n `8`; equity avg `0.8836` n `69`; fx avg `0.1276` n `6`; index avg `0.1676` n `23`; metal avg `0.9152` n `18`; unknown avg `-0.0865` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
