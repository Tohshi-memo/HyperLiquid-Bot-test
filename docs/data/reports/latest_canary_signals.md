# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T21:52:24.474129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.0132` n `229`; crypto_major avg `-0.0576` n `8`; equity avg `0.005` n `92`; fx avg `0.0006` n `6`; index avg `-0.0013` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0713` n `765`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.448` n `229`; crypto_major avg `0.1747` n `8`; equity avg `0.0066` n `92`; fx avg `0.0094` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.2761` n `765`
- 4h: commodity avg `0.1508` n `12`; crypto_alt avg `0.2573` n `229`; crypto_major avg `0.0579` n `8`; equity avg `-0.2377` n `92`; fx avg `-0.0182` n `6`; index avg `-0.0091` n `25`; metal avg `0.0832` n `20`; unknown avg `-0.4404` n `765`
- 24h: commodity avg `-0.2888` n `12`; crypto_alt avg `1.0236` n `229`; crypto_major avg `0.852` n `8`; equity avg `-0.6338` n `92`; fx avg `-0.1738` n `6`; index avg `0.043` n `25`; metal avg `0.1528` n `20`; unknown avg `-0.234` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
