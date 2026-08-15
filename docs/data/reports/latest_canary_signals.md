# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T22:07:25.771614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.0103` n `230`; crypto_major avg `-0.024` n `8`; equity avg `-0.017` n `114`; fx avg `-0.0018` n `6`; index avg `0.0014` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.097` n `791`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0531` n `230`; crypto_major avg `0.0466` n `8`; equity avg `0.0029` n `114`; fx avg `0.0035` n `6`; index avg `0.0031` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0063` n `791`
- 4h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0533` n `230`; crypto_major avg `0.0022` n `8`; equity avg `0.0472` n `114`; fx avg `0.0049` n `6`; index avg `-0.0079` n `25`; metal avg `0.0019` n `20`; unknown avg `0.9395` n `791`
- 24h: commodity avg `-0.096` n `12`; crypto_alt avg `0.8787` n `230`; crypto_major avg `0.5557` n `8`; equity avg `0.1463` n `114`; fx avg `0.0145` n `6`; index avg `-0.0097` n `25`; metal avg `0.0067` n `20`; unknown avg `0.0856` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
