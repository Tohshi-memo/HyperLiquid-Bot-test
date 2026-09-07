# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T07:07:26.336906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0551` n `12`; crypto_alt avg `0.0575` n `232`; crypto_major avg `0.038` n `8`; equity avg `-0.0037` n `134`; fx avg `0.0273` n `6`; index avg `0.0108` n `26`; metal avg `-0.0257` n `20`; unknown avg `-0.0242` n `794`
- 1h: commodity avg `-0.1431` n `12`; crypto_alt avg `-0.0155` n `232`; crypto_major avg `-0.104` n `8`; equity avg `0.0426` n `134`; fx avg `0.0077` n `6`; index avg `0.0578` n `26`; metal avg `0.0808` n `20`; unknown avg `0.9381` n `782`
- 4h: commodity avg `0.0508` n `12`; crypto_alt avg `-0.2475` n `232`; crypto_major avg `-0.2251` n `8`; equity avg `0.1956` n `134`; fx avg `-0.0444` n `6`; index avg `0.0954` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.8391` n `758`
- 24h: commodity avg `0.0157` n `12`; crypto_alt avg `0.249` n `232`; crypto_major avg `-0.5399` n `8`; equity avg `0.4576` n `134`; fx avg `-0.0122` n `6`; index avg `0.0642` n `26`; metal avg `-0.1588` n `20`; unknown avg `382.8353` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
