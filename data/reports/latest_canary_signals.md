# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T10:37:27.536463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0201` n `12`; crypto_alt avg `0.0676` n `230`; crypto_major avg `0.009` n `8`; equity avg `-0.0647` n `113`; fx avg `0.0048` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0422` n `20`; unknown avg `-0.0011` n `787`
- 1h: commodity avg `-0.1039` n `12`; crypto_alt avg `0.0508` n `230`; crypto_major avg `-0.0073` n `8`; equity avg `0.1171` n `113`; fx avg `0.0251` n `6`; index avg `0.0215` n `25`; metal avg `-0.0569` n `20`; unknown avg `0.1949` n `787`
- 4h: commodity avg `-0.1282` n `12`; crypto_alt avg `-0.3077` n `230`; crypto_major avg `-0.2413` n `8`; equity avg `0.4826` n `113`; fx avg `-0.0277` n `6`; index avg `0.0744` n `25`; metal avg `0.1038` n `20`; unknown avg `0.1076` n `787`
- 24h: commodity avg `-0.0685` n `12`; crypto_alt avg `-0.739` n `230`; crypto_major avg `-0.6635` n `8`; equity avg `1.8448` n `113`; fx avg `-0.0611` n `6`; index avg `0.3534` n `25`; metal avg `-0.2259` n `20`; unknown avg `0.9412` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
