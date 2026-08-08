# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T03:48:04.841095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0236` n `230`; crypto_major avg `0.0197` n `8`; equity avg `0.0115` n `112`; fx avg `0.0001` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.2832` n `783`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.2241` n `230`; crypto_major avg `0.3641` n `8`; equity avg `0.0041` n `112`; fx avg `0.0062` n `6`; index avg `-0.0048` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0766` n `783`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `0.4309` n `230`; crypto_major avg `0.5272` n `8`; equity avg `-0.022` n `112`; fx avg `0.0049` n `6`; index avg `0.007` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0558` n `783`
- 24h: commodity avg `-0.1762` n `12`; crypto_alt avg `0.0498` n `230`; crypto_major avg `0.6206` n `8`; equity avg `1.7067` n `112`; fx avg `-0.0793` n `6`; index avg `0.2239` n `25`; metal avg `0.3468` n `20`; unknown avg `0.0112` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
