# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T05:22:26.963243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0447` n `230`; crypto_major avg `0.1456` n `8`; equity avg `-0.006` n `114`; fx avg `0.0021` n `6`; index avg `0.0035` n `25`; metal avg `0.0357` n `20`; unknown avg `0.0114` n `792`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.0316` n `230`; crypto_major avg `0.0308` n `8`; equity avg `0.0573` n `114`; fx avg `-0.0066` n `6`; index avg `0.0033` n `25`; metal avg `0.0258` n `20`; unknown avg `16.3621` n `792`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `0.4944` n `230`; crypto_major avg `0.5864` n `8`; equity avg `0.4943` n `114`; fx avg `0.0357` n `6`; index avg `0.0565` n `25`; metal avg `-0.0875` n `20`; unknown avg `0.1327` n `792`
- 24h: commodity avg `-0.1682` n `12`; crypto_alt avg `0.5567` n `230`; crypto_major avg `0.8681` n `8`; equity avg `0.8603` n `114`; fx avg `-0.0313` n `6`; index avg `0.0943` n `25`; metal avg `0.2191` n `20`; unknown avg `0.0643` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
