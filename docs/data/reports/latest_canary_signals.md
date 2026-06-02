# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T11:37:22.628928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.8` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.038` n `12`; crypto_alt avg `-0.2836` n `228`; crypto_major avg `-0.0705` n `8`; equity avg `0.1027` n `69`; fx avg `-0.0031` n `6`; index avg `0.0528` n `23`; metal avg `0.0381` n `18`; unknown avg `-0.3167` n `422`
- 1h: commodity avg `0.0593` n `12`; crypto_alt avg `-0.0189` n `228`; crypto_major avg `0.1264` n `8`; equity avg `0.2205` n `69`; fx avg `0.0134` n `6`; index avg `-0.033` n `23`; metal avg `0.0359` n `18`; unknown avg `0.0786` n `422`
- 4h: commodity avg `-0.1592` n `12`; crypto_alt avg `-0.3641` n `228`; crypto_major avg `-0.6296` n `8`; equity avg `0.2121` n `69`; fx avg `-0.0136` n `6`; index avg `0.1301` n `23`; metal avg `-0.309` n `18`; unknown avg `-0.5235` n `422`
- 24h: commodity avg `-0.7239` n `12`; crypto_alt avg `-0.4055` n `228`; crypto_major avg `-2.0986` n `8`; equity avg `0.7342` n `69`; fx avg `0.1398` n `6`; index avg `0.0387` n `23`; metal avg `0.6345` n `18`; unknown avg `-0.0941` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
