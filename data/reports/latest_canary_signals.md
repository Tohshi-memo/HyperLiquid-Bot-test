# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T04:37:33.404959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `0.0898` n `230`; crypto_major avg `0.0657` n `8`; equity avg `-0.0197` n `112`; fx avg `0.0019` n `6`; index avg `-0.0085` n `25`; metal avg `0.0052` n `20`; unknown avg `1.5246` n `783`
- 1h: commodity avg `0.02` n `12`; crypto_alt avg `0.0786` n `230`; crypto_major avg `0.0348` n `8`; equity avg `0.0058` n `112`; fx avg `-0.0014` n `6`; index avg `-0.0177` n `25`; metal avg `0.0153` n `20`; unknown avg `1.5188` n `783`
- 4h: commodity avg `0.0582` n `12`; crypto_alt avg `0.5414` n `230`; crypto_major avg `0.5922` n `8`; equity avg `-0.0473` n `112`; fx avg `0.0027` n `6`; index avg `-0.0088` n `25`; metal avg `-0.008` n `20`; unknown avg `1.4997` n `783`
- 24h: commodity avg `-0.2246` n `12`; crypto_alt avg `0.3548` n `230`; crypto_major avg `0.7774` n `8`; equity avg `1.6932` n `112`; fx avg `-0.0742` n `6`; index avg `0.1867` n `25`; metal avg `0.3454` n `20`; unknown avg `0.0299` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
