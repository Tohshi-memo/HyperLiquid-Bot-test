# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T12:37:26.734858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0482` n `230`; crypto_major avg `0.0984` n `8`; equity avg `0.0535` n `113`; fx avg `-0.0007` n `6`; index avg `0.0005` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.0646` n `787`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `0.1683` n `230`; crypto_major avg `0.3314` n `8`; equity avg `-0.1024` n `113`; fx avg `-0.0108` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.0381` n `787`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0819` n `230`; crypto_major avg `-0.2042` n `8`; equity avg `0.1523` n `113`; fx avg `-0.0402` n `6`; index avg `0.0417` n `25`; metal avg `0.1373` n `20`; unknown avg `-0.046` n `787`
- 24h: commodity avg `-0.4403` n `12`; crypto_alt avg `-0.9305` n `230`; crypto_major avg `-0.6071` n `8`; equity avg `0.5841` n `113`; fx avg `0.0089` n `6`; index avg `0.1052` n `25`; metal avg `-0.5898` n `20`; unknown avg `0.249` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2257`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
