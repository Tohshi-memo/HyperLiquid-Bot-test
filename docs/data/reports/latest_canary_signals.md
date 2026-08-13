# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T20:22:31.862878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.0055` n `230`; crypto_major avg `-0.0019` n `8`; equity avg `-0.0284` n `113`; fx avg `-0.0017` n `6`; index avg `0.0012` n `25`; metal avg `0.0235` n `20`; unknown avg `-0.0165` n `787`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.0081` n `230`; crypto_major avg `0.0077` n `8`; equity avg `-0.2677` n `113`; fx avg `-0.001` n `6`; index avg `-0.027` n `25`; metal avg `0.018` n `20`; unknown avg `0.0007` n `787`
- 4h: commodity avg `-0.2795` n `12`; crypto_alt avg `-0.1442` n `230`; crypto_major avg `0.0852` n `8`; equity avg `0.0293` n `113`; fx avg `0.006` n `6`; index avg `0.0216` n `25`; metal avg `-0.0477` n `20`; unknown avg `0.0411` n `787`
- 24h: commodity avg `-0.5014` n `12`; crypto_alt avg `-0.2872` n `230`; crypto_major avg `0.382` n `8`; equity avg `1.5099` n `113`; fx avg `0.0092` n `6`; index avg `0.3053` n `25`; metal avg `-0.5042` n `20`; unknown avg `0.0565` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2439`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
