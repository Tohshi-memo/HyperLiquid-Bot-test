# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T08:22:27.552224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0542` n `13`; crypto_alt avg `0.0082` n `235`; crypto_major avg `-0.0393` n `8`; equity avg `-0.054` n `149`; fx avg `-0.0009` n `6`; index avg `-0.0048` n `26`; metal avg `0.0204` n `20`; unknown avg `0.8178` n `1074`
- 1h: commodity avg `0.0738` n `13`; crypto_alt avg `0.4106` n `235`; crypto_major avg `0.3579` n `8`; equity avg `0.0926` n `149`; fx avg `-0.0073` n `6`; index avg `0.0249` n `26`; metal avg `0.0589` n `20`; unknown avg `0.8834` n `1056`
- 4h: commodity avg `-0.1524` n `13`; crypto_alt avg `0.4692` n `235`; crypto_major avg `0.0229` n `8`; equity avg `0.1618` n `149`; fx avg `-0.002` n `6`; index avg `0.0532` n `26`; metal avg `0.0562` n `20`; unknown avg `0.4385` n `976`
- 24h: commodity avg `-0.1587` n `13`; crypto_alt avg `-1.1833` n `235`; crypto_major avg `-0.8885` n `8`; equity avg `0.1566` n `149`; fx avg `0.0388` n `6`; index avg `0.1427` n `26`; metal avg `-0.2206` n `20`; unknown avg `0.6209` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
