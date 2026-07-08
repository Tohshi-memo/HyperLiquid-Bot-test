# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T19:22:26.531667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.0177` n `229`; crypto_major avg `0.0756` n `8`; equity avg `0.04` n `91`; fx avg `0.0035` n `6`; index avg `0.0108` n `25`; metal avg `-0.0135` n `20`; unknown avg `1.5206` n `764`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `0.0112` n `229`; crypto_major avg `-0.1518` n `8`; equity avg `0.1447` n `91`; fx avg `-0.0146` n `6`; index avg `0.0113` n `25`; metal avg `0.1131` n `20`; unknown avg `1.5427` n `764`
- 4h: commodity avg `-0.4647` n `12`; crypto_alt avg `0.7225` n `229`; crypto_major avg `0.7994` n `8`; equity avg `1.2808` n `91`; fx avg `-0.0095` n `6`; index avg `0.3249` n `25`; metal avg `0.5393` n `20`; unknown avg `1.6229` n `764`
- 24h: commodity avg `0.2682` n `12`; crypto_alt avg `-2.0299` n `229`; crypto_major avg `-2.6364` n `8`; equity avg `1.0316` n `91`; fx avg `-0.0099` n `6`; index avg `0.0242` n `25`; metal avg `-0.5984` n `20`; unknown avg `0.3555` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
