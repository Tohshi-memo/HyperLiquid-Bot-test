# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T17:07:39.559605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0876` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1092` n `12`; crypto_alt avg `0.1761` n `228`; crypto_major avg `-0.0327` n `8`; equity avg `-0.0648` n `77`; fx avg `0.0048` n `6`; index avg `-0.0301` n `23`; metal avg `-0.0712` n `18`; unknown avg `-0.0097` n `687`
- 1h: commodity avg `0.0456` n `12`; crypto_alt avg `0.0055` n `228`; crypto_major avg `-0.2749` n `8`; equity avg `-0.0305` n `77`; fx avg `-0.0044` n `6`; index avg `-0.1147` n `23`; metal avg `0.0066` n `18`; unknown avg `-0.029` n `687`
- 4h: commodity avg `-0.0206` n `12`; crypto_alt avg `-1.3327` n `228`; crypto_major avg `-1.706` n `8`; equity avg `-0.7302` n `77`; fx avg `0.0591` n `6`; index avg `-0.6184` n `23`; metal avg `-0.2572` n `18`; unknown avg `0.8642` n `687`
- 24h: commodity avg `-0.8883` n `12`; crypto_alt avg `-1.6447` n `228`; crypto_major avg `-1.2884` n `8`; equity avg `-0.8775` n `77`; fx avg `-0.0166` n `6`; index avg `-0.7` n `23`; metal avg `0.4038` n `18`; unknown avg `0.437` n `623`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0435`, n `668`, weak_sample_signal
