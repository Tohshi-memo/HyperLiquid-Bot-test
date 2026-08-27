# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T13:52:30.631225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `0.1103` n `231`; crypto_major avg `0.2208` n `8`; equity avg `-0.0007` n `127`; fx avg `-0.0045` n `6`; index avg `0.0207` n `26`; metal avg `0.029` n `20`; unknown avg `0.0206` n `792`
- 1h: commodity avg `0.1129` n `12`; crypto_alt avg `0.2132` n `231`; crypto_major avg `0.2211` n `8`; equity avg `-0.1322` n `127`; fx avg `0.0529` n `6`; index avg `-0.0235` n `26`; metal avg `0.014` n `20`; unknown avg `-0.0511` n `792`
- 4h: commodity avg `0.2666` n `12`; crypto_alt avg `-0.4978` n `231`; crypto_major avg `-0.6937` n `8`; equity avg `-0.6216` n `127`; fx avg `0.038` n `6`; index avg `-0.0736` n `26`; metal avg `-0.0583` n `20`; unknown avg `0.0004` n `792`
- 24h: commodity avg `0.4285` n `12`; crypto_alt avg `2.2745` n `231`; crypto_major avg `2.6297` n `8`; equity avg `1.3414` n `127`; fx avg `-0.0369` n `6`; index avg `0.1957` n `26`; metal avg `-0.3743` n `20`; unknown avg `0.5533` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
