# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T02:22:22.138090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `0.4013` n `228`; crypto_major avg `0.4609` n `8`; equity avg `0.2648` n `69`; fx avg `0.0023` n `6`; index avg `0.0782` n `23`; metal avg `0.2396` n `18`; unknown avg `0.0459` n `422`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.8676` n `228`; crypto_major avg `-0.5383` n `8`; equity avg `-0.0929` n `69`; fx avg `0.028` n `6`; index avg `-0.1633` n `23`; metal avg `-0.2854` n `18`; unknown avg `0.5062` n `422`
- 4h: commodity avg `-0.2975` n `12`; crypto_alt avg `-0.7901` n `228`; crypto_major avg `-0.4933` n `8`; equity avg `-0.7163` n `69`; fx avg `0.0516` n `6`; index avg `-0.5408` n `23`; metal avg `0.1809` n `18`; unknown avg `0.4695` n `422`
- 24h: commodity avg `-0.4463` n `12`; crypto_alt avg `-1.3388` n `228`; crypto_major avg `-1.5854` n `8`; equity avg `-0.9766` n `69`; fx avg `-0.0024` n `6`; index avg `-0.3685` n `23`; metal avg `-0.4683` n `18`; unknown avg `1.9166` n `406`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
