# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T06:37:48.918870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0532` n `230`; crypto_major avg `0.0091` n `8`; equity avg `0.079` n `114`; fx avg `-0.0073` n `6`; index avg `0.0243` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0049` n `792`
- 1h: commodity avg `-0.0505` n `12`; crypto_alt avg `0.0752` n `230`; crypto_major avg `0.1501` n `8`; equity avg `0.2483` n `114`; fx avg `-0.0205` n `6`; index avg `0.0599` n `25`; metal avg `-0.0165` n `20`; unknown avg `0.1135` n `776`
- 4h: commodity avg `-0.19` n `12`; crypto_alt avg `0.2398` n `230`; crypto_major avg `0.3492` n `8`; equity avg `0.7351` n `114`; fx avg `0.0166` n `6`; index avg `0.1229` n `25`; metal avg `0.0082` n `20`; unknown avg `0.0981` n `776`
- 24h: commodity avg `-0.2253` n `12`; crypto_alt avg `0.5611` n `230`; crypto_major avg `0.8992` n `8`; equity avg `1.0549` n `114`; fx avg `-0.0395` n `6`; index avg `0.1545` n `25`; metal avg `0.1997` n `20`; unknown avg `0.1175` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
