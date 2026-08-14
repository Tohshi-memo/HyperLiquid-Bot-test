# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T08:22:28.238775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0309` n `230`; crypto_major avg `-0.0265` n `8`; equity avg `-0.0968` n `113`; fx avg `-0.0014` n `6`; index avg `-0.0066` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0191` n `787`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.1226` n `230`; crypto_major avg `-0.112` n `8`; equity avg `0.2228` n `113`; fx avg `-0.0431` n `6`; index avg `0.0233` n `25`; metal avg `0.0695` n `20`; unknown avg `-0.0402` n `787`
- 4h: commodity avg `0.2979` n `12`; crypto_alt avg `-0.5017` n `230`; crypto_major avg `-0.5856` n `8`; equity avg `0.1544` n `113`; fx avg `0.006` n `6`; index avg `0.0407` n `25`; metal avg `0.11` n `20`; unknown avg `-0.0179` n `755`
- 24h: commodity avg `0.0562` n `12`; crypto_alt avg `-0.7202` n `230`; crypto_major avg `-0.9105` n `8`; equity avg `1.6943` n `113`; fx avg `-0.0518` n `6`; index avg `0.3251` n `25`; metal avg `-0.0898` n `20`; unknown avg `1.0116` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
