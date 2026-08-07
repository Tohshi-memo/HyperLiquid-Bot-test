# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T22:22:28.719156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `0.0309` n `230`; crypto_major avg `-0.0201` n `8`; equity avg `-0.0038` n `112`; fx avg `-0.0104` n `6`; index avg `0.0086` n `25`; metal avg `0.012` n `20`; unknown avg `-0.0037` n `782`
- 1h: commodity avg `-0.0833` n `12`; crypto_alt avg `-0.1191` n `230`; crypto_major avg `-0.0197` n `8`; equity avg `0.0124` n `112`; fx avg `0.0067` n `6`; index avg `-0.0018` n `25`; metal avg `0.0235` n `20`; unknown avg `-0.0724` n `782`
- 4h: commodity avg `-0.3575` n `12`; crypto_alt avg `-0.2422` n `230`; crypto_major avg `0.004` n `8`; equity avg `0.3939` n `112`; fx avg `0.0173` n `6`; index avg `0.0793` n `25`; metal avg `0.1042` n `20`; unknown avg `-0.1577` n `782`
- 24h: commodity avg `-0.2174` n `12`; crypto_alt avg `-0.4143` n `230`; crypto_major avg `-0.0885` n `8`; equity avg `1.6358` n `112`; fx avg `-0.1261` n `6`; index avg `0.0765` n `25`; metal avg `0.4783` n `20`; unknown avg `0.0969` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
