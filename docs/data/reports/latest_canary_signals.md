# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T20:37:29.572783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `0.0202` n `229`; crypto_major avg `0.0356` n `8`; equity avg `0.0082` n `92`; fx avg `-0.0123` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.0458` n `765`
- 1h: commodity avg `-0.0224` n `12`; crypto_alt avg `-0.1526` n `229`; crypto_major avg `-0.1853` n `8`; equity avg `-0.1286` n `92`; fx avg `-0.0162` n `6`; index avg `0.0144` n `25`; metal avg `0.0679` n `20`; unknown avg `-0.0004` n `765`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `0.0574` n `229`; crypto_major avg `0.095` n `8`; equity avg `-0.0926` n `92`; fx avg `-0.0441` n `6`; index avg `0.0442` n `25`; metal avg `-0.0183` n `20`; unknown avg `-0.2362` n `765`
- 24h: commodity avg `-0.2367` n `12`; crypto_alt avg `0.5236` n `229`; crypto_major avg `0.6618` n `8`; equity avg `-0.6533` n `92`; fx avg `-0.1689` n `6`; index avg `0.0391` n `25`; metal avg `0.1353` n `20`; unknown avg `-0.1873` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
