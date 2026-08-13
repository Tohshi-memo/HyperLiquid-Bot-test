# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T18:32:14.116330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0692` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.0845` n `8`; equity avg `-0.0563` n `113`; fx avg `-0.0009` n `6`; index avg `0.0105` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.0382` n `787`
- 1h: commodity avg `-0.1471` n `12`; crypto_alt avg `-0.0658` n `230`; crypto_major avg `-0.0596` n `8`; equity avg `-0.1559` n `113`; fx avg `-0.0007` n `6`; index avg `-0.02` n `25`; metal avg `-0.0202` n `20`; unknown avg `-0.0187` n `787`
- 4h: commodity avg `0.0261` n `12`; crypto_alt avg `-1.0093` n `230`; crypto_major avg `-0.7061` n `8`; equity avg `-0.2231` n `113`; fx avg `0.0061` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0389` n `20`; unknown avg `0.0084` n `787`
- 24h: commodity avg `-0.5799` n `12`; crypto_alt avg `-0.8385` n `230`; crypto_major avg `-0.2426` n `8`; equity avg `1.1599` n `113`; fx avg `0.0025` n `6`; index avg `0.3002` n `25`; metal avg `-0.4667` n `20`; unknown avg `0.0176` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.234`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
