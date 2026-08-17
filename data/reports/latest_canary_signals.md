# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T09:52:23.930519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0579` n `12`; crypto_alt avg `-0.0422` n `230`; crypto_major avg `-0.022` n `8`; equity avg `0.0091` n `114`; fx avg `0.022` n `6`; index avg `0.0024` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0345` n `792`
- 1h: commodity avg `0.111` n `12`; crypto_alt avg `-0.0497` n `230`; crypto_major avg `0.0418` n `8`; equity avg `-0.1067` n `114`; fx avg `0.0328` n `6`; index avg `-0.0133` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0109` n `792`
- 4h: commodity avg `0.1875` n `12`; crypto_alt avg `-0.3439` n `230`; crypto_major avg `-0.0876` n `8`; equity avg `0.2137` n `114`; fx avg `0.0159` n `6`; index avg `0.0136` n `25`; metal avg `-0.0914` n `20`; unknown avg `0.0703` n `776`
- 24h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.3792` n `230`; crypto_major avg `0.5189` n `8`; equity avg `1.1385` n `114`; fx avg `-0.0067` n `6`; index avg `0.1216` n `25`; metal avg `0.1411` n `20`; unknown avg `0.0495` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
