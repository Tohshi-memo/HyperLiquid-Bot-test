# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T14:22:41.065096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0866` n `12`; crypto_alt avg `0.0785` n `230`; crypto_major avg `0.1139` n `8`; equity avg `0.2452` n `113`; fx avg `-0.0118` n `6`; index avg `0.0373` n `25`; metal avg `-0.0561` n `20`; unknown avg `-0.0112` n `787`
- 1h: commodity avg `-0.0518` n `12`; crypto_alt avg `0.2373` n `230`; crypto_major avg `0.1498` n `8`; equity avg `1.538` n `113`; fx avg `-0.0246` n `6`; index avg `0.2091` n `25`; metal avg `-0.1443` n `20`; unknown avg `0.0769` n `787`
- 4h: commodity avg `-0.2827` n `12`; crypto_alt avg `0.1983` n `230`; crypto_major avg `0.181` n `8`; equity avg `1.6573` n `113`; fx avg `-0.043` n `6`; index avg `0.2629` n `25`; metal avg `-0.1414` n `20`; unknown avg `0.1921` n `787`
- 24h: commodity avg `-0.5271` n `12`; crypto_alt avg `-0.0391` n `230`; crypto_major avg `0.4852` n `8`; equity avg `1.9967` n `113`; fx avg `-0.0061` n `6`; index avg `0.2937` n `25`; metal avg `-0.6722` n `20`; unknown avg `0.4176` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2295`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
