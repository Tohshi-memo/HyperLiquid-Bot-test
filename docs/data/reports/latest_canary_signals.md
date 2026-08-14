# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T09:37:29.267867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `-0.1993` n `230`; crypto_major avg `-0.1871` n `8`; equity avg `-0.0131` n `113`; fx avg `0.0017` n `6`; index avg `-0.0028` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.0976` n `787`
- 1h: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.275` n `230`; crypto_major avg `-0.2032` n `8`; equity avg `-0.0562` n `113`; fx avg `0.0155` n `6`; index avg `0.0044` n `25`; metal avg `0.035` n `20`; unknown avg `-0.0819` n `787`
- 4h: commodity avg `0.0654` n `12`; crypto_alt avg `-0.4252` n `230`; crypto_major avg `-0.5267` n `8`; equity avg `0.3029` n `113`; fx avg `0.0067` n `6`; index avg `0.0489` n `25`; metal avg `0.2531` n `20`; unknown avg `-0.0801` n `755`
- 24h: commodity avg `0.0129` n `12`; crypto_alt avg `-0.7952` n `230`; crypto_major avg `-0.76` n `8`; equity avg `1.7338` n `113`; fx avg `-0.0679` n `6`; index avg `0.3457` n `25`; metal avg `-0.0857` n `20`; unknown avg `0.9488` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
