# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T17:22:25.369220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.2896` n `232`; crypto_major avg `0.2034` n `8`; equity avg `-0.0381` n `131`; fx avg `0.014` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.8487` n `793`
- 1h: commodity avg `0.0322` n `12`; crypto_alt avg `0.0481` n `232`; crypto_major avg `0.1358` n `8`; equity avg `-0.2016` n `131`; fx avg `-0.0023` n `6`; index avg `-0.0726` n `26`; metal avg `-0.0833` n `20`; unknown avg `0.4292` n `791`
- 4h: commodity avg `0.3993` n `12`; crypto_alt avg `-0.0361` n `232`; crypto_major avg `-0.3176` n `8`; equity avg `-0.4945` n `131`; fx avg `-0.0144` n `6`; index avg `-0.0478` n `26`; metal avg `0.0648` n `20`; unknown avg `-0.395` n `790`
- 24h: commodity avg `0.6124` n `12`; crypto_alt avg `0.2635` n `232`; crypto_major avg `-1.1981` n `8`; equity avg `-1.4847` n `130`; fx avg `0.0419` n `6`; index avg `-0.2431` n `26`; metal avg `-0.6203` n `20`; unknown avg `-0.2233` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0384`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0376`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0348`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0337`, n `668`, weak_sample_signal
