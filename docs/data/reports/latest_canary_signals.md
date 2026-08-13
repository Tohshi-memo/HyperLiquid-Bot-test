# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T17:52:26.833005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `12`; crypto_alt avg `0.0482` n `230`; crypto_major avg `-0.0003` n `8`; equity avg `-0.0525` n `113`; fx avg `-0.0045` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0053` n `787`
- 1h: commodity avg `-0.0648` n `12`; crypto_alt avg `0.2532` n `230`; crypto_major avg `0.1258` n `8`; equity avg `0.2109` n `113`; fx avg `0.0028` n `6`; index avg `0.0137` n `25`; metal avg `-0.0128` n `20`; unknown avg `0.0768` n `787`
- 4h: commodity avg `0.0913` n `12`; crypto_alt avg `-0.6143` n `230`; crypto_major avg `-0.4345` n `8`; equity avg `0.4091` n `113`; fx avg `-0.0028` n `6`; index avg `0.1164` n `25`; metal avg `-0.0766` n `20`; unknown avg `-0.1295` n `787`
- 24h: commodity avg `-0.4077` n `12`; crypto_alt avg `-0.7709` n `230`; crypto_major avg `-0.2761` n `8`; equity avg `1.2373` n `113`; fx avg `0.0007` n `6`; index avg `0.3254` n `25`; metal avg `-0.423` n `20`; unknown avg `0.0098` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2341`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
