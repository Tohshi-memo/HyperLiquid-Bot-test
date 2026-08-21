# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T20:52:24.731324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0966` n `230`; crypto_major avg `0.0615` n `8`; equity avg `-0.0115` n `121`; fx avg `-0.0018` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.0014` n `793`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `1.0169` n `230`; crypto_major avg `0.7552` n `8`; equity avg `0.0416` n `121`; fx avg `-0.008` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0932` n `20`; unknown avg `-0.1974` n `793`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.1679` n `230`; crypto_major avg `-0.0018` n `8`; equity avg `0.007` n `121`; fx avg `0.0076` n `6`; index avg `-0.0312` n `25`; metal avg `-0.1303` n `20`; unknown avg `-0.5023` n `793`
- 24h: commodity avg `0.1392` n `12`; crypto_alt avg `7.3751` n `230`; crypto_major avg `5.3791` n `8`; equity avg `0.9887` n `121`; fx avg `-0.0937` n `6`; index avg `0.0979` n `25`; metal avg `0.5021` n `20`; unknown avg `1.1072` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
