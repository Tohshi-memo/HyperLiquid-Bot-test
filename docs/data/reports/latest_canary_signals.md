# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T09:39:22.639660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `12`; crypto_alt avg `0.6569` n `228`; crypto_major avg `0.9039` n `8`; equity avg `0.18` n `88`; fx avg `-0.0121` n `6`; index avg `0.0238` n `25`; metal avg `0.0224` n `20`; unknown avg `0.0564` n `763`
- 1h: commodity avg `-0.1172` n `12`; crypto_alt avg `0.6991` n `228`; crypto_major avg `1.097` n `8`; equity avg `0.246` n `88`; fx avg `-0.0133` n `6`; index avg `0.0018` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.1743` n `763`
- 4h: commodity avg `-0.1209` n `12`; crypto_alt avg `0.7538` n `228`; crypto_major avg `0.8837` n `8`; equity avg `-0.3206` n `88`; fx avg `-0.0881` n `6`; index avg `-0.1041` n `25`; metal avg `0.1664` n `20`; unknown avg `2.3639` n `741`
- 24h: commodity avg `-0.4437` n `12`; crypto_alt avg `2.6696` n `228`; crypto_major avg `2.6433` n `8`; equity avg `-1.7678` n `88`; fx avg `-0.0971` n `6`; index avg `-0.5014` n `25`; metal avg `1.1059` n `20`; unknown avg `16.9875` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
