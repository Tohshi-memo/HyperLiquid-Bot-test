# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T10:37:15.421676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1261` n `12`; crypto_alt avg `0.1054` n `228`; crypto_major avg `0.1497` n `8`; equity avg `-0.0009` n `67`; fx avg `-0.0043` n `6`; index avg `0.1038` n `23`; metal avg `-0.0232` n `18`; unknown avg `0.0939` n `396`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `0.1668` n `228`; crypto_major avg `0.1618` n `8`; equity avg `-0.0075` n `67`; fx avg `0.0025` n `6`; index avg `-0.0845` n `23`; metal avg `-0.0913` n `18`; unknown avg `-0.1772` n `396`
- 4h: commodity avg `-0.0238` n `12`; crypto_alt avg `-1.407` n `228`; crypto_major avg `-0.8425` n `8`; equity avg `-0.2125` n `67`; fx avg `-0.0253` n `6`; index avg `-0.1361` n `23`; metal avg `-0.1067` n `18`; unknown avg `-0.0456` n `386`
- 24h: commodity avg `-0.3333` n `12`; crypto_alt avg `-5.4311` n `228`; crypto_major avg `-3.8011` n `8`; equity avg `-1.4182` n `67`; fx avg `0.0466` n `6`; index avg `-0.1197` n `23`; metal avg `-0.8558` n `18`; unknown avg `-2.176` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
