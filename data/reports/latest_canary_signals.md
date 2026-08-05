# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T14:22:41.796854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `-0.1176` n `230`; crypto_major avg `-0.0985` n `8`; equity avg `-0.4083` n `108`; fx avg `0.0168` n `6`; index avg `-0.0512` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.0056` n `782`
- 1h: commodity avg `-0.284` n `12`; crypto_alt avg `-0.0221` n `230`; crypto_major avg `0.1182` n `8`; equity avg `0.4265` n `108`; fx avg `-0.0054` n `6`; index avg `0.0325` n `25`; metal avg `0.1943` n `20`; unknown avg `0.0246` n `782`
- 4h: commodity avg `-0.4334` n `12`; crypto_alt avg `-0.0084` n `230`; crypto_major avg `0.2039` n `8`; equity avg `0.2251` n `108`; fx avg `-0.0294` n `6`; index avg `0.0941` n `25`; metal avg `0.2733` n `20`; unknown avg `-0.015` n `782`
- 24h: commodity avg `-0.2465` n `12`; crypto_alt avg `1.0691` n `230`; crypto_major avg `0.9061` n `8`; equity avg `1.7011` n `108`; fx avg `0.0522` n `6`; index avg `0.3924` n `25`; metal avg `0.8441` n `20`; unknown avg `0.7549` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
