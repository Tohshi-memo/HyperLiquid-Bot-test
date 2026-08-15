# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T14:07:31.918224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.0156` n `230`; crypto_major avg `-0.0251` n `8`; equity avg `0.0182` n `114`; fx avg `-0.0026` n `6`; index avg `-0.0028` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0095` n `791`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `0.0747` n `230`; crypto_major avg `-0.0417` n `8`; equity avg `0.0407` n `114`; fx avg `0.0036` n `6`; index avg `0.0036` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.026` n `791`
- 4h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.0171` n `230`; crypto_major avg `0.1188` n `8`; equity avg `0.0635` n `114`; fx avg `0.001` n `6`; index avg `0.0275` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.1039` n `791`
- 24h: commodity avg `-0.0402` n `12`; crypto_alt avg `1.189` n `230`; crypto_major avg `0.5435` n `8`; equity avg `-0.7328` n `114`; fx avg `0.0856` n `6`; index avg `-0.1538` n `25`; metal avg `-0.0566` n `20`; unknown avg `0.039` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
